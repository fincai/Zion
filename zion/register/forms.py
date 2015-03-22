from django import forms
from zion.validators import validate_username
from zion.signin.models import User

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20,
            help_text="Your displayed username. Between 3 and 16 characters, only letters and digits are allowed.")
    email = forms.EmailField(label='E-mail address', 
                             help_text="Working e-mail inbox is required to maintain control over your forum account.",
                             max_length=255)
    email_rep = forms.EmailField(max_length=255)
    password = forms.CharField(label='Password',
                               help_text="Password you will be using to sign in to your account. Make sure it's strong.",
                               max_length=255, widget=forms.PasswordInput)
    password_rep = forms.CharField(max_length=255, widget=forms.PasswordInput)
    
    accepted_rules = forms.BooleanField(label='Forum Terms of Services', required=True,
                                  error_messages={'required':"Acception is mandatory for membership."})
    

        

    def clean_username(self):
        validate_username(self.cleaned_data['username'])
        try:
            User.objects.get(username=self.cleaned_data['username'])
            raise forms.ValidationError('The username has already been used.')
        except User.DoesNotExist:
            pass
        return self.cleaned_data['username']
    

    def clean_email_rep(self):
        '''Verify whether the repeats are matched.
        Compare iff both of them have passed the default validation(in the cleaned_data)
        Notice that if a field fails to pass the default validation(not in the cleaned_data),
        clean_field will not be invoked.'''

        if 'email' in self.cleaned_data:
            if self.cleaned_data['email'] != self.cleaned_data['email_rep']:
                raise forms.ValidationError('Entered addresses do not match.')
            else:
                try:
                    User.objects.get(email=self.cleaned_data['email'])
                    raise forms.ValidationError('The email address has been used.') 
                except User.DoesNotExist:
                    pass
        return self.cleaned_data['email_rep']

    def clean_password_rep(self):
        if 'password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_rep']:
                raise forms.ValidationError('Entered passwords do not match.')
        return self.cleaned_data['password_rep']
