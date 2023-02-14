from django import forms

from polls.models import todo


class dateinput(forms.DateInput):
    input_type = 'date'


class todoform(forms.ModelForm):
    date = forms.DateField(widget=dateinput)

    class Meta:
        model = todo
        fields = '__all__'
