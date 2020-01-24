from django.shortcuts import render
from .forms import PostForm
from . import models

from django.views.generic.edit import CreateView

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # user.refresh_from_db()
            cap = post.cleaned_data('caption')
            form =PostForm()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password= raw_password)
            # login(request,user)
            return redirect('account:index')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html',{'form':form})

# def like(request,pk):
#     feed = get_object_or_404(Feed,pk=pk)
#     user= request.user
#     if request.method=='POST':
#         if feed.user_like.filter(id=user.id).exists():
#             feed.user_like.remove(user)
#             return render(request, 'index.html', {'form':form})
#         else:
#             feed.user_like.add(user)
#             return render(request, 'index.html', {'form':form})

