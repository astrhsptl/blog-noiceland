from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError

User = get_user_model()

class UpdateUserForm(UserChangeForm):
    username = forms.CharField(max_length=30, label='NickName', required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'NickName', 'class': 'text-field__input'}))
    name = forms.CharField(max_length=30, label='First Name',required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'text-field__input'}))
    lastname = forms.CharField(max_length=30, label='First Name',required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Lastname', 'class': 'text-field__input'}))
    email = forms.CharField(max_length=30, label='First Name',required=False,
                           widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'text-field__input'}))
    status = forms.CharField(max_length=30, label='About you',required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'About you', 'class': 'text-field__input'}))
    avatar = forms.ImageField()

    def clean_username(self):
        print('wtf?')
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            raise ValidationError('Username alrady taken')
        except:
            return username
        
    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        print(data)
        return data

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('name', 'lastname', 'username', 'email', 'avatar', 'status', 'background')

class CustomSignupForm(UserCreationForm):
    email = forms.CharField(max_length=30, label='First Name',required=False,
                           widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'text-field__input'}))
    username = forms.CharField(max_length=30, label='NickName', required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'NickName', 'class': 'text-field__input'}))
    name = forms.CharField(max_length=30, label='First Name',required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'text-field__input'}))
    lastname = forms.CharField(max_length=30, label='First Name',required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Lastname', 'class': 'text-field__input'}))
    status = forms.CharField(max_length=30, label='About you',required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'About you', 'class': 'text-field__input'}))
    avatar = forms.ImageField()    
    background = forms.ImageField()    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'text-field__input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation', 'class': 'text-field__input'}))


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'lastname', 'username', 'email', 'status', 'avatar', 'background',)


# class CustomSignupForm(SignupForm):
#     name = forms.CharField(max_length=30, label='First Name',
#                            widget=forms.TextInput(attrs={'placeholder': 'Name'}))
#     lastname = forms.CharField(max_length=30, label='Last Name',
#                                widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
#     status = forms.CharField(max_length=256,
#                              widget=forms.TextInput(attrs={'placeholder': 'Status'}))
#     avatar = forms.ImageField()
#     background = forms.ImageField()

#     # def signup(self, request, user):
#     #     user.name = self.cleaned_data['name']
#     #     user.lastname = self.cleaned_data['lastname']
#     #     user.status = self.cleaned_data['status']
#     #     print(request['FILES'])
#     #     # user.avatar = request['FILES']
#     #     user.background = self.avatar
#     #     print(self.avatar)
#     #     user.save()
#     #     return user