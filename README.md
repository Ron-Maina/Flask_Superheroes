# Flask Superheroes

## Description
An API for tracking heroes and their superpowers.

## Deliverables
* Contained in the README in the code-challenge directory

## Requirements
- Internet Access
- Visual Studio Code
- Postman

## Project Setup

* Open the terminal and clone the repo
```
git clone git@github.com:Ron-Maina/Flask-superheroes.git
```
* Change directory into the cloned repo by running
```
cd Flask-superheroes
```
* Open with visual studio by running 
```
code .
```
* To install the project's dependencies, open a terminal window in visual studio and run
```
pipenv install
```
* After dependencies are done installing, open the project's virtualenv
```
pipenv shell
```
* Change directory into the app folder
```
cd python-code-challenge-superheroes/code-challenge/app
```
* Run the following to create and seed the database
```
flask db revision --autogenerate -m "Creating tables"
flask db upgrade
python seed.py
```
* Run the command below and open the link to use the API based on the routes required and test endpoints using postman
```
flask run
```
* On a new terminal window change directory into the client folder 
```
cd python-code-challenge-superheroes/code-challenge/client
```
* Install npm dependencies and run the server to interact with the front end
```
npm install
npm start
```

## Author
* Ron Maina

## License 
MIT License

Copyright (c) [2023] [Ron Maina]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.