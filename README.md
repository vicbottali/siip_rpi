# Siip
Flask application to be run on a Raspberry Pi.

### Setup

* git clone [https://github.com/vicbottali/siip_rpi.git]
* cd into the project directory
* Setup virtual environment 
    ```bash
    python3 -m venv venv
    ```
* Activate virtual environment
    ```bash
    . venv/bin/activate
    ```
* Make sure flask is installed
    ```bash
    pip install Flask
    ```

### Running locally

* Export application environment variable - where app.py is the file name of the application
    ```bash
    export FLASK_APP=app.py 
    ```
* If you want to run the development server in debug mode (so you don't have stop and restart after changes)
    ```bash
    export FLASK_ENV=development 
    ```
* Run development server 
    ```bash
    flask run
    # If python 2 is giving you trouble, you can try to run it with python3 like below:
    python3 -m flask run
    ```


#### Other Resources
===

* Sqlite3 - Used for the database
    - Helpful tutorial for basic CRUD operations [https://stackabuse.com/a-sqlite-tutorial-with-python/]

* RFID Reader
    - Uses the mfrc522 library for interaction
    - Full instructions [https://pimylifeup.com/raspberry-pi-rfid-rc522/]

* JQuery - Commonly used JavaScript library
    - Loaded in base.html from a CDN (basically I'm dowloading it from a remote source when the page loads)
    - Currently used in main.html, to alter the frontend and make the AJAX request to the flask server, to tell the Reader to        start reading
    - Once the information is read, return data to the frontend as a JSON reponse, then take action via the frontend

* Hammer js - JavaScript Library for registering touchscreen events
    - Saved locally in static/js/
    - You can see it used in main.html, listening for a 'tap' event where JQuery is listening for a 'click' event
