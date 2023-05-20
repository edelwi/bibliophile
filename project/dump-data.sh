#!/bib/sh
#python manage.py dumpdata --exclude=auth --exclude=contenttypes --indent 4 -o init_data.json
python manage.py dumpdata --natural-foreign --natural-primary --exclude=auth --exclude=contenttypes --indent 4 -o init_data_2.json