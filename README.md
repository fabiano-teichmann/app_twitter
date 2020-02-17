# Monitoramento Twitter
# Monitoramento Twitter

Para dar deploy na aplicação é necessário ter python3 e siga os seguintes procedimentos.

1. Baixe o repositório com o comando 

    git clone https://github.com/fabiano-teichmann/app_twitter.git
    
2. Entre no diretório do projeto e crie o virtualenv com o comando  

    python3 -m venv venv
    
3. Logo depois disto ative o virtualenv e instale as bibliotecas requiridas com o comando

    source venv/bin/activate && pip install -r requirements.txt


4. Crie o arquivo settings.ini com as credenciais para a api Twitter na raíz do seu projeto com as credenciais de seu projeto


	[settings]
	# settings django
	debug=False
	secret_key=digite aqui sua key
	# access Twitter
	consumer_key= digite aqui seu consumer key
	consumer_secret= digite aqui seu consumer_secret
	access_token_key= digite aqui access_token_key
	access_token_secret=  digite aquiaccess_token_secret
	secret_key= digite aqui  access_token_secret

    
    
4. Aplique o migrate do django entrando na pasta

      
      python manage.py migrate
   
5. Crie o usuário admin

    
    python manage.py createsuperuser
    

     
6. Aponte para seu diretório do seu projeto o arquivo de configuração wgsgi do Python Anywhere

7. Coloque em settings.py na variável ALLOWED_HOST o seu domínio no Python Anywhere