from django import forms

from .models import Order


class RegistrationForm(forms.ModelForm):
    # CHOICES = Order.state
    """CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    """
    full_name = forms.CharField(
        label='Nome Completo', min_length=4, max_length=100)
    address_1 = forms.CharField(max_length=300, error_messages={
        'Obrigatório': 'Necessário indicar um endereço'}, label="Endereço 1")
    address_2 = forms.CharField(
        max_length=300, label="Endereço 2", required=False)
    postal_code = forms.CharField(
        max_length=12, label='CEP')

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        if not name or len(name) < 4:
            raise forms.ValidationError(
                'Nome precisa ter 4 ou mais caracteres')
        elif isinstance(name, int):
            raise forms.ValidationError(
                'Deve conter letras')
        return name

    def clean_address_1(self):
        address = self.cleaned_data['address_1']
        if not address or len(address) < 4:
            raise forms.ValidationError(
                'Informe um enderço válido')
        return address
   # state = forms.ChoiceField(widget=forms.Select(choices=CHOICES))
    # state = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Order
        fields = ('full_name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Nome Completo (Obrigatório)', 'name': 'fullname', 'id': 'custName'})
        self.fields['address_1'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Endereço 1 (Obrigatório)', 'name': 'address1', 'id': 'custAdd'})
        self.fields['address_2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Endereço 2 (Opcional)', 'name': 'address2', 'id': 'custAdd2'})
        self.fields['postal_code'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'CEP (Obrigatório)', 'name': 'postalcode', 'id': 'PostalCode'})
