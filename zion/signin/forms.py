from django import forms

class SignInForm(forms.Form):
    user_email = forms.EmailField(max_length=255, label='Your email')
    user_password = forms.CharField(widget=forms.PasswordInput, 
                        max_length=255, label='Your password')
    user_remember_me = forms.BooleanField(label='Stay signed in', 
                help_text='Sign me in automatically next time', required=False)


            
        


