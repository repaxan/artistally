from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ValidationError

from aa_app import models

from decimal import Decimal
import json

@login_required
@user_passes_test(lambda u: not u.confirmToken)
def newWriteup(request):
    d = json.loads(bytes.decode(request.body))
    u = request.user
    try:
        e = models.Event.objects.get(ID = int(d["eventID"]))
        w = models.newWriteup(u, e, int(d["rating"]), d["review"])
    except models.Event.DoesNotExist as ex:
        return JsonResponse({"error": "invalid: event"}, status = 400)
    except ValidationError as ex:
        return JsonResponse({"error": "invalid: %s" % ", ".join(ex.message_dict.keys())}, status = 400)
    return JsonResponse({"writeupID": w.ID})

@login_required
@user_passes_test(lambda u: not u.confirmToken)
def setRating(request):
    d = json.loads(bytes.decode(request.body))
    u = request.user
    try:
        w = models.Writeup.objects.get(ID = int(d["writeupID"]))
        if w.user != u:
            return JsonResponse({"error": "not your writeup"}, status = 400)
        w.setRating(int(d["rating"]))
    except models.Writeup.DoesNotExist as ex:
        return JsonResponse({"error": "couldn't find the writeup"}, status = 400)
    except ValidationError as ex:
        return JsonResponse({"error": "invalid: %s" % ", ".join(ex.message_dict.keys())}, status = 400)
    return JsonResponse({})

@login_required
@user_passes_test(lambda u: not u.confirmToken)
def setReview(request):
    d = json.loads(bytes.decode(request.body))
    u = request.user
    try:
        w = models.Writeup.objects.get(ID = int(d["writeupID"]))
        if w.user != u:
            return JsonResponse({"error": "not your writeup"}, status = 400)
        w.setReview(d["review"])
    except models.Writeup.DoesNotExist as ex:
        return JsonResponse({"error": "couldn't find the writeup"}, status = 400)
    except ValidationError as ex:
        return JsonResponse({"error": "invalid: %s" % ", ".join(ex.message_dict.keys())}, status = 400)
    return JsonResponse({})

@login_required
@user_passes_test(lambda u: not u.confirmToken)
def deleteWriteup(request):
    d = json.loads(bytes.decode(request.body))
    u = request.user
    try:
        w = models.Writeup.objects.get(ID = int(d["writeupID"]))
        if w.user != u:
            return JsonResponse({"error": "not your writeup"}, status = 400)
        w.delete()
    except models.Item.DoesNotExist as ex:
        return JsonResponse({"error": "couldn't find the writeup"}, status = 400)
    return JsonResponse({})
