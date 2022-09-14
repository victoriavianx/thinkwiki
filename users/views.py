from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from utils.mixins import SerializerByMethodMixin

from .models import User

from .serializers import IsActiveSerializer, UserListSerializer, UserSerializer, UserDetailSerializer, LoginSerializer, PendingRequestsListSerializer, ReturnOfPendingRequestsList

from users.permissions import IsAdminOrOwner, IsAdminOwnerOrReadOnly

from friendship.models import Friend, FriendshipRequest

from friendship.exceptions import AlreadyExistsError, AlreadyFriendsError


class UserView(SerializerByMethodMixin, ListCreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_map = {
        "GET": UserListSerializer,
        "POST": UserSerializer
    }
    
class LoginView(APIView):
    queryset = Token.objects.all()
    serializer_class = LoginSerializer

    def post(self, request: Request) -> Response:
        serialized_login = LoginSerializer(data=request.data)
        serialized_login.is_valid(raise_exception=True)

        user = authenticate(
            username=serialized_login.validated_data["username"],
            password=serialized_login.validated_data["password"],
        )

        if not user:
            return Response({"detail": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})
        
class UserDetailView(SerializerByMethodMixin, RetrieveUpdateAPIView):
    permission_classes = [IsAdminOwnerOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_map = {
        "GET": UserDetailSerializer,
        "PATCH": UserSerializer
    }

class UserManagementView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserManagementDetailView(UpdateAPIView):
    permission_classes = [IsAdminOrOwner]
    queryset = User.objects.all()
    serializer_class = IsActiveSerializer

# Views Friend
class SendFriendRequestAndDeleteFriendshipView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, id_friend:str) -> Response:
        friend = get_object_or_404(User, id=id_friend)

        try:      
            Friend.objects.add_friend(request.user, friend, message="Friend request sent.")
        except AlreadyExistsError:
            return Response({"message": "You already requested friendship from this user."}, status=status.HTTP_409_CONFLICT)
        except AlreadyFriendsError:
            return Response({"message": "Users are already friends"}, status=status.HTTP_409_CONFLICT)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request: Request, id_friend: str) -> Response:
        listFriends = Friend.objects.friends(request.user)
        friend = get_object_or_404(User, id=id_friend)

        if not friend in listFriends:
            return Response({"message": "You and this user are no longer friends,"}, status=status.HTTP_404_NOT_FOUND)
            
        Friend.objects.remove_friend(request.user, friend)

        return Response(status=status.HTTP_204_NO_CONTENT)


class AcceptOrRejectFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, id_friend:str) -> Response:
        accept = request.query_params.get("accept", None)

        user = get_object_or_404(User, id=id_friend)

        try:
            friend_request = FriendshipRequest.objects.get(from_user=user, to_user=request.user)
        except ObjectDoesNotExist:    
            return Response({"message": "FriendshipRequest matching query does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if accept == "1":
            friend_request.accept()
        else:
            friend_request.reject()
            friend_request.delete()

        return Response(status=status.HTTP_200_OK)        


class ListPendingRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friendship_request = Friend.objects.unrejected_requests(user=request.user)

        serializer = PendingRequestsListSerializer(friendship_request, many=True)
    
        return Response(serializer.data)
  

class ListFriendsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        listFriends = Friend.objects.friends(request.user)

        serializer = ReturnOfPendingRequestsList(listFriends, many=True)

        return Response(serializer.data)

