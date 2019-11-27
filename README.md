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

## Making sure dependencies are up to date
Run to install dependencies
```bash 
pip install -r requirements.txt
```

* Update requirements.txt if you add anything new (pip install)
    - ```bash
      pip freeze > requirements.txt
      ```

## Database Management
* Using a SQLite db locally
* Now you can use flask-sqlalchemy and flask-migrate to manage and interact with the db

### Flask-Migrate - Making Changes to the Database Structure/Schema
For initial setup:
    ```bash 
    flask db init
    ```
The above command would create the inital Migrations directory. Since the directory is in source control, you won't need to run it for this. But note that when you create migrations in the future, they need to be added to source control.

* Models are defined in app/models.py
* After making changes to models.py, you'll need to migrate the database to keep it in sync
    1.  To make a new migration file run:
        ```bash
        flask db migrate -m "optional description"
        ```
        * Note that this doesn't change the db, just generates a file in the migrations directory*
        * Make sure to add the file to source control *
    
    2. To apply the changes from the file generated above:
        ```bash
        flask db upgrade
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
