# Project 5: Brevet time calculator with Ajax and MongoDB

Reimplementation of the RUSA ACP controle time calculator with flask and ajax.

## ACP controle times

Controls are points where a rider must obtain proof of passage, and control times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here (https://rusa.org/pages/acp-brevet-control-times-calculator). 

Additional background information is given here (https://rusa.org/pages/rulesForRiders).  

This is a replacement of the calculator here (https://rusa.org/octime_acp.html).

## AJAX Flask and Mongo implementation

This code fills in times as the input fields are filled using Ajax and Flask.

Each time a distance is filled in, the corresponding open and close times are filled in with Ajax.

The submit button is then used to store valid control times in a mongodb database, making sure not to add duplicates. This database can be accessed and viewed on a separate page by clicking the display button.

## Testing

To run the server, change to the DockerMongo directory and type:

- $ sudo make

To exit the server hit:

- ctrl c

After closing the server, remove everything made by up:

- $ sudo make down

To remove docker images and containers:

- $ sudo make prune

Keep in mind that you will need docker and docker-compose installed on your local machine

## Authors

####Samuel Lundquist - slundqui@uoregon.edu
