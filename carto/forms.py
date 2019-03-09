from django import forms


class ContactForm(forms.Form):
    email_widget = forms.EmailInput(attrs={'class': 'form-control',
                                           'placeholder': "Votre e-mail"})
    email = forms.EmailField(label='Votre e-mail',
                             max_length=150,
                             widget=email_widget)
    message_widget = forms.Textarea(attrs={'class': 'form-control',
                                           'placeholder': "Votre message",
                                           'rows': '5'})
    message = forms.CharField(label='Votre message',
                              strip=True,
                              widget=message_widget)
                              