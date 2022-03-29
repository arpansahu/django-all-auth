from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm
from django import forms
from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        # For a single Column
        # self.fields['email'].widget.attrs.update({
        #     'class': 'form-control'
        # })

    def signup(self, request, user):
        user.save()
        return user


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class CustomResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })
        self.fields["email"].label = ""


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)


CustomResetPasswordForm
