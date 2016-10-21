# README #

### Author: Harpreet Dhillon , harpreet@uoregon.edu ###

---

### Purpose ###
* This application is for Project 4 of CIS 322 at University of Oregon.
* The purpose of this project was to clone the calculator at http://www.rusa.org/octime_acp.html and improve the system to use Flask and AJAX for realtime updates.

### Application Specifics ###
* The application runs on the flask_vocab.py script and displays either:
  * The index page template
  * or the respective error template: 400, 403, 500
* As keystrokes are read, a JSON object will be sent to the server via a POST request. The returned data will then either be displayed or make some modification to the anagram page.

### Running the Application ###
* Test deployment to other environments including Raspberry Pi.  Deployment 
  should work "out of the box" with this command sequence:
  * `git clone <yourGitRepository> <targetDirectory>`
  * `cd <targetDirectory>`
  * `make configure`
  * `make run`
  * (control-C to stop program)
* The default port is 5000, so the webserver should be reachable at http://localhost:5000 , and also through its IP address.
 
### Testing the Application ###
* Nose tests for acp_times.py can be run with:
  * `nosetests`
  * The nosetests test for boundary cases as well as random values.
