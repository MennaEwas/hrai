# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User

# # class RegisterForm(UserCreationForm):
# #     email = forms.EmailField()
# #     #saved in the database 
# #     class Meta:
# #         model = User
# #         fields = ["username", "email", "password1", "password2"]
        
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=200)
#     password = forms.CharField(widget=forms.PasswordInput)

# class UserRegisterationForm(forms.ModelForm):
#     password = forms.CharField(label="Password", 
#                                 widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Repeat Password", 
#                                 widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ["username", "firstname", "email"]

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('passwords don\'t match.')
#         return cd['password2']

