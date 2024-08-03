from django import forms # type: ignore
from .models import Category, Task

class CategoryForms(forms.ModelForm):
    
    class Meta:
        model = Category
        exclude = ('owner',)

class TaskForm(forms.ModelForm):
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        exclude = ('owner',)