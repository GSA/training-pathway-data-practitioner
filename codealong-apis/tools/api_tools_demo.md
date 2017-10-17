# API Tools Demo

## SOAPUI

1. Open new REST project.

2. A dialog will be displayed. Enter the following in the "URI" box (using Per Diem API):

https://api.data.gov/sam/v1/registrations/1459697830000?api_key=DEMO_KEY

Click OK.

3. A REST project will be displayed. The hierarchy for SOAPUI is:

* Project
 * Service
  * Resource
   * Method
    * Request

4. In the Request dialog, notice the following:

HTTP Method: defaults to GET
Endpoint: the Base URI
Resource: everything from the Base URI to the parameters
Parameters: on the URL path (for GET)
Parameter box: individual parameters
api_key - For api.gsa.gov

5. Click run button. Click the JSON tab, to see the data that is returned. (SOAPUI defaults to XML.)

6. Compare to SAM API documentation: http://gsa.github.io/sam_api/sam/console/

In doco, registration ID is listed as a "path" parameter, and is part of the path.

7. To do this in SOAPUI, add a new parameter named "RegistrationID". Make the Style "Template". Add a value of 	`1459697830000`.

8. Note the "resource" box at the top has a new item in it: {RegistrationId}
Remove the number in front of it, so that the resource value is: `/sam/v1/registrations/{RegistrationId}`

9. Run the API again. You should get the same result.

10. Look at various things like headers, response, etc.

## POSTMAN

1. Open PostMan, click Import. This allows you to import a variety of files, such as RAML, WADL, Swagger/OpenAPI. We will be using the OpenAPI from the City Pairs API.

2. Click import from link.

3. Open the Prototype City Pairs API documentation: https://gsa.github.io/prototype-city-pairs-api-documentation/api-docs/console/

4. Right click and open the citypairs.json file. This is in the OpenAPI 2.0 specification. 


5. Copy the URL from this JSON file:

https://gsa.github.io/prototype-city-pairs-api-documentation/api-docs/console/citypairs.json

6. In PostMan, past this into the import dialog. Click Import.

7. You should see a dialog that says "Collection imported".

8. Click the collection labeled "Prototype City Pairs API" in the left hand side. Click the "airfares folder". 

9. There are two GET requests listed:

Negotiated Airfares
Individual Airfare by ID

Show this matches the Swagger documentation. Explain this is all set by the OpenAPI file.

## Negotiated Airfares

10. Click the Negotiated Airfares, Click params.

11. Replace the values as follows:

award_year: 2017

origin_airport_abbrev: ABQ

destination_airport_abbrev: BWI

api_key: DEMO_KEY

12. View data result, Status.

## Individual Airfare by ID

13. Click the Individual Airfare by ID request.

14. Click params.

15. Replace the values as follows:

id: 999

api_key: DEMO_KEY


16. Explain the id is in the URL path.

17. Note: the API spec doesn't guarantee the API will behave this way. The API implementation is separate.
