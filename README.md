# Introduction

Rates API is a HTTP based API which calculates the average price of an ocean and air freight rates for each day on a route between origin and destination region.

This has the following tech stack
* [Docker](https://www.docker.com/) : It is a technology that packages an application into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.
* [Flask Rest X](https://github.com/python-restx/flask-restx) : Flask-RESTX is an extension for Flask that encourages best practices with minimal setup. It provides a coherent collection of decorators and tools to describe API and expose its documentation properly using Swagger.
* [Postgres](https://www.postgresql.org/): Most used, powerful, open source object relational database.  

# Other Technologies

* [Pre-commit hook](https://pre-commit.com/): Git hook scripts to identify issues and quality of your code before pushing it to GitHub
* [Pytest](https://github.com/pytest-dev/pytest): Testing framework for python code
* [Faker](https://github.com/joke2k/faker): Python package that generate fake data for testing

# Setup Guide

This application is setup with docker, so don't forget to install [Docker Engine](https://docs.docker.com/engine/install/) and [Docker compose](https://docs.docker.com/compose/) in your system before using it.

* Clone this repository to your local machine
  ```
  git clone git@github.com:3sarojbhattarai/rates-api.git
  ```
* Please check docker-compose.yml file and change the value if necessary.

* Build the images and run the containers

  ```
  docker-compose up --build
  ```

* Test it out at http://localhost:5000 where you will see swagger documentation.

* Curl command to see rates between two regions in an specified date range.  

   GET /rates/regions
  ```
  curl "http://127.0.0.1:5000/rates/regions?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
  ```

# Test with Pytest

* To run pyest, you have to go inside docker container
  ```
    docker exec -it rates-api bash
  ```

* Inside container, run Pytest 

  ```
    pytest -v
  ```
