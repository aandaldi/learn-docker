from flask import Flask, flash, render_template, request, redirect
import mysql.connector
import sys
sys.stdout.flush()
app = Flask(__name__)

#mysql connect
def getMysqlConnection():
    return mysql.connector.connect(
        user='root', 
        host='db', 
        port='3306', 
        password='root', 
        database='test_crud'
    )

@app.route('/')
def home():
	try:
		db = getMysqlConnection()
		cursor = db.cursor()
		sqlstr = "SELECT * from tbl_user"
		print(sqlstr)
		cursor.execute(sqlstr)
		output_json = cursor.fetchall()
		print(output_json, flush=True)
		return render_template('home.html', datas=output_json)
	except Exception as e:
		print("Error in SQL:\n", e, flush=True)
		return render_template('home.html')
	finally:
		cursor.close() 
		db.close()


@app.route('/add', methods=['POST'])
def add_user():
	try:
		db = getMysqlConnection()
		cursor = db.cursor()
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']		
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _password,)
			cursor.execute(sql, data)
			db.commit()
			flash('User added successfully!')
			print("berhasil add", flush=True)
			return render_template('home.html')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
		return render_template('home.html')
	finally:
		cursor.close() 
		db.close()

@app.route('/edit/<int:id>')
def edit_view(id):
	try:
		db = getMysqlConnection()
		cursor = db.cursor()
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		db.close()


@app.route('/update', methods=['POST'])
def update_user():
	try:
		db = getMysqlConnection()
		cursor = db.cursor()		
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		_id = request.form['id']
		# validate the received values
		if _name and _email and _password and _id and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (_name, _email, _hashed_password, _id,)
			cursor.execute(sql, data)
			db.commit()
			flash('User updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		db.close()

@app.route('/delete/<int:id>')
def delete_user(id):
	try:
		db = getMysqlConnection()
		cursor = db.cursor()
		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
		db.commit()
		flash('User deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		db.close()


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')