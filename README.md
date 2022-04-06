# DSA_1008_TaxiService
The '''best''' taxi service, served by Flask. 

# Requirements
Required libraries are in requirements.txt.
Run `pip install -r requirements.txt` in the root folder of the project to run it.

# Running the project
Included with the project is a PowerShell script `start_flask.ps1` which can be used to setup the configuration needed. However, it is understandable that running PowerShell scripts are a hassle since you need to disable some things and what not. Thus, run the following commands (while in the root folder of the project) to achieve the equivalent.
**For cmd:**

    set FLASK_APP=.
    flask run
   
**For PowerShell**

    $env:FLASK_APP = "."
    flask run

**For Linux/Unix**

    export FLASK_APP=.
    flask run
