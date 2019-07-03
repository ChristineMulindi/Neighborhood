# Neighborhood

This a a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.


## Author

* **Christine Mulindi**

## Features


As a user, You will be able to:

1. Sign in with the application to start using.
2. Set up a profile about yourself and a general location and your neighborhood name.
3. Find a list of different businesses in your neighborhood.
4. Find Contact Information for the health department and Police authorities near your neighborhood.
5. Create Posts that will be visible to everyone in your neighborhood.
6. Change your neighborhood when you decide to move out.
7. Only view details of a single neighborhood.


### Installing

*** To view the app.Visit -> [neighborhood](https://github.com/ChristineMulindi/neighborhood)

1. Clone this repo: git clone https://github.com/ChristineMulindi/neighborhood.git.
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database gallery using the command below.


       CREATE DATABASE instaclone; 
       **if you opt to use your own database name, replace instaclone your preferred name, then also update settings.py variable DATABASES > NAME

5. Migrate the database using the command below


       python3.6 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Running the tests

Use the command given below to run automated tests.


        python manage.py test 




## Built With

* [Django](https://www.djangoproject.com/) - web framework used
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## License

This project is licensed under the MIT License.Copyright 2019( ChristineMulindi)