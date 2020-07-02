from django import forms


class UserAnswer(forms.Form):
    answer = forms.CharField(label="your answer here",
                             initial="Your Answer Here", required=True)
