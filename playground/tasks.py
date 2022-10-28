from time import sleep
from celery import shared_task

@shared_task
def notify_customers(message):
    '''A celery task to simulate sending messages'''
    print('Sending 10k email...')
    print(message)
    sleep(10)
    print('emails were send successfully')
