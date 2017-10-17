# Lab 2 Readme

## Lab Goal

The goal of this lab is to retrieve data from the Prototype City Pairs API.


## Skills and Info learned

- GSA API Standards
- REST APIs
- HTTP GET
- https://www.hurl.it


## Lab Steps

1. Open the web browser, and paste the following URL into the address bar:

https://api.gsa.gov/travel/citypairs/v0/airfares?award_year=2017&origin_airport_abbrev=ABQ&api_key=DEMO_KEY

* Q1: What is the ORIGIN_CITY_NAME of all these records?

2. Go to the website hurl.it

3. In the Destination box, type the URL from Step 1 and click "Launch request". 

* Q2: What was the HTTP response code?

4. Change the Destination to: "https://api.gsa.gov/travel/citypairs/v0/airfares" and add the following in the "Add Parameter" section:

Name: award_year
Value: 2017

Name: origin_airport_abbrev
Value: ABQ

Name: api_key
Value: DEMO_KEY

5. Click Launch Request.

* Q3: What is the HTTP Verb and URL used?

6. Refresh the page and repeat step 4 and 5 with these values:

Name: award_year
Value: 2017

Name: origin_airport_abbrev
Value: XXXX

Name: api_key
Value: DEMO_KEY


* Q4. What is the HTTP response code?

* Q5. What is in the BODY?

7. Delete the origin_airport_abbrev parameter and click "Launch request".

* Q6: What is the HTTP response code?


