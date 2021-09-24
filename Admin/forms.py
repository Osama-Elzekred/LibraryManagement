from django import forms
from Books.models import Author

class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)