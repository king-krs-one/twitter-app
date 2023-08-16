from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet
import random

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html")
    return HttpResponse('<h1>Hello there</h1>')

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{
        "id": x.id,
        "content": x.content,
        "likes": random.randint(0,20)
    } for x in qs]

    data = {
        "isUser": False,
        "response": tweet_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScipt or Swift/Java/iOS/Android
    return json
    """
    
    data = {
        "id": tweet_id,
    }
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not found"
        status = 404

    return JsonResponse(data, status=status) # json.dumps content_type='application/json'