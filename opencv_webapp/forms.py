from django import forms
from .models import ImageUploadModel


class SimpleUploadForm(forms.Form):
   title = forms.CharField(max_length=50)
   # ImageField Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
   # file = forms.FileField()
   image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    #form을 통해 받아들여야 할 데이터가 명시되어 잇는 메타데이터(DB테이블을 연결)
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document',)
