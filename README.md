# Digistarts - Technical Python Developer Test

API developed for Python developer testing at [Digistarts](https://www.digistarts.com/).

An API was developed to enable mathematical operations between two binary numbers.

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


### API endPoints
```
|-----------------------------------------------------------------------------------------|
| Objective                                           | Endpoints                | Verbs  |
|-----------------------------------------------------------------------------------------|
| Sum between two binary numbers                      | /v1/calculator/sum/      | POST   |
| Subtract between two binary numbers                 | /v1/calculator/sub/      | POST   |
| Multiply between two binary numbers                 | /v1/calculator/mult/     | POST   |
| Divide between two binary numbers                   | /v1/calculator/div/      | POST   |
| Resting between two binary numbers                  | /v1/calculator/mod/      | POST   |
|-----------------------------------------------------------------------------------------|
```

\* The case in question considers that the virtual environment was created within the project directory, if this is not the case, the activation path of the virtual environment should be changed according to the correct creation location.

