from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import User
from utils import JSON, convert_to_builtin_type

# from django.utils import simplejson
# from django.core import serializers
import json

 
def login(req):
    if req.method == "GET":
        return render_to_response('login.html')
    else:
        username = req.POST['username']
        password = req.POST['password']
        users = User.objects.filter(username=username,password=password)
        if users:
            req.session['username'] = username
#             res = json.dumps(JSON(), default=convert_to_builtin_type)
            res = json.dumps(JSON(data=[1,2,3]), default=convert_to_builtin_type)
            print(res)
            return HttpResponse(res, content_type="application/json")
        else:
            return HttpResponseRedirect('/login')
        
def index(req):
    username = req.session.get('username',None)
    if username:
        user = User.objects.filter(username=username)
        return render_to_response("index.html")
    else:
        return HttpResponseRedirect('/login') 
    

def logout(req):
    try:
        del req.session['username']
    except KeyError:
        pass
    response = HttpResponseRedirect('/login')
#     response.delete_cookie('username')
    return response