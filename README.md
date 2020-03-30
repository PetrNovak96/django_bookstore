```
mkdir books
pipenv install django==2.2.7 psycopg2-binary==2.8.4
pipenv shell
django-admin startprojectt bookstore_project .
django-admin startproject bookstore_project .
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py startapp users
sudo docker-compose down
ls
sudo rm -r users
python manage.py startapp users
python manage.py makemigrations users
sudo docker-compose up -d --build
sudo docker-compose web python manage.py makemigrations users
sudo docker-compose exec web python manage.py makemigrations users
docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py test
git init
git status
git add .
git commit -m 'initial commit'
python manage.py startapp pages
git add .
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py test
def setUp(self):
url = reverse('home')
self.response = self.client.get(url)
def test_homepage_status_code(self):
self.assertEqual(self.response.status_code, 200)
def test_homepage_template(self):
self.assertTemplateUsed(self.response, 'home.html')
def test_homepage_contains_correct_html(self):
self.assertContains(self.response, 'Homepage')
def test_homepage_does_not_contain_incorrect_html(self):
self.assertNotContains(
sudo docker-compose exec web python manage.py test pages
clear
git status
git add .
git commit -m 'testy a pages'
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py test
sudo docker-compose exec web python manage.py test users
git add .
git commit -m 'sign up, login'
mkdir static
clear~
mkdir static/css
mkdir static/js
mkdir static/images
touch static/css/base.css
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py collectstatic
sudo rm -r staticfiles
python manage.py collectstatic
pipenv install django-crispy-forms==1.8.0
sudo docker-compose down
sudo docker-compose up -d --build
python manage.py test
sudo docker-compose exec web python manage.py test
git add .
git commit -m "s bootstrapem"
clear
pipenv install django-allauth==0.40.0
sudo docker-compose down
sudo docker-compose up -d --build
python manage.py migrate
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py test
git add .
git commit -m 'allauth'
sudo apt-get install libpq-dev python-dev
pip install psycopg2
sudo pip install psycopg2
sudo apt-get install libpq-dev python-dev
sudo apt-get install libpq-dev python3-dev
sudo pip3 install psycopg2
cd /etc
ls
cd sou*
cd apt
ls
cd sou*d
ls
sudo rm sstp
sudo rm *sstp*
exit
sudo apt --fix-broken install
sudo apt autoremove
clear
sudo docker-compose exec web python manage.py makemigrations books
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py test
git add .
git commit -m 'reviews'
sudo docker-compose exec web pipenv install pillow==6.2.1
pipenv install pillow==6.2.1
sudo docker-compose down
sudo docker-compose up -d --build
mkdir media
mkdir media/covers
sudo docker-compose exec web python manage.py makemigrations books
sudo docker-compose exec web python manage.py migrate
git add .
git commit -m "media"
clear
sudo docker-compose exec web python manage.py makemigrations books
sudo docker-compose exec web python manage.py migrate
sudo docker-compose down
sudo docker-compose up --build -d
sudo docker-compose exec web python manage.py test
git commit -m "permissions"
git add .
git commit -m "permissions"
clear
python3 manage.py startapp orders
clear
sudo docker-compose down
sudo docker-compose up -d 
pipenv install stripe==2.32.0
sudo docker-compose down
sudo docker-compose up -d --build
sudo docker-compose down
sudo docker-compose up -d --build
sudo docker-compose up
sudo docker-compose down
sudo docker-compose up -d --build
git add .
git commit -m "orders app"
git add .
git commit -m "základní search"
clear
pipenv install django-debug-toolbar==2.0
clear
sudo docker-compose down
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py makemigrations books
sudo docker-compose exec web python manage.py migrate
clear
git add .
git commit -m "základní caching a index"
sudo docker-compose exec web python manage.py check --deploy
touch docker-compose-prod.yml
sudo docker-compose down
sudo docker-compose -f docker-compose-prod.yml up -d --build
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py check --deploy
sudo docker-compose down
sudo docker-compose -f docker-compose-prod.yml up -d
sudo docker-compose exec web python manage.py check --deploy
sudo docker-compose down
sudo docker-compose -f docker-compose-prod.yml up -d
sudo docker-compose exec web python manage.py check --deploy
sudo docker-compose down
sudo docker-compose -f docker-compose-prod.yml up -d
sudo docker-compose exec web python manage.py check --deploy
sudo docker-compose down
sudo docker-compose -f docker-compose-prod.yml up -d
sudo docker-compose exec web python manage.py check --deploy
clear
sudo docker-compose down
sudo docker-compose -f docker-compose.yml up -d
sudo docker-compose exec web python manage.py check --deploy
clear
sudo docker-compose down
sudo docker-compose docker-compose.yml up -d --build
sudo docker-compose up -d --build
sudo docker-compose up
git add .
clear
git commit -m "security veci"
cat ~/bash_hist* > README.md
cat ~/.bash_hist* > README.md
exit
pipenv shell
exit
```