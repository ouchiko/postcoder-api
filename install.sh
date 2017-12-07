cd front/app/datasrc && tar -zxvf opennames.tar.gz
docker-compose down
docker-compose build front
docker-compose -d up
