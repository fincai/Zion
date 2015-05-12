from django import forms

class SignInForm(forms.Form):
    user_email = forms.EmailField(max_length=255, label='Your email')
    user_password = forms.CharField(widget=forms.PasswordInput, 
                        max_length=255, label='Your password')
    user_remember_me = forms.BooleanField(label='Stay signed in', 
                help_text='Sign me in automatically next time', required=False)


class ChangeEmailForm(forms.Form):
	email = forms.EmailField(label='E-mail address', 
                             help_text="Working e-mail inbox is required to maintain control over your forum account.",
                             max_length=255)

