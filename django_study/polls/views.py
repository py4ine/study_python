from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    print("클라이언트의 요청을 받음")
    input("요청을 처리하는 상태 (완료하려면 Enter)")
    return HttpResponse("Hello, you're at the index.")