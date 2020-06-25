from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import ProUser


class UserAccountRegistrationForms(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ProUser
        fields = ("username", 'first_name', 'last_name', 'email', )


class UserAccountProfileForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = ProUser
        fields = ("username", 'first_name', 'last_name', 'email', 'image')
