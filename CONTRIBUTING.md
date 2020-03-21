# Contribuer au dossier

### Comment faire pour contribuer
- Pour les personnes connaissant git, les contributions se font par pull request
-  Si vous ne connaissez pas git, (les personnes en licence math par exemple):
je vous invite à envoyer le code source de votre contribution par mail à souffan.nathan@gmail.com et celle ci sera ensuite intégrer

### De quelle manière

#### Correction d'exercices
Les corrections d'exercices se font en latex dans les dossiers *src* du TD approprié avec le fichier pdf de sortie dans le dossier *target* \
Pour éviter d'avoir des fichiers sources trop long, vous pouvez écrire la correction de l'exercice *X* du TD *Y*  directement dans un fichier `exoX.tex` ayant comme seul en tête, (tout les en-têtes nécessaires seront placés dans le fichier `tdY.tex`) `\documentclass[tdY.tex]{subfiles}`, il suffira ensuite d'ajouter `subfile{exoX.tex}` dans le fichier `tdY.tex`.

#### Reporter une erreur
Si vous voyez une correction incorrecte ou incomplète, nous vous invitions à créer une [issue](https://github.com/nsouff/DL-maths-info/issues), ou si vous n'avez pas de compte github envoyer un mail
