from django import forms

class NewCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4,}))
    

def clean_comment(self):
    text = self.cleaned_data['comment']
    if len(text) < 5:
        raise forms.ValidationError('At least 5 characters.')
    return text
