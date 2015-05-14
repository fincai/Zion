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


class ChangePasswordForm(forms.Form):
    password = forms.CharField(label='Password',
                               help_text="Password you will be using to sign in to your account. Make sure it's strong.",
                               max_length=255, widget=forms.PasswordInput)
    password_rep = forms.CharField(max_length=255, widget=forms.PasswordInput)
    


    def clean_password_rep(self):
        if 'password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_rep']:
                raise forms.ValidationError('Entered passwords do not match.')
        return self.cleaned_data['password_rep']
