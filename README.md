# Utibucare
This is an app that allows patients to order medicine online and gets delivered on their preference location

## Author
Pauline Wafula

# Description
Utibucare  is a web application that mimics a ecommerce apps , Awwards.This application allows a user to order drugs online and chose the method to be delivered.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

Create an account and log in
View the services offered 
Able to order medicine of preference from the app
Be able to view my ordered medicine from the cart
Able to checkout my medicine, reduce the quantity
Get a notification if its to be delivered or i make the payments

Behaviour|	Input |	Output|
Display login form or sign up incase you dont have an account |	clicking the get started button |	Displays the registration form on clicking sign up
Displays services offered	On log in  | Button redirects you to order medicine | redirected to the medicine page.
Click add to cart to add medicine | 	medicine will be added to cart | click checkout
Redirects you to details of shipping address | add required details in case of shipping| redirect to make payment
## SetUp / Installation Requirements
Prerequisites
python
pip
activate virtual environment
# Cloning
In your terminal:

  $ git clone https://github.com/paulinenanzala19/utibucare.git
  $ cd utibucare
# Running the Application
Creating the virtual environment

  $ python3.8 -m venv --without-pip virtual
  $ source virtual/bin/activate
  $ curl https://bootstrap.pypa.io/get-pip.py | python
# Installing Django and other Modules

  $ python3  pip install django
  $ python3  pip install django-bootstrap3
  $ python3  pip install pillow
  $ python3  pip install django-registration
  $ python3  pip install django-crispy-forms
## To run the application, in your terminal:

  $ python manage.py runserver

# Technologies Used
Python3.10
Django
HTML
CSS(Bootstrap)
live link
['']

# known bugs
Yet to integrate the payment system