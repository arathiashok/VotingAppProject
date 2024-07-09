# Voting App Team 5

[![Quality Gate Status](https://sonarqube.cs.uiowa.edu/api/project_badges/measure?project=Team5-Voting&metric=alert_status&token=sqb_61cdcc22cb5d4fa12b817dd343132d3c189a12c2)](https://sonarqube.cs.uiowa.edu/dashboard?id=Team5-Voting)

Arathi, Izzy, Eric

## Environment Requirements

[All environment requirements required to run locally here](https://uiowa.instructure.com/groups/193777/pages/environment-requirements). All future steps assume these minimum instructions have been met.

Each section assumes:
- Git Bash terminal running at top level directory


## How to start the website

`. ./scripts/start_website_dev.sh`

## How to start without Docker

`export FLASK_ENV=development`
`export FLASK_APP=./app/src`
`python -m flask run --host=0.0.0.0`

Access website at [http://localhost:5000](http://localhost:5000)

## How to run automated tests

`. ./scripts/run_automated_tests.sh`

## How to run automated tests without Docker

`python -m pytest`

Access output in CLI.

## Directory Tree

```
.

├── app
│   ├── src
│   │   ├── main
│   │   │   ├── __init__.py
│   │   │   ├── main_controller.py
│   │   │   └── routes.py
│   │   ├── templates
│   │   ├── user
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── test_model.py
│   │   ├── __init__.py
│   │   └── config.py
│   ├── tests
│   │   ├── main_tests
│   │   │   └── main_route_test.py
│   │   └── conftest.py
│   ├── Dockerfile
│   ├── poetry.lock
│   └── pyproject.toml
├── db
│   └── init.sql
├── docs
│   └── assets
│       ├── App Architecture Diagram.png
│       └── App Sonar Integration.png
├── scripts
│   ├── run_automated_tests.sh
│   └── start_website_dev.sh
├── .gitignore
├── .gitlab-ci.yml
├── docker-compose.yml
└── README.md
```

- `./app` - Stores the website
- `./db` - Stores the `init.sql` that contains the SQL for the database
- `./scripts` Stores any CI tests or local scripts for environment management or automated testing

## Diagrams

#### Architecture Diagram of running application
![Architecture Diagram](docs/assets/App%20Architecture%20Diagram.png)

#### Sonar Integration Diagram
![Sonar Integration Diagram](docs/assets/App%20Sonar%20Integration.png)


# References:

- [Flask file structure following MVC Pattern](https://plainenglish.io/blog/flask-crud-application-using-mvc-architecture)
- [Flask integration with Docker](https://blog.abbasmj.com/dockerizing-flaskmysql-application-using-compose)
- [Poetry integration with Docker](https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker)