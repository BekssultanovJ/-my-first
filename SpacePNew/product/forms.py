from django import forms

from product.models import Category, Product, ProductImage


class ProductForm(forms.Form):
    def init(self, *args, **kwargs):
        super(ProductForm, self).init()

    name = forms.CharField(max_length=50)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    def save(self):
        data = self.cleanned_data
        product = Product.objects.create(**data)
        return product


class ProductForm(forms.ModelForm):
    # TODO: загрузка изображений
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']