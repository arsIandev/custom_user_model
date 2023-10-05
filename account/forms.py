from django.contrib.auth.forms import (UserCreationForm as DJUserCreationForm,
                                       UserChangeForm as DjChangeForm)
from django.contrib.auth import get_user_model


class UserCreationForm(DJUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('name', 'email',)


class UserChangeForm(DjChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)
