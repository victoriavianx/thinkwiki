from django.contrib.auth import authenticate

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authtoken.models import Token

from users.permissions import IsAdminOwnerOrReadOnly

from .models import User

from .serializers import IsActiveSerializer, UserSerializer, UserDetailSerializer, LoginSerializer

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

class UserDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserManagementView(UpdateAPIView):
    permission_classes = [IsAdminOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = IsActiveSerializer