import logging
from datetime import datetime
from time import sleep

from belhard.celery import app
from .models import Task


@app.task
def my_task():
    sleep(2)
    task = Task(name='task')
    task.save()
