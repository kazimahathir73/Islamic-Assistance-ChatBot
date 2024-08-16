from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .chatbot import get_response

def function(request):
    return render(request, 'chats/index.html')

def getResponse(request):
    message = request.GET.get('userMessage')
    bot_response = get_response(message)
    return HttpResponse(bot_response)

