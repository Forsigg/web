sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/django_conf.py /etc/gunicorn.d/django_conf.py
sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /etc/gunicorn.d/django_conf.py ask.wsgi:application