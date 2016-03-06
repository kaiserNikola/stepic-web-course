git config --global user.email "kaiserNikola@github.com"                              
git config --global user.name "kaiserNikola"             


sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo apt-get update
sudo apt-get install python3-dev libmysqlclient-dev

sudo pip3 install gunicorn django mysqlclient


mysql -u root -e "create database stepic;"
mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -u root -e "GRANT ALL PRIVILEGES ON box_django.* TO 'box'@'localhost';"

#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart

