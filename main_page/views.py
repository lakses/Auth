from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NewsForm
from .models import News
from django.contrib import messages
from django.shortcuts import get_object_or_404
def main(request):
    if 'home_link' in request.POST:
        redirect('account/home/')
    elif 'register'in request.POST:
        redirect('account/register/')

    news = News.objects.all().order_by('-pub_date')
    return render(request, 'main.html', {'news': news})

@staff_member_required
def create_news(request):
    if request.method == 'POST':
        if 'create_news' in request.POST:  
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news = form.save(commit=False)
                news.author = request.user
                news.save()
                messages.success(request, 'Новость успешно создана!')
                return redirect('create_news')
        
        elif 'delete_news' in request.POST:
            title_to_delete = request.POST.get('title_to_delete')
            try:
                news_to_delete = News.objects.get(title=title_to_delete)
                news_to_delete.delete()
                messages.success(request, f'Новость "{title_to_delete}" успешно удалена!')
            except News.DoesNotExist:
                messages.error(request, f'Новость с названием "{title_to_delete}" не найдена.')
            return redirect('create_news')
    else:
        form = NewsForm()
    
    return render(request, 'create_news.html', {'form': form})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news_item': news_item})