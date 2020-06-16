from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from account.models import ProUser


class UserAccountRegistrationForms(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ("username", 'first_name', 'last_name', 'email', )

    def clean_email(self):
        email = self.cleaned_data['email']
        filt_stud_qs = ProUser.objects.all().filter(email=email)

        if len(filt_stud_qs) > 0 and not filt_stud_qs[0].id == self.instance.id:
            raise ValidationError("This e-mail exists")

        return email


class UserAccountProfileForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        fields = ("username", 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        filt_stud_qs = ProUser.objects.all().filter(email=email)

        if len(filt_stud_qs) > 0 and not filt_stud_qs[0].id == self.instance.id:
            raise ValidationError("This e-mail exists")
        return email
