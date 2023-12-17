from django import forms
from django.core.validators import RegexValidator


class DateTimeForm(forms.Form):
    start_datetime = forms.DateTimeField(
        label='시작 날짜 및 시간 선택',
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    start_datetime_txt = forms.CharField(
        label='시작 날짜 및 시간 초 입력',
        max_length=len('1970-01-01 00:00:00'),
        required=False,
        validators=[
            RegexValidator(
                regex=r'^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d$',
                message='1970-01-01 00:00:00 형식에 맞게 입력하세요.',
                code='invalid_text'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': '1970-01-01 00:00:00'})
    )

    end_datetime = forms.DateTimeField(
        label='종료 날짜 및 시간 선택',
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    end_datetime_txt = forms.CharField(
        label='종료 날짜 및 시간 초 입력',
        max_length=len('1970-01-01 00:00:00'),
        required=False,
        validators=[
            RegexValidator(
                regex=r'^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d$',
                message='1970-01-01 00:00:00 형식에 맞게 입력하세요.',
                code='invalid_text'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': '1970-01-01 00:00:00'})
    )