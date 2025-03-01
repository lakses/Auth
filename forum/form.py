from django import forms
from .models import Forum
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ForumFormeeees(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'description'] 
