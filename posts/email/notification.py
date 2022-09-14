
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from friendship.models import Friend
from categories.models import Categories
from posts.models import Post
from posts.serializers import UserMailSerializer
from users.models import User
from datetime import datetime, timedelta
from django.utils import timezone


class Send_notification():
    def friend_notification(user_id):

        user = get_object_or_404(User, id = user_id)

        user_friends = Friend.objects.friends(user)

        friends_email = UserMailSerializer(user_friends, many=True)

        if friends_email.data:
            mail_list = []
            for email in list(friends_email.data):
                    mail_list.append(email['email'])
                    
            send_mail(
                subject = f'New Posts',
                message = f'Your friend {user.username}, make a new post at thinki wiki',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = mail_list,
                fail_silently = False
            )

    def category_notification(category_id):
        
        category = get_object_or_404(Categories, id = category_id)


        if category.categories_followed.all():              
           
            followers_mails = UserMailSerializer(category.categories_followed, many=True)
            
           
            last_day = datetime.now(tz=timezone.utc) + timedelta(days=-1)
            today = datetime.now(tz=timezone.utc)

            posts_from_last_day = Post.objects.filter(created_at__gte=last_day, created_at__lte = today)
            if followers_mails and posts_from_last_day:

                mail_list = []
                for email in list(followers_mails.data):
                    mail_list.append(email['email'])

                send_mail(
                    subject = f'New Posts',
                    message = f'Hello Thinker, the category {category.name}, have {len(posts_from_last_day)} new posts at thinki wiki',
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = mail_list,
                    fail_silently = False
                )
    @classmethod
    def categories_notification(cls):
        
        categories = Categories.objects.all()

        for category in categories:
            cls.category_notification(category.id)
        




