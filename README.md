# Take_break

This a commandline application that helps you to take a break

## Prerequisites

- [python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
- [python3-dev](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-16-04-server)
- [cup of coffee](https://www.wikihow.com/Make-Instant-Coffee)

## Installation

follow the instruction carefully

1. `git clone the repo` and into Take_break
2. create a virtual environment by running `virtualenv -p python3 venv`
3. initialize the env by running `source venv/bin/activate`
4. install the dependencies `pip install -r requirements.txt`
5. bundle the cli-app by running `python setup.py bdist_wheel --universal`
6. the pip install break-app `pip install dist/BreakApp-0.10-py2.py3-none-any.whl`
7. then run the app `breakapp`
