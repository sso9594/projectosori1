from typing_extensions import Self
from xml.etree.ElementTree import Comment
from django import forms
from .models import Post,Comment,FreePost,FreeComment

class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        #fields ={'title','body'}

    def __init__(self, *args, **kwargs):
        super(postform, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }

class Freepostform(forms.ModelForm):
    class Meta:
        model=FreePost
        fields='__all__'
        #fields ={'title','body'}

    def __init__(self, *args, **kwargs):
        super(Freepostform, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields=['comment']

    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }        