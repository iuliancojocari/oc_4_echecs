Python 3 needed

# Initialiser le projet

1. Cloner le repository sur votre ordinateur

```shell
$ git clone https://github.com/iuliancojocari/oc_4_echecs.git
```

2. Créer un environnement virtuel python

```shell
$ python -m venv venv
```

3. Activer l'environnement virtuel.
   Sous Windows vous pouvez activer l'environnement virtuel de la manière suivante :

```shell
$ .\venv\Scripts\activate
```

4. Installer les dépendances
   Dans le terminal, naviguez dans le dossier où se trouve le fichier "requirements.txt"
   Pour installer les dépendances Python, éxécutez la commande :

```shell
$ pip install -r requirements.txt

```

# Lancer le programme

Pour lancer le programme, exécutez la commande suivante :

```shell
python -m chess
```

# Générer le rapport flake8

Pour générer un nouveau rapport flake8, éxécutez la commande :

```shell
$ flake8 --format=html --htmldir=flake8_report

```
