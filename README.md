# HCC Workshop
The HCC Workshop is an interactive web application that showcases research undertaken by the Human Centred Computing research group within the Research School of Computer Science at The Australian National University.
Students and staff can develop and contribute toward new applications, host experiments to collect data, and promote research ideas.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.  
A step-by-step tutorial is available at [this link](***REMOVED***).
### Prerequisites
The workshop is built using Django 1.10.1, Bootstrap 3.3.7, HTML 5, CSS 3, and jQuery 3.1.1. All requirements are contained in the requirements.txt file which will be used during installation. We recommend working with Docker when setting up a development environment for the workshop.  
### Installation
These instructions will guide you through installing the development environment via the recommended method of using Docker. 
1. First, install all prerequisities and ensure they are up to date.
```
git --version
docker -v
docker-compose -v
```
2. Next, create a directory to store the files and clone the code from the CECS research gitlab instance.
```
cd path/to/some/directory
git clone ***REMOVED***
```
3. Do *not* work on the master branch. Create a new branch that is named after your application.
```
git checkout -b new-branch
```
Or, checkout an existing branch
```
git checkout existing-branch
```
4. Next, build and run the docker containers.
```
docker-compose up --build
```
5. Now you can load up your favourite text editor to make changes to the code. You can verify that the docker containers are running by viewing the output in the terminal, or opening up a new terminal and typing
```
docker ps
```

### Creating a new application
Once you have started the development environment, you must create your application. This will generate the necessary starter code that you will use. 
1. Launch a new terminal and navigate to the root folder of the project. 
```
cd path/to/some/directory/workshop
```
2. Run a command in the bash terminal of the docker web container
```
docker-compose run -d web python manage.py startapp yourapp
```
3. A new subfolder with all the necessary starter files will be generated in the root workshop directory. Open this folder and edit these files to start building your application.   

### Viewing progress
You are able to run the HCC workshop on your development machine to view and test it as you develop.  
1. If you installed the workshop via Docker, ensure that the Docker containers are running.
```
docker-compose up
```
2. Now, open a web browser and navigate to
```
http://localhost:8000
```
3. You can use the Docker console to help you debug the application. To shut down the development server, press Ctrl+C in the console.   

## Documentation
Documentation for running participants through the HCC Workshop is available upon request from [Christopher Chow](***REMOVED***).   

## Live Deployment
Installation and setup instructions for deploying the HCC Workshop on a web server is available upon request from [Christopher Chow](***REMOVED***).   

## Developing and Contributing 
Development for the HCC Workshop is only open to members of the ANU HCC research group. Please take a look at the [Contributing Guidelines](CONTRIBUTING.md) for basic instructions on contributing to this project. For all other queries, please contact the project maintainers.   

## Maintainers
* Christopher Chow, ***REMOVED***

## Acknowledgements
* Leana Copeland
* Jakub Nabaglo