from django.http import HttpResponse
from django.shortcuts import render

from aa_app import models

import json

EMPTY_JSON_200 = HttpResponse(json.dumps({}), content_type = "application/json")

def newUser(request):
    d = json.loads(bytes.decode(request.body))
    u = models.newUser(d["username"], d["password"], d["email"], d["startYear"])
    request.session["cookieID"] = u.cookieID
    return EMPTY_JSON_200

def login(request):
    d = json.loads(bytes.decode(request.body))
    u = models.User.objects.get(username = d["username"])
    assert u.password == d["password"]
    request.session["cookieID"] = u.cookieID
    return EMPTY_JSON_200

def logout(request):
    del request.session["cookieID"]
    return EMPTY_JSON_200

def setEmail(request):
    d = json.loads(bytes.decode(request.body))
    u = models.User.objects.get(cookieID = request.session["cookieID"])
    u.setEmail(d["email"])
    return EMPTY_JSON_200

def setPassword(request):
    d = json.loads(bytes.decode(request.body))
    u = models.User.objects.get(cookieID = request.session["cookieID"])
    u.setPassword(d["password"])
    return EMPTY_JSON_200

def setUsername(request):
    d = json.loads(bytes.decode(request.body))
    u = models.User.objects.get(cookieID = request.session["cookieID"])
    u.setUsername(d["username"])
    return EMPTY_JSON_200
