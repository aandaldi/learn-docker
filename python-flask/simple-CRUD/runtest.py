from flask import Flask, render_template
import pymysql
app = Flask(__name__)


# mysql connect
connection = pymysql.connect(
    host='127.0.0.1',
    user='local',
    password='local',
    db='simple_crud'
)

#input

# title = input("Enter title of your task: ")
# desc = input("Add some description to it: ")
# date = input("Enter the date for this task (YYYY-MM-DD): ")



# try:
#     with connection.cursor() as cursor:
#         sql = "INSERT INTO todos (`title`, `desc`, `date`) VALUES (%s, %s, %s)"
#         try:
#             cursor.execute(sql, (title, desc, date))
#             print("Task added successfully")
#         except:
#             print("Oops! Something wrong")
 
#     connection.commit()
# finally:
#     connection.close()

@app.route('/', methods=['GET'])
def home():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from todos"
            try:
                cursor.execute(sql)
                data = cursor.fetchall()
                print(data)
            except:
                print("Oops! Something wrong")
    
        connection.commit()
    finally:
        print('a')
        # connection.close()

    return render_template('home.html', datas=data)

if __name__ == '__main__':
    app.run()