from django import forms


#Building a search view
class  SearchForm(forms.Form):
    query =forms.CharField()