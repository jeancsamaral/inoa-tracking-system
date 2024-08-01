# tasks.py

from celery import shared_task

@shared_task
def example_task(param):
    print(f'Executing task with param: {param}')
