# Galton

[![Build Status](https://scrutinizer-ci.com/g/galton-no/galton/badges/build.png?b=master)](https://scrutinizer-ci.com/g/galton-no/galton/build-status/master)

## How can I set up a development environment?

This is the process almost from scratch, assuming you're on a Mac and have installed Homebrew already.

1. Install Python: `brew install python3`.
2. Upgrade package management tools: `pip3 install --upgrade pip setuptools wheel`.
3. Install Virtualenv: `pip3 install virtualenv`.
4. Prepare to create you virtual environment: `mkdir ~/.virtualenvs`.
5. Create your virtual environment: `python3 -m venv ~/.virtualenvs/galton`.
6. Activate your virtual environment: `source ~/.virtualenvs/galton/bin/activate`.
7. Clone the repository: `git clone git@github.com:galton-no/galton.git`.
8. Navigate into the project: `cd galton`.
9. Install the required packages: `pip install -r requirements.txt`.
10. Start the development webserver: `python manage.py runserver`.
11. Visit [http://localhost:8000/](http://localhost:8000/).
