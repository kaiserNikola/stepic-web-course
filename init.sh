git config --global user.email "kaiserNikola@noreply.github.com"                              
git config --global user.name "kaiserNikola"             


sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo apt-get update && sudo apt-get upgrade --yes
sudo apt-get install lynx python3-dev libmysqlclient-dev --yes
sudo pip3 install gunicorn django mysqlclient

sudo service mysql restart

mysql -u root -e "create database stepic;" # CHARACTER SET utf8 COLLATE utf8_general_ci;"
#mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
#mysql -u root -e "GRANT ALL PRIVILEGES ON box_django.* TO 'box'@'localhost';"
#mysql -u root -e "SET NAMES UTF8;"

#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart


sudo rm /usr/bin/python
sudo ln /usr/bin/python3 /usr/bin/python
sudo rm /usr/bin/python2                                 
sudo ln -s /usr/bin/python3 /usr/bin/python2             
sudo rm /usr/bin/python2.7                               
sudo ln -s /usr/bin/python3 /usr/bin/python2.7 



