from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('', include('blog.urls')),
]

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
]

path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

path('drafts/', views.post_draft_list, name='post_draft_list'),

path('post/<pk>/publish/', views.post_publish, name='post_publish'),

path('post/<pk>/remove/', views.post_remove, name='post_remove'),

<a class="btn btn-default" href="{% url 'add_comment_to_post' pk=post.pk %}">Add comment</a>

path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),

path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),