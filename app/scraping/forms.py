from django import forms
from .models import FaceBook_Data_Login

class FaceBookForm(forms.ModelForm):
    class Meta:
        model=FaceBook_Data_Login
        # fields = "__all__"
        # fields = {'facebook_password','facebook_email',}
        fields = ['facebook_email','facebook_password',]
        