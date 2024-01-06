from django import forms

class PracticeForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    value = forms.DecimalField()
    email_address = forms.EmailField(required = False,)
    message = forms.CharField(
	max_length = 10,)
    email_address = forms.EmailField( 
    label="Please enter your email address",)
    first_name = forms.CharField(initial='Your name')
    agree = forms.BooleanField(initial=True)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_color3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)