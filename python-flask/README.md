
![](https://kenya-tech.com/wp-content/uploads/2019/01/flask-python.png)

# Create Simple flask apps with docker
1. install flask package on your python environment
2. create python file and import flask.
3. create requirements.txt  => memuat semua file yang ingin di instal di aplikasi
4. create docker file

    ~~~
    FROM python:3.7-alpine         
    # RUN apt-get update -y
    # RUN apt-get install -y python-pip python-dev build-essential
    COPY . /app 
    WORKDIR /app
    RUN pip install -r requirements.txt
    #ENTRYPOINT ["python"]
    CMD ["python","app.py"]             #cmd menjalankan file yang dengan cli python dan file yang ingin di jalankan
    ~~~

5. build docker image
    ~ docker build -t simple-flask . ~

6. run docker image 
    `docker run -d -p 5021:5000 --rm --name simple-flask-1 simple-flask` 