# bibliophile

[![test_bibliophile](https://github.com/edelwi/bibliophile/actions/workflows/main.yml/badge.svg)](https://github.com/edelwi/bibliophile/actions/workflows/main.yml)

[MIT License](LICENSE.txt)

This is a simple django application for storing information about books in a home library.

The main reason for creating this app was to restore my django skills.

## How to install and run (to play with django internal server)

Required python >= 3.8

```shell
git clone https://github.com/edelwi/bibliophile.git
cd bibliophile
python3  -m venv venv
source ./venv/bin/activate  # activate virtual environment (on linux) on Windows run venv\Scripts\activate.bat
pip install -r requirements.txt
cd project/
python manage.py migrate
python manage.py compilemessages  # optional (russian language support)
python manage.py createsuperuser  # and set up superuser login and password
python manage.py loaddata fixtures/init_data_clean.json  # optional (demo data, not much)
DEBUG=True python manage.py runserver  # run on http://127.0.0.1:8000/
```
