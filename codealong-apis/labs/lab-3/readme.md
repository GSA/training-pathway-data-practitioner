# Lab 3 Readme

## Lab Goal

The goal of this lab is to tour GSA's APIs.

## Skills and Info learned

- GSA's public APIs.
- Viewing API calls in browser.
- Using Google Chrome Developer Tools
- Viewing HTTP response codes
- Viewing Swagger documentation

## Lab Steps


Go to the GSA API directory at https://open.gsa.gov/api. Scroll down to the section titled "Featured GSA APIs". This is the official GSA API directory.

### Per Diem API

1. On the GSA APA directory page, scroll down to the "Per Diem API". Click the `View Project` button.

This should open the following page:

https://www.gsa.gov/technology/government-it-initiatives/digital-strategy/per-diem-apis/api-for-per-diem-rates

2. View the API documentation on this page.

Q1: What is the base URL for this API?

Q2: What is the response format for this API?


3. Scroll down the the Parameters table

Q3: What parameters can be used to search with this API?

4. Open a new browser window and copy the first sample URL into the path:

https://inventory.data.gov/api/action/datastore_search?resource_id=8ea44bc4-22ba-4386-b84c-1494ab28964b&filters={"FiscalYear":"2017","Zip":"10036"}

Examine the response data. 

Q1: What is the value for "Success:"?

Q2: How many records were returned by this API call?


5. In the browser window, change the URL to an invalid value:

https://inventory.data.gov/api/action/datastore_search?resource_id=8ea44bc4-22ba-4386-b84c-1494ab28964b&filters={"FiscalYear":"2017","Zip":"zzzzzz"}

Q3: What is the value for "Success:"?

6. In chrome, right click the page and select "Inspect" to open the Chrome Developer Tools.

7. Click the "Network" tab. Click F5 to re-run the API call. Click the first row that is in red. Click "Headers".

Q4: What is the HTTP status code?

8. Click "Response". 

Q5: What is the value for "Success:"?

Q6: What does the response say is wrong with this API call?

### eMuseum API


1. Scroll down to the API titled "eMuseum API". Click the `View Project` button. 
This should open the following page:
http://gsa.github.io/eMuseum-API

2. View the Overview page. 

* Q1: What is the name of this API?

* Q2: What is the purpose of this API?

3. View the API basics page.

* Q3: What is the source system (or systems) of this API?

4. View the API calls page to see the templates or enpoints available through this API.

5. In a separate browser window, paste this URL to see the Artist Index:

https://gsafinearts.pbs.gsa.gov/emuseum/api/search/people?Index=a

Q4: How many artists are returned by this query?

Q5: How do you know these records are artists?

Bonus questions:

* Q6: Where is this API documentation hosted?

* Q7: How do you provide feedback for this API?


### System for Award Management API

1. Scroll down to the API titled "System for Award Management API". Click the `View Project` button. 
This should open the following page:
http://gsa.github.io/sam_api/sam/

2. Go the "API Basics" tab. This has basic information about using the API.

3. Paste the Example URL into another browser tab:

https://api.data.gov/sam/v1/registrations/1459697830000?api_key=YOUR_API_KEY

Q1: What is the error message?

4. Use Chrome Developer Tools, Network to resubmit this request.

Q2: What is the HTTP response code?

Q3: What format is the response in?

5. Close Chrome Developer tools.

6. In the original Chrome window, replace `YOUR_API_KEY` with '`DEMO_KEY`

https://api.data.gov/sam/v1/registrations/1459697830000?api_key=DEMO_KEY

7. Back in the API documentation, go to the "API Calls" page.

8. Click the "Expand Operations" link to see the sample query.

Q4: What is the legalBusinessName for this result?

Q5: What is the HTTP Status code?







	