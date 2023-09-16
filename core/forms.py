from django import forms
from django.core.mail.message import EmailMessage
from .models import Cliente
from .models import Produto



class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assuntos', max_length=150)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Nome: {nome}\n E-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage (
        subject='Equipe Clã do Tarot',
        body=conteudo,
        from_email='Samaedo666@gamil.com',
        to=[email],
        headers={'reply_to':'Samaedo666@gamil.com'}
        )
        mail.send()


class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'})
        }
    
    def sendmail(self):
        nome_completo = self.cleaned_data['nome_completo']
        email = self.cleaned_data['email']  # Adicione essa linha para obter o email
        
        conteudo = 'Muito grato por sua mensagem'

        mail = EmailMessage (
            subject='Equipe Clã do Tarot',
            body=conteudo,
            from_email='Samaedo666@gmail.com',  # Corrija o endereço de e-mail
            to=[email],  # Use o endereço de e-mail do cliente
            headers={'reply_to':'Samaedo666@gmail.com'}  # Corrija o endereço de e-mail
        )
        mail.send()



class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto

        fields = '__all__'