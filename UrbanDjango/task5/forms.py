from django import forms
from django.core.exceptions import ValidationError



class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин: ',
                               error_messages={'required': 'Повторите попытку.'})
    password = forms.CharField(min_length=8, label=' Введите пароль: ',
                               error_messages={'required': 'Повторите попытку.'},
                               widget=forms.PasswordInput())
    repeat_password = forms.CharField(min_length=8, label=' Повторите пароль: ',
                               error_messages={'required': 'Повторите попытку.'},
                               widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=0, label='Введите свой возраст:',
                              error_messages={'required': 'Вы должны быть старше 18.', })

    def clean_username(self):
        users = ['Vasya', 'Petya', 'Anna']
        username = self.cleaned_data.get('username')
        if username in users:
            raise ValidationError(f'Пользователь {username} уже зарегестрирован.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if password != repeat_password:
            raise ValidationError('Пароли не совпадают.')
        return password

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if len(str(age)) > 3:
            raise ValidationError('Введите не более 3 символов')
        elif int(age) < 18:
            raise ValidationError('Вы должны быть старше 18')
        return age

