from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data['caption']
            form.save()
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

