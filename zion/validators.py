import re
from django import forms

def validate_username(value):
    if len(value) < 3:
        raise forms.ValidationError(
            'Username must be at least 3 characters long.')
    if len(value) > 16:
        raise forms.ValidationError(
            'Username cannot be longer than 16 characters.')
    if not re.search(r'[\w_]+', value):
        raise forms.ValidationError(
            'Username can only contain letter, number or underscore.')
            

    
def validate_password(value):
    pass
