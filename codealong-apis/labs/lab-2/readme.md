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

Q1: What is the Origin of all these records?

2. Go to the website hurl.it

3. In the "GET" box, type the URL from above and click "Launch request". 

Q2: What was the HTTP response code?


4. Change the destination next to Get to: "https://api.gsa.gov/travel/citypairs/v0/airfares" and add the following in the "Add Parameter" section:

Name: award_year
Value: 2017

Name: origin_airport_abbrev
Value: ABQ

Name: api_key
Value: DEMO_KEY

5. Refresh the page and repeat step 4 with these values:

Name: award_year
Value: 2017

Name: origin_airport_abbrev
Value: XXXX

Name: api_key
Value: DEMO_KEY


Q3. What is the HTTP response code?

6. Add the Destination City Code with a value of "XXX" and click "Launch request".

Q4: What is the HTTP response code?

Q5: What should the code be?

7. Go to this issue in Github:

https://github.com/GSA/prototype-city-pairs-api/issues/44

8. View this page:
https://github.com/GSA/prototype-city-pairs-api/blob/master/standards.md

Q6: What do these standards say about the Error Handling in the City Pairs API?


## Teacher notes
