sudo apt update
sudo apt install python3.5
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install django==2.1
sudo pip3 install gunicorn


sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

PYTHONPATH='pwd'/.. gunicorn --bind 0.0.0.0:8000 ask.wsgi:application

#sudo ln -sf /home/box/web/etc/django_conf.py /etc/gunicorn.d/django_conf.py
#sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c /etc/django_conf.py ask.wsgi:application