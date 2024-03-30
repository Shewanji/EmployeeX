Employee Management System
__________________________________________________________________________________________________________________________________________________________________________________

The Employee Management System is a simple Django-based web application that allows users to manage employees' data within a company. It provides the CRUD functionalities to add, delete, update, and view employees information through a user-friendly interface. The system also implements user authentication including signup, login, and logout  functionalities to ensure secure access to the website.

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Installation:
______________________________________________

To run the Employee Management System locally, follow these steps:

1. Clone the repository:

   git clone https://github.com/Shewanji/EmployeeX.git

2. Change into the project directory:

    cd EmployeeX

3. Create a virtual environment and activate it:

    python3 -m venv myenv

    source myenv/bin/activate

4. Install the required dependencies:

    pip install -r requirements.txt

5. Set up the database:

    python manage.py makemigrations

    python manage.py migrate

6. Run the development server:

    python manage.py runserver

7. Open your web browser and visit http://localhost:8000 to access the Employee Management System.
  
   


