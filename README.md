# Studio Ghibli Python App
A Python Flask webapp that utilizes [Studio Ghibli API](https://ghibliapi.herokuapp.com/). With full documentation and Unit Testing. As well as instructions on how to run it. And demo a deployed version of the app.

### Contents
- [Code Structure](#code-structure)
- [Perspective](#perspective)
- [Dependancies](#dependancies)
- [Installation](#installation)
- [Deployed App](#deployed-app)


#### Code Structure
###### Code is divided into two main sections
1. **app** directory. **Flask** web application that has a site and API that gets all Studio Ghibli movies as well as people/characters in them.
2. **tests** directory. Has unittests using Pytest for all sections of app.

#### Perspective
- In **app/services**, There are two services:
    1. ghibli.py for dealing with Ghibli API.
    2. cache.py for caching requests for 1 minute as per the spec of the task.

- In **app/site**, As specified, There is a `/movies/` endpoint that returns all Studio Ghibli movies as well as people/characters in them in a nice HTML UI. With the help of **Bootstrap**.
    - For convenience, I show the number of movies retrieved from the API in the navigation bar.
    - Because movie fans are a very anxious crowd when it comes to new releases, I cache the results of the `/movies/` **GET** request for 1 minute. Then after that interval has passed I get a new version of the data from the API.

- In **app/api**, There is a `/api/movies/` API endpoint that returns all Studio Ghibli movies in JSON format to be consumed by any client.

    - Further in **app/docs**, I added documentation for API using Swagger UI. 
    - To view Swagger API documentation go to:
    `localhost:8000/apidocs/`


#### Dependancies
0. Python 3.7.* or higher is installed. Install instructions [here](https://www.python.org/downloads/).
1. Make sure virtualenv is installed, if not check [here](https://virtualenv.pypa.io/en/latest/installation/).

#### Installation
1. Clone repository into an empty directory on your machine. 
`git clone https://github.com/captainmoha/moviepy`
2. Create a virtual env in the same parent directory in which you cloned the repo.
`virtualenv -p python3 app_env`
3. Activate virtual env in your terminal.
`source app_env/bin/activate`
4. Go to repo directory.
`cd moviepy`
5. Install requirements
`pip install -r requirements.txt`
6. Run **Flask** web app.
`flask run`
7. Open browser to check out the running app
go to `localhost:8000/movies/`
8. To view Swagger API documentation
go to `localhost:8000/apidocs/`
9. In another terminal you can run app unit tests go to moviepy directory:
`cd moviepy`
then run 
`pytest`


#### Deployed App
- For convenience, I have also deployed the application on **Heroku** cloud platform to see a quick glance of the application.
- Links: 
App: https://moviepy.herokuapp.com/movies/
Documentation https://moviepy.herokuapp.com/apidocs/