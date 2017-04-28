from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    name= request.GET.get('name')
    flink = request.GET.get('flink')
    tlink = request.GET.get('tlink')
    try:
        user1 = user.objects.filter(username=name)
        for object in user1:
            object.f_link=flink
            object.t_link=tlink
            object.save()

        return HttpResponse(object)
    except:
        HttpResponse('no such user exist.')

def detail(request,username):
    return HttpResponse('hye i am %s'% username)


def delUser(request):
    name = request.GET.get('name')
    try:
        user1= user.objects.filter(username=name)
        user1.delete()
        return HttpResponse('user has deleted')
    except:
        return HttpResponse('no such user exist.')


def addUser(request):

    try:
        name = request.GET.get('name')
        flink = request.GET.get('flink')
        tlink = request.GET.get('tlink')
        object=user()
        object.username=name
        object.f_link = flink
        object.t_link = tlink
        object.save()

        return HttpResponse(object)
    except:
        return HttpResponse('could not add this user.')

def showUsers(request):
    user1=user.objects.all()
    data= ''
    for object in user1:
        data += object.username + ', ' + object.f_link + ' , '+ object.t_link+ ' ---- '

    return HttpResponse(data)

def showDetail(requst):
    name = requst.GET.get('name')
    try:
        user1=user.objects.filter(username=name)
        return HttpResponse(user1)
    except:
        return HttpResponse('no such user exist')
def tempContact(request):
    user1 = TempContact.objects.all()
    data = ''
    for object in user1:
        data += str(object.f_name) + ', ' +str(object.l_name) + ' , ' + str(object.other_phone) + ' , '+str(object.gender)+' , '+str(object.city)+'\n'+' , '+str(object.photo) + ' , '+str(object.profile_picture)+' ---- '

    return HttpResponse(data)