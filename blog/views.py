from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here (the logic of our application).
# Views are functions that take a web request 
# and return a web response. 
# This response can be the HTML contents of a web page, 
# or a redirect, or a 404 error, or an XML document, 
# or an image, etc.
# The view itself contains whatever arbitrary logic 
# is necessary to return that response. 
# This code is in blog/views.py
# multiple steps to this bit, change views.py, then urls.py, then urls.py in the project folder!
# you will then get an error until you create a template!
def post_list(request):
    #See queryset chapter. This allows us to have dynamic content in our website.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #then we past the posts to the render function,
    #which will use a template to create the HTML page that is sent to the browser.
    return render(request, 'blog/post_list.html', {'posts': posts})
    #after you add the above, you have to go back and modify the template
    #use template tags