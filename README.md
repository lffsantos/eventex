# EVENTEX


Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/lffsantos/eventex.svg?branch=master)](https://travis-ci.org/lffsantos/eventex)
[![Code Health](https://landscape.io/github/lffsantos/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/lffsantos/eventex/master)


## Como desenvolver?

1. clone o respositório.
2. crie um virtualenvo com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância .env
6. Execute os testes.

```console
git clone git@github.com:henriquebastos/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?

1. crie uma instância no heroku
2. Envie as configurações parao heroku
3. Defina uma secret key para a instância
4. Defina o DEBUG=False
5. configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia  
heroku config:push  
heroku config:set SECRET_KEY= python contrib/secret_gen.py  
heroku config:set DEBUG=False  
#configuro o email  
git push heroku master --force  
```