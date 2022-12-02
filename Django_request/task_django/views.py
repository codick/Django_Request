from django.shortcuts import render
from django.http import HttpResponse

def task(request):
    host = request.META["HTTP_HOST"]
    info = request.META["HTTP_USER_AGENT"]
    ip_client = request.META["REMOTE_ADDR"]
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>Information: {info}</p>
    <p>Ip: {ip_client}</p>
""")

def page_not_found_view(request):
    return HttpResponse(request, '404.html', status=404, reason="Ошибка 404")

def user(request, login='kirill',folder_name='kostya',post_number='5'):
    return HttpResponse(f"""
    <p> Login: {login} </p>
    <p> Folder_name: {folder_name} </p>
    <p> post_number: {post_number} </p>
    """)