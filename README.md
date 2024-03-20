# Flask Web & Database Project Starter

This is a starter project for you to use to start your Flask web & database
projects.

It contains quite a lot of example code. You can use this to see how the various
parts of the project work, or you can delete it and start from scratch.

There are two videos to support:

* [A demonstration of setting up the project](https://www.youtube.com/watch?v=72JwLuAyHyM&t=360s)
* [A walkthrough of the project codebase](https://www.youtube.com/watch?v=72JwLuAyHyM&t=735s)

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Set up the virtual environment
; python -m venv web-application-starter-venv

# Activate the virtual environment
; source web-application-starter-venv/bin/activate 

# Install dependencies
(web-application-starter-venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Create a test and development database
(web-application-starter-venv); createdb YOUR_PROJECT_NAME
(web-application-starter-venv); createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(web-application-starter-venv); open lib/database_connection.py

# Seed the development database
(web-application-starter-venv); python seed_dev_database.py

# Run the tests (with extra logging)
(web-application-starter-venv); pytest -sv

# Run the web server
; python app.py
# Now visit http://localhost:5001/emoji in your browser
```

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-plain&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-plain&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-plain&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-plain&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-plain&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
