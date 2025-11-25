from django import forms
from .models import Student


class UserFormFields(forms.Form):
    last_name = forms.CharField(
        max_length=100,
        label="Фамилия",
        widget=forms.TextInput(attrs={'placeholder': 'Иванов'})
    )
    first_name = forms.CharField(
        max_length=100,
        label="Имя",
        widget=forms.TextInput(attrs={'placeholder': 'Иван'})
    )
    middle_name = forms.CharField(
        max_length=100,
        label="Отчество",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Иванович'})
    )
    age = forms.IntegerField(
        label="Возраст",
        min_value=16,
        max_value=100
    )
    group = forms.ChoiceField(
        choices=[('101', '101'), ('102', '102'), ('103', '103')],
        label="Группа"
    )
    email = forms.EmailField(label="E-mail")
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    programming_language = forms.ChoiceField(
        choices=[
            ('python', 'Python'),
            ('java', 'Java'),
            ('cpp', 'C++'),
            ('js', 'JavaScript'),
        ],
        label="Язык программирования"
    )


class UserFormData(forms.ModelForm):
    email = forms.EmailField(label="E-mail", required=True)
    programming_language = forms.ChoiceField(
        choices=[
            ('python', 'Python'),
            ('java', 'Java'),
            ('cpp', 'C++'),
            ('js', 'JavaScript'),
        ],
        label="Язык программирования",
        required=False
    )

    class Meta:
        model = Student
        fields = ['last_name', 'first_name', 'middle_name', 'birth_year', 'group_number']
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'middle_name': 'Отчество',
            'birth_year': 'Год рождения',
            'group_number': 'Номер группы',
        }
        widgets = {
            'birth_year': forms.NumberInput(attrs={'placeholder': '2000'}),
            'group_number': forms.TextInput(attrs={'placeholder': '101'}),
        }

    def clean_birth_year(self):
        year = self.cleaned_data['birth_year']
        if not (1900 <= year <= 2100):
            raise forms.ValidationError("Год должен быть от 1900 до 2100.")
        return year

    def clean_email(self):
        email = self.cleaned_data['email']
        if "@" not in email or "." not in email.split("@")[-1]:
            raise forms.ValidationError("Введите корректный e-mail.")
        return email