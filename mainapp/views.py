from cgitb import enable
from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("testttttt")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sentttttttt")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 0, minute = 2)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_tas5ss_"+"5", task='send_mail_app.tasks.send_mail_func',enabled=True)#, args = json.dumps([[2,3]]))
    return HttpResponse("Doneeeeeeeeee")

