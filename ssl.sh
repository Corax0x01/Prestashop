
#!/bin/bash

sudo docker exec prestashop-prestashop-1 chmod +x /docker/ssl.sh
sudo docker exec prestashop-prestashop-1 /docker/ssl.sh
