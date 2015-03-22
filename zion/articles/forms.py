from django import forms

class NewArticleForm(forms.Form):
    name = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':'8', }))

def clean_body(self):
    return self.cleaned_data['body']
