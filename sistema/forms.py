from django import forms


class RelatorioForm(forms.Form):
    
    patrimonio = forms.CharField(max_length=4)
    estado = forms.CharField(max_length=16)
    nome = forms.CharField(max_length=128)
    serie = forms.CharField(max_length=64)
    marca = forms.CharField(max_length=32)
    setor = forms.CharField(max_length=32)
    data_saida = forms.DateField()
    data_retorno = forms.DateField()
    descricao = forms.CharField(widget=forms.Textarea)

    def clean(self):
        dados = super().clean()
        
        patrimonio = dados.get('patrimonio')
        estado = dados.get('estado')
        return dados