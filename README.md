This repo contains all the code and files associated with the completely functional CIMP backend system (as a part of the CodeChef Club Recruitment Challenge)

Tech Stack & Tools:
-  Python (Flask Framework)
-  MySQL (Database)
-  RESTful APIs (JSON)
-  Postman (API Testing)
-  Git & GitHub (Version Control)

API routes:
CLUB MANAGEMENT:
/clubs/create
/clubs/all

ROLES ASSIGNMENT AND MANAGEMENT:
/roles/assign-president
/roles/assign-faculty

MAMANGEMENT (ADD, DELETE, MODIFY) OF CLUB MEMBERS:
/members/add
/members/remove



MySQL is used for DBMS as the given challenge does have a relational model.
Database name: cimp_portal

Tables in cimp_portal:
clubs, students, club_members, faculty

Important Note:

1) In order to ensure security, the connection between Flask and the MySQL database is made through the use of a .env file which contains the password
of the root user (in the localhost)

2) And in order to ensure proper heirarchy, the api routes associated with specific functions such as clubs, members and role management are defined in
different .py files which are then integrated with the main app.py file by registering (and thereby) blueprints associated with those api routes 
(from other files to app.py)


