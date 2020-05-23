from django import forms
from .models import Comment, User

# from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
        fields = ['content']
        
class UpdateCommentForm(BSModalForm):
    class Meta:
        model = Comment
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
        fields = ['content']