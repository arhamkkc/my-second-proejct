from django import forms
from blog.models import Photo,Contact,Category


# for uplaod content from frontend
class PhotoForm(forms.ModelForm):
    class Meta():
        model = Photo
        fields = '__all__'


# contact form 
class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'

        widgets = {
            'Full_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Contact_No':forms.TextInput(attrs={'class':'form-control'}),
            'purpose':forms.Select(attrs={'class':'form-control'}),
            'requirements':forms.Textarea(attrs={'class':'form-control'}),
        }

# for adding category from the frontend 
class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ['category_name','category_image']