# Lab 6 Readme

## Lab Goal

The goal of this lab is to use Google Scripts to consume REST APIs.

At GSA, Google Scripts are governed by the policies as listed on this page:

https://insite.gsa.gov/portal/content/540025

## Skills and Info learned

Populate a Google Spreadsheet with data from a REST API.

## Lab Steps

1. Log into GSA email in Chrome.

2. Open a new tab and go to https://drive.google.com.

3. Create a new Google spreadsheet and name it Code_Along_API_Sample.

3. Enter the following to set up the spreadsheet (if you copy and paste, be sure to right click and paste "Values only"):

A1 - `Code Along API`


B8 - `Airfares`

Row 9 -- Copy the values below, then right click on row 9 in your spreadsheet and select "Paste Special..Paste Values Only" :

| ID | ITEM_NUM | AWARD_YEAR | ORIGIN_AIRPORT_ABBREV | ORIGIN_CITY_NAME | DESTINATION_AIRPORT_ABBREV | DESTINATION_CITY_NAME | YCA_FARE | XCA_FARE |
| -- | -------- | ---------- | --------------------- | ---------------- | -------------------------- | --------------------- | -------- | -------- |   

4. Double-click teh bottom tab labeled `Sheet1` and rename this spreadsheet to `Worksheet`.

5. Select "Tools...Script Editor" to open a Google script.

6. Click the title `Untitled project` and rename to `GSA_IG_CODEALONG_TEMP`

### First function

7. Replace the body of the script with the following:

```/* Function that calls the API */
function getCityPairsFromURL (URL) {
    
  Logger.log(URL); //log data to logger to check
  
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Worksheet'); 
    
  var response = UrlFetchApp.fetch(URL); // call the API

  // Parse the JSON reply

  var textResponse = response.getContentText(); // get the response content as text
  var jsonData = JSON.parse(textResponse); //parse text into json
  
  //clear the old results
    sheet.getRange(10,1,500,10).clear();

  //create array to hold data
  var dataArray = [];
  
	
    for each (var airfare in jsonData.result) {
      dataArray=[]; //replace array
      
      dataArray.push(airfare.ID, 
                 airfare.ITEM_NUM,
                 airfare.AWARD_YEAR, 
                 airfare.ORIGIN_AIRPORT_ABBREV, 
                 airfare.ORIGIN_CITY_NAME,
                 airfare.DESTINATION_AIRPORT_ABBREV,
                 airfare.DESTINATION_CITY_NAME,
                 airfare.YCA_FARE,
                 airfare.XCA_FARE
                ); 
      sheet.appendRow(dataArray)
    
  }
  }
```
  
 Click save. 

### Second Function

8. Paste the following text at the bottom of the script, outside any other braces.

```  
/* Quick sample to call API */
  function quickAPICall() {
    
	var url = 'https://api.gsa.gov/travel/citypairs/v0/airfares?award_year=2017&origin_airport_abbrev=ABQ&api_key=DEMO_KEY';
    
    getCityPairsFromURL(url); 
  
  }
```
 
Click save.
 
 ### Testing the functions
 
9.  In the script editor, select `quickAPICall` from the drop-down box.
 
10. Click the "run" (triangle) button.
 
11. The first time you run this, you will receive a dialog that says :Authorization required". Click "Review Permissions".

12. You may be asked "Choose an Account From GSA.GOV". Select your GSA email.

13. The dialog will say "GSA_IG_CODEALONG_TEMP" wants to View and manage your spreadsheets in Google Drive and Connect To An External Service.  Click the "Allow" button.

14. A dialog should be displayed with the message `Running function quickAPICall". 

15. When the message disappears, switch the Chrome tab to view the spreadsheet. There should be data populated in row 10 and below.


### Adding Year and Origination City Parameters

16. Add the following values to the spreadsheet:

A4 - `Award Year`

B4 - `2017`

A5 - `Origination City Abbreviation`

B5 - `ABY - ALBANY`

17. Switch back to the script editor. Copy and paste the following at the bottom of the script.
  
```
  //calls by year, origination city
  function getCityPairsByOriginationCity() {
    
    var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Worksheet'); //get sheet by name from active spreadsheet
  
  //get values from spreadsheet
  var award_year = sheet.getRange(4,2).getValue();
  
  var origination_combined = sheet.getRange(5,2).getValue(); 
  
  var split_origination = origination_combined.split(" - ");
  
  var origin_airport_abbrev = split_origination[0];
      
  var apiKey = "DEMO_KEY"; //apiKey for api.data.gov
  
  var myURL = 'https://api.gsa.gov/travel/citypairs/v0/airfares?award_year=' + award_year +"&origin_airport_abbrev=" + origin_airport_abbrev + "&api_key=" + apiKey; //api endpoint as a string 
    
   getCityPairsFromURL(myURL); 
    
  }
```
Click Save.

18. In the script editor, select `getCityPairsByOriginationCity` from the drop-down box.

19. After the function runs, switch to the spreadsheet tab. The data should be replaced.

### Adding Destination City parameter

20. Add the following values to the spreadsheet:

A6 - `Desintation City Abbreviation`

B6 - `DCA - WASHINGTON`

21. Switch back to the script editor. Copy and paste the following at the bottom of the script.


```
//calls by year, destination city
  function getCityPairsByDestinationCity() {
    
    var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Worksheet'); //get sheet by name from active spreadsheet
  
  //get values from spreadsheet
  var award_year = sheet.getRange(4,2).getValue();
  
  var destination_combined = sheet.getRange(6,2).getValue(); 
  
  var split_destination = destination_combined.split(" - ");
  
  var dest_airport_abbrev = split_destination[0];
      
  var apiKey = "DEMO_KEY"; //apiKey for forecast.io weather api
  
  var myURL = 'https://api.gsa.gov/travel/citypairs/v0/airfares?award_year=' + award_year +"&destination_airport_abbrev=" + dest_airport_abbrev + "&api_key=" + apiKey; //api endpoint as a string 
    
   getCityPairsFromURL(myURL); 
    
  }
```
Click Save.

22. In the script editor, select `getCityPairsByDestinationCity` from the drop-down box.

23. After the function runs, switch to the spreadsheet tab. The data should be replaced.

### Add method using both parameters

24. Switch back to the script editor. Copy and paste the following at the bottom of the script.

```
//calls by year, origination city, destination city
function getCityPairsByBoth() {
    
    var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Worksheet'); //get sheet by name from active spreadsheet
  
  //get values from spreadsheet
  var award_year = sheet.getRange(4,2).getValue();
  
  var origination_combined = sheet.getRange(5,2).getValue(); 
  
  var split_origination = origination_combined.split(" - ");
  
  var origin_airport_abbrev = split_origination[0];
  
  var destination_combined = sheet.getRange(6,2).getValue(); 
  
  var split_destination = destination_combined.split(" - ");
  
  var dest_airport_abbrev = split_destination[0];
      
  var apiKey = "DEMO_KEY"; //apiKey for api.gsa.gov
  
  
  
  var myURL = 'https://api.gsa.gov/travel/citypairs/v0/airfares?award_year=' + award_year +"&origin_airport_abbrev=" + origin_airport_abbrev+"&destination_airport_abbrev=" + dest_airport_abbrev + "&api_key=" + apiKey; //api endpoint as a string 
    
   getCityPairsFromURL(myURL); 
    
  }
```
  
Click Save.


25. In the script editor, select `getCityPairsByBoth` from the drop-down box.

26. After the function runs, switch to the spreadsheet tab. The data should be replaced.

### Add Function Calls to Menu

27. Switch back to the script editor. Copy and paste the following at the bottom of the script.

```
//this method adds the menu to the spreadsheet
function onOpen() {
  var ss = SpreadsheetApp.getUi();
 ss.createMenu('Call City Pairs API')
 .addItem('Get City Pairs By Origination City', 'getCityPairsByOriginationCity')
  .addItem('Get City Pairs By Destination City', 'getCityPairsByDestinationCity')
  .addItem('Get City Pairs By Both', 'getCityPairsByBoth')
      .addToUi();
}
```

Click Save.

28. Switch to spreadsheet and refresh or reload the page.

29. After a few seconds, the menu should be added titled `Call City Pair API`

30. Test all 3 methods from the menu and verify data is updated each time.


### BONUS MATERIAL: POPULATING DROP-DOWN BOXES FOR PARAMETERS


31. Create a new tab in the Google spreadshet, and label it "Origination".

32. Open the Excel spreadsheet titled "api_sample_data.xls".

33. Copy the data from the Excel tab titled "ORIGINATION". Select all the data in the Excel spreadsheet, copy and past it into the matching Google spreadsheeet.

34. Go back to the Google spreadsheet titled "Worksheet".

35. Select cell C5.

36. From the menu, select "Data...Data Validation". 

37. In the "Data Validation" dialog, select the box next to the "Criteria" box and select "Select Data Range".

38. The "What Data?" Dialog will be displayed. Click on the "ORIGINATION" tab. Select the header above Column C (which has combined these values). The dialog should be populated with the value "ORIGINATION!C:C".

39. Click "Save".

40. Cell B5 should now be populated with values from the "ORIGINATION" tab.

41. Change the value in cell B5 to another city. Select "Call City Pairs API...Get City Pairs By Origination City" from the menu.

### Adding drop-downs for Award Year and Destination City

42. Repeat steps 31-41 to add a drop-down box for Award Year, using the correct data from the Excel spreadseheet.

43. Repeat steps 31-41 to add a drop-down box for Destination City, using the correct data from the Excel spreadseheet.












