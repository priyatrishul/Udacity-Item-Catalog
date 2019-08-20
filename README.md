# Udacity Full Stack - Item Catalog Project

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.
In this sample project, the homepage displays all current categories along with the latest added items.

After the user has logged-in, user can add item to the categories and edit and delete the items they have created

### Requirements

1. This project makes use of the virtual machine to run the program. Download and 
Install `VirtualBox` from [here](https://www.virtualbox.org/).
2. Download and Install `Vagrant` from [here](https://www.vagrantup.com/).
3. Download vagrant directory with VM configurations from [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
4. Create Google credentials [here](https://console.developers.google.com/apis/credentials).
    - Click Create credentials 
    - Select OAuth client ID
    - Select Web application and create
    - provide Authorized Javascript origins as http://localhost:8000
    - provide Authorized redirect URIs as http://localhost:8000/login
    - provide Authorized redirect URIs as http://localhost:8000/gconnect
    - provide Authorized redirect URIs as http://localhost:8000/gdisconnect
    - Download JSON and rename as client_secrets.json and place in the same path your application    resides

### Steps to run the program

1. Place the contents of this repository in catalog folder of vagrant directory with VM configurations.
2. cd into the vagrant directory. Start the virtual machine by running command 
`vagrant up`.
3. When `vagrant up` is finished running,you can run `vagrant ssh` to log in.
4. to access the shared folder run

    `cd /vagrant/catalog`

5. Setup the database

    `python db_setup.py`
   
6. load sample data

    `python catalogdata.py`

7. Run the application

    `python catalog.py`

8. Access the application

    `http://localhost:8000/`

9. Access API Endpoints

    `http://localhost:8000/catalog.json`
    
    `http://localhost:8000/category.json`
    
    `http://localhost:8000/items.json`
