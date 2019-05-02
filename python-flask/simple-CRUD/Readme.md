# Learn Docker Compose

##### run runtest.py to test on your local without docker-compose
##### on this folder, you can see just home.html, but this app can run on postman(backend)

1. Install Docker Compose
    ~~~
    sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

    ~~~
2. Create Apps.py and requirement.txt
3. Create dockerfile
4. Create Docker Compose.
   example:
    
    ~~~
    version: "2"
    services:
      app:                      #this your service apps name
        build: .                #dockerfile location
        depends_on:             #for depends service
          - db
        ports:
          - "5000:5000"
    
      db:
        image: mysql:5.7
        container_name: db
        restart: always
        ports:
          - "32000:3306"
        environment: 
          MYSQL_ROOT_PASSWORD: root
          MYSQL_PASSWORD: root
          MYSQL_USER: root
          MYSQL_ROOT_HOST: 0.0.0.0
        volumes:
          - db_data:/var/lib/mysql
    volumes: 
      db_data:
    ~~~  
   
4. On your apps service, for connect to database in other container, using
    ~~~
    def getMysqlConnection():
        return mysql.connector.connect(
            user='root', 
            host='db',      # this is depends on(source: docker-compose) 
            port='3306', 
            password='root', 
            database='test_crud'
    )
    ~~~
5. Run Docker Compose
    ``` docker-compose up```

    for rebuild docker-compose, using
    ``` docker-compose up -d --force-recreate --build```
    don't forget to grant all previlage to user.
~~~ SELECT User,authentication_string FROM mysql.user;
GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY PASSWORD '*81F5E21E35407D884A6CD4A731AEBFB6AF209E1B';~~~