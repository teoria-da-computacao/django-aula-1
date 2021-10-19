# Aplicações Web desenvolvidas na aula

### Passos para lançar e editar a aplicação
1. Abra a linha de comandos (PowerShell ou cmd)
1. Descarregue uma cópia (clone) do repositório com o comando `git clonehttps://github.com/teoria-da-computacao/aula-1` ou descarregue o projeto como um zip e descompacte
1. Entre na pasta  `cd aula-1`
2. Crie e instale um ambiente virtual. Use o pipenv.
    1. Instale o pipenv `python -m pip install pipenv`
    1. Crie um ambiente virtual com o django instalado `pipenv install django`
    1. Active o ambiente virtual `pipenv shell`
5. Lance a aplicação no browser com o comando `python manage.py runserver`
6. abra a pasta com o Pycharm, ou com o comando `pycharm .`

### Passos para criar uma nóva página na aplicação
1. no ficheiro `views.py` crie uma nova função que renderize a nova página
2. na pasta `website\templates\website` crie uma página HTML correspondente para ser renderizada, extendendo o layout base (veja como é feito nas outras páginas)
3. no ficheiro `website\urls.py` crie um novo `path` para o novo URL
4. no ficheiro `layout.html` (que está na pasta `website\templates\website`) atualize o menu de navegação, inlcuindo um link para a nova página

