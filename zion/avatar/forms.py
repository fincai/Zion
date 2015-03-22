from PIL import Image
from django import forms
from zion.settings import UPLOAD_LIMIT

class UploadAvatarForm(forms.Form):
    avatar_upload = forms.ImageField() 

    def clean_avatar_upload(self):
        image = self.cleaned_data['avatar_upload']
        if image.size > UPLOAD_LIMIT:
            raise forms.ValidationError("Avatar image cannot be larger than 1MB")
        return image
    
