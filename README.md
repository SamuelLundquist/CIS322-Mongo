# Project 5: Brevet time calculator with Ajax and MongoDB

Simple list of controle times from project 4 stored in MongoDB database.

## What is in this repository

You have a minimal implementation of Docker compose in DockerMongo folder, using which you can connect the flask app to MongoDB (as demonstrated in class). Refer to the lecture slide "05a-Table-driven.pdf" and "05b-Docker-Compose.pdf" (dated 10/24 and 10/26). You'll also need MongoCommands.txt. Solved acp_times.py file is in piazza under resources tab! 

## Functionality you'll add

You will reuse *your* code from project 4 (https://bitbucket.org/UOCIS322/proj4-brevets/). Recall: you created a list of open and close controle times using AJAX. In this project, you will create the following functionality. 1) Create two buttons ("Submit") and ("Display") in the page where have controle times. 2) On clicking the Submit button, the control times should be entered into the database. 3) On clicking the Display button, the entries from the database should be displayed in a new page. 

Handle error cases appropriately. For example, Submit should return an error if there are no controle times. One can imagine many such cases: you'll come up with as many cases as possible.

## Tasks

You'll turn in your credentials.ini using which we will get the following:

* The working application.

* A README.md file that includes not only identifying information (your name) but but also a revised, clear specification 
  of the brevet controle time calculation rules.

* Dockerfile

* Test cases for the two buttons. No need to run nose.

* docker-compose.yml

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* AJAX in the frontend. That is, open and close times are automatically populated, 
	* Frontend to backend interaction (with correct requests/responses), 
	* README is updated with your name and email.

* If the AJAX logic is not working, 10 points will be docked off. 

* If the README is not clear or missing, up to 15 points will be docked off. 

* If the two test cases fail, up to 15 points will be docked off. 

* If the logic to enter into or retrieve from the database is wrong, 30 points will be docked off.

* If none of the functionalities work, 30 points will be given assuming 
    * The credentials.ini is submitted with the correct URL of your repo, and
    * Dockerfile is present 
    * Docker-compose.yml works/builds without any errors 

* If the Docker-compose.yml doesn't build or is missing, 10 points will be docked off.

* If credentials.ini is missing, 0 will be assigned.
