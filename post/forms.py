from django import forms


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)
    rating = forms.ChoiceField(label="Rating", choices=[(i, str(i)) for i in range(1, 6)], required=False)