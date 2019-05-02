# learn-docker
### Docker

### Perintah Dasar Docker
1. ```docker images```              untuk melihat seluruh images
2. ```docker search <images>```     untuk melihat seluruh images
3. ```docker ps```                  untuk melihat container yang aktif
4. ```docker ps -a```               untuk melihat seluruh container
5. ```docker run -d –name <nama_container> <parameter_tambahan> <nama_image>:<tag>``` Menjalankan container dengan image yang sudah di download
6. ```docker exec -it <nama_container> /bin/sh``` Masuk ke dalam container yang sedang berjalan
7. ```docker rm <nama_container>``` menghapus container
8. ```docker rmi <image_id>```  menghapus image


### Simple Docker Example to 
```docker run -dit -p 122:22 -p 180:80 --rm --name portalweb --hostname portalweb nama_image ```  contoh
```--rm ``` untuk menghapus container setelah container di stop

### UPLOAD DOCKER
```docker login```
```docker images```
```docker push aandaldi/nama_image```

### DOCKER COMPOSE
1. ``` docker-compose up```         untuk running docker compose
2. ``` docker-compose up -d --force-recreate --build``` untuk rebuild docker compose



