# Digistarts - Technical Python Developer Test

[![Build Status](https://travis-ci.org/carlos-moreno/digistarts-challenge.svg?branch=master)](https://travis-ci.org/carlos-moreno/digistarts-challenge)
[![Maintainability](https://api.codeclimate.com/v1/badges/eec3a1a3074473d330cc/maintainability)](https://codeclimate.com/github/carlos-moreno/digistarts-challenge/maintainability)
[![codecov](https://codecov.io/gh/carlos-moreno/digistarts-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/carlos-moreno/digistarts-challenge)


API developed for Python developer testing at [Digistarts](https://www.digistarts.com/).

An API was developed to allow mathematical operations (+, -, *, / and %) between two binary numbers and also to generate a set with unique elements ordered in ascending order.

## How to execute the project?

- Clone the repository
```
git clone https://github.com/carlos-moreno/digistarts-challenge.git
```
- Access the application directory
```
cd digistarts-challenge
```
- Install the dependencies *
```
pipenv sync --dev
```
- Active virtualenv
```
source .venv/bin/activate
``` 
- Run the tests
```
pytest -v
```
- Start project
```
uvicorn app.main:app --reload
```

### API endpoints
```
|-----------------------------------------------------------------------------------------|
| Objective                                           | Endpoints                | Verbs  |
|-----------------------------------------------------------------------------------------|
| Sum between two binary numbers                      | /v1/calculator/sum/      | POST   |
| Subtract between two binary numbers                 | /v1/calculator/sub/      | POST   |
| Multiply between two binary numbers                 | /v1/calculator/mult/     | POST   |
| Divide between two binary numbers                   | /v1/calculator/div/      | POST   |
| Resting between two binary numbers                  | /v1/calculator/mod/      | POST   |
| Return a set of unique elements                     | /v1/vector/set/          | POST   |
|-----------------------------------------------------------------------------------------|
```

### Examples of requests

![Page of docs](https://carlos-moreno.github.com/imgs/page-docs.png)

### Tip:

If you do not want to configure the application locally, you can execute it using a docker image
 created for the project according to the steps below.
 
* Run the command below to download the docker image
```
docker pull carlosmoreno/digistarts-challenge
```
* Run the command below to start the project
```
docker run -d --name challenge -p 8000:80 carlosmoreno/digistarts-challenge
```

Now just access the API at http://127.0.0.1:8000

\* The case in question considers that the virtual environment was created within the project directory, if this is not the case, the activation path of the virtual environment should be changed according to the correct creation location.

