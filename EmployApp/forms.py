from django import forms

# form that allows on to submit employee application information
class employeeApply(forms.Form):
    name = forms.CharField()
    date_of_birth = forms.DateField()
    position_applying_to = forms.CharField()
    desired_salary = forms.DecimalField(decimal_places=2)
