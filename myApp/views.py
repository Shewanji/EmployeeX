from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'base.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee/list/') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        # Extract form data from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            # Return error message if passwords don't match
            error_message = "Passwords do not match."
            return render(request, 'signup.html', {'error_message': error_message})

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            # Return error message if username is already taken
            error_message = "Username is already taken. Please choose a different one."
            return render(request, 'signup.html', {'error_message': error_message})

        # Create a new user instance
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        # Log in the new user
        login(request, new_user)

        # Redirect to employee list page
        return redirect('myApp:user_login')
    else:
        # Render the signup form
        return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('myApp:home')  

def employee_list(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees, 10)

    page_number = request.GET.get('page')
    employees_page = paginator.get_page(page_number)

    return render(request, 'employee_list.html', {'employees': employees_page})

def create_employee(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        hire_date = request.POST['hire_date']
        address = request.POST['address']
        department = request.POST['department']
        role = request.POST['role']
        
        if not all([first_name, last_name, email, hire_date, address, department, role]):
            return HttpResponseBadRequest("All fields are required.")

        new_employee = Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            hire_date=hire_date,
            address=address,
            department=department,
            role=role
        )
        new_employee.save()
        return redirect('myApp:employee_list')
        
    elif request.method == "GET":
        return render(request, "create_employee.html")
    else:
        return HttpResponse("An exception occurred! Employee has not been added!")

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        # Handle the form submission and update the employee object
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.email = request.POST['email']
        employee.hire_date = request.POST['hire_date']
        employee.address = request.POST['address']
        employee.department = request.POST['department']
        employee.role = request.POST['role']
        
        # Save the updated employee object
        employee.save()
        
        return redirect('myApp:employee_list')

    # Render the update form with the employee data
    return render(request, 'update_employee.html', {'employee': employee})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('myApp:employee_list')
    else:
        return HttpResponse(status=405)
