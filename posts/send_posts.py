from apscheduler.schedulers.background import BackgroundScheduler
from posts.email.notification import Send_notification

def tests():
    print('oi')

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(Send_notification.categories_notification, 'interval', hours=24)
    scheduler.start()



