
from django.shortcuts import render, get_object_or_404

from django.core.mail import send_mail

from django.conf import settings

from .models import Post

from .forms import RequestForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from django.shortcuts import render_to_response








# Create your views here.

def post_list(request):

	queryset1_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset1_list = queryset1_list.filter(Q(title__icontains=query))
	
	paginator = Paginator(queryset1_list, 4 ) # Show 25 contacts per page

	page = request.GET.get('page')

	try:
		queryset1 = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		queryset1 = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset1 =	paginator.page(paginator.num_pages)



	
	context = {
	   "posts": queryset1
	   
	}
	
	return render(request, 'myblog/post_list.html',context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

def post_new(request):
    form_class = RequestForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
        	name = form.cleaned_data.get("name")
        	topic = form.cleaned_data.get("topic")
        	details = form.cleaned_data.get("details")
        	form_email = form.cleaned_data.get("email")
        	subject = 'Site contact form'
        	from_email = settings.EMAIL_HOST_USER
        	to_email = [form_email, 'vivektalwar13071999@gmail.com']
        	contact_message = "NAME-%s ,TOPIC-%s, DETAILS-%s, via EMAIL-%s"%(name,
        		topic,
        		details,
        		form_email)
        	send_mail(subject, contact_message, from_email, [to_email] ,fail_silently=True)


    
    return render(request, 'myblog/post_edit.html', {
        'form': form_class,
    })

def post_about(request):
   return render_to_response('myblog/post_info.html')