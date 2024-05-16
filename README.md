# 420HairSalon_finalProject
# Amy Nguyen, Iana Feniuc, Darina Hojeij
# May 2024

# README typed by Amy Nguyen on May 15 2024

# Important Notes
- Admin super :
    username = nasr
    password = 123

- Admin appoint :
    username = appoint_manager1
    password = 456

- Admin user :
    username = user_manager1
    password = 123

The rest of the users have a password of 12345.

# Project

This project is a full stack application using Flask, orientated in appointment making. There are different levels of access such as 
admins, clients, professionals, and default being visitor. 

Full stack with SQL database, HTML/CSS/JS front end, flask and python backend. 

# USERS
Admins:

Admin appoint is able to add/update/delete appointments, either via the nav bar or the appoint panel.
Admin user is able to add/update/delete users.
Admin super can do everything but add/update/delete an admin super.

Users:
There are clients, professionals, and visitors. Clients and professionals have similar permissions. When not logged in or registered, the default view is one of a visitor, who is able to view all appointments, and information about the website and the API.

All users can update their own profile, but limitations applies to users. All fields may be changed by admin_user or admin_super.

# Appointment

For clients:

The user is not permitted to change the username box as it is their appointment they are making. They are permitted to select the room number, date, time slot, professional and service.

For professionals:

Similar to the clients, but instead of professional, they pick which client they would like in the appointment.

For admins:

There is no username field, but a field for user and a field for professionals. They can pick whoever they wish, the rest are similar to the Member users.

All users are able to view appointments, and specific appointments excluding visitors. They may only edit/delete/add report for their own appointment except if their user type is admin_appoint or super.

All appointments can be filtered or sorted as any user wishes.

# Reports

Each appointment has one report. Can either be created if the user is apart of the appointment, or if they are admin_appoint/super. The reports can then be updated/deleted. One report per appointment only.

# API

The api focuses on GET all/specific, POST and DELETE of appointments. There is a document in the website located in the nav bar accessible for any users to view the API documentation, as well as test out the GET for all/specific appointment.


