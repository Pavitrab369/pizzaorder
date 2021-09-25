from django import forms
from .models import Pizza,Size
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label="Topping 1",max_length=100)
#     topping2 = forms.CharField(label="Topping 2",max_length=100)
#     # toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olives','Olives')],widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label="Size", choices=[('small',"Small"),('medium','Medium'),('large','Large')])

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {'topping1': "Topping 1",'topping2': "Topping 2"}
        # widgets = {
        #     'topping1': forms.RadioSelect(choices=[('mozzarella','Mozzarella'),('cheddar','Cheddar'),('parmesan','Parmesan')]),
        #     'topping2': forms.RadioSelect(choices=[('cap','Capsicum'),('tomato','Tomato'),('pep','peperoni'),('olives','Olives')])
        #     }

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
