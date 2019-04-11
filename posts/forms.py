from django import forms
from .models import Post, Image, Comment

class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        # fields = '__all__' # 입력을 받을 수 있도록 보여주는 것
        fields =['content',] 
        
class ImageForm(forms.ModelForm):
    class Meta :
        model = Image
        # fields = '__all__'
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs = {'multiple':True})
        }

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['content',] # content만 입력