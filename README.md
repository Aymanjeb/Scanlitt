# Scanlitt
Django code of the mini-test:

User's Guide:

Extracting Files from the Downloaded Project: The downloaded project is probably in a compressed format, such as a .zip or .tar.gz file. You will need to extract the files from the archive into a directory on your computer.
1.	Install Python and Django: If you have not already done so, you need to install Python and Django on your computer. Python can be downloaded from the official website (https://www.python.org/downloads/), and Django can be installed using pip (the Python package manager). To install Django, open a command prompt or terminal window and run the pip install django command.
2.	Navigate to the project directory: Open a command prompt or terminal window and navigate to the directory where you extracted the project files. This directory should contain a file named manage.py.
4- Run the python command manage.py makemigrations
3.	Execute the migrate command by running the python command manage.py migrate
4.	Run the createsuperuser command by running the python manage.py createsuperuser command. This command prompts you to enter a username, email (optional) and password for the new superuser. Enter the required information and press Enter after each prompt.
5.	Start the development server: you can start the development server by running the python manage.py runserver command. This command starts the development server and displays the URL that you can use to access the site in your web browser (usually http://localhost:8000/).
6.	Access the site in your web browser: Open your web browser and enter the URL displayed by the development server (usually http://localhost:8000/) in the address bar. You should see the Django project login page "scanlitt_project". Enter the superuser information and log in.

