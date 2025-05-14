Instruction on how to run Django Project on your local computer:

Requirements:
Python
Text Editor
Terminal
Pip

Virtualenv (pip intall virtualenv)
*Creating a virtual environment is now necessary

Steps:

1. Go to your terminal (I used command prompt)

2. cd src of the project 
	example: cd C:\Users\adamn\Downloads\Capstone\src

3. python -m venv venv (not required)
	windows: venv\Scripts\activate
	macOS/Linux: source venv/bin/activate

4. pip install -r requirements.txt

5. python manage.py makemigrations

6. python manage.py migrate

7. python manage.py runserver

8. Type http://http://127.0.0.1:8000/ in your web browser

9. To stop server ctrl + c in the terminal


Additional Info:

To get to admin go to http://127.0.0.1:8000/admin

admin login:
email: adam@adam.com
password: johnson

