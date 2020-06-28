from django import forms


class UserDetails(forms.Form):
    college = forms.CharField(max_length=400)
    year = forms.IntegerField(min_value=1, max_value=4)
    contact = forms.CharField(min_length=10, max_length=10, required="False")
