from django import forms
from .models import Candidate
from .models import Jedi
from .models import Answer
class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'planet', 'age', 'email')
        labels = {
            'name':'Ваше имя',
            'planet':'Планета',
            'age':'Возраст',
            'email':'E-mail'
        }

class JediForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Jedi.objects.all())


class TestTaskForm(forms.Form):
    #question = forms.CharField(max_length=100, label="")
    CHOICES = (
        ('Y', 'Да'),
        ('N', 'Нет'),
    )
    answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label ="")