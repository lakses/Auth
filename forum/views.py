from django.shortcuts import render, get_object_or_404,redirect
from .models import Forum, Topic, Comment
from django.contrib.auth.decorators import login_required
from .form import ForumFormeeees
from .form import CommentForm
def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum_list.html', {'forums': forums})
def topic_list(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    topics = forum.topics.all()

    if request.method == 'POST':
        topic_id = request.POST.get('topic_id')  
        topic = get_object_or_404(Topic, id=topic_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            return redirect('topic_list', forum_id=forum.id)

    return render(request, 'topic_list.html', {'forum': forum, 'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    comments = topic.comments.all()
    return render(request, 'topic_detail.html', {'topic': topic, 'comments': comments})

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumFormeeees(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.creator = request.user
            forum.save()
            return redirect('forum_list')
    else:
        form = ForumFormeeees()
    return render(request, 'create.html', {'form': form})