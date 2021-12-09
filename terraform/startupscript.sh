#! /bin/bash
sudo apt-get update 
sudo apt-get -y install apache2 
sudo apt-get restart apache2
sudo gsutil cp gs://BUCKETNAME/copyindex.sh /copyindex.sh 
chmod 755 /copyindex.sh
sudo crontab -u root -l | { cat; echo "2 * * * * sudo /copyindex.sh"; } | sudo crontab -u root -