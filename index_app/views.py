from django.shortcuts import render, render_to_response

# Create your views here.
def index(req):
    return render_to_response('index_app/index.html', {})

def about(req):
    return render_to_response('index_app/about.html', {})

def services(req):
    return render_to_response('index_app/services.html', {})

def blog(req):
    return render_to_response('index_app/blog.html', {})

def contact(req):
    return render_to_response('index_app/contact.html', {})
