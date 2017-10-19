# Lab 5 Readme

## Lab Goal

The goal of this lab is to use HTML and JavaScript to consume REST APIs. We will be using the APIs provided by GSA's Enterprise Analytics and Reporting (GEAR) application.

## Skills and Info learned
Building a web page that uses APIs.


## Lab Steps

### GEAR List Page

1. In your browser, go to the following URL: https://dev.ea.gsa.gov/#!/siteoverview

2. Click on the Data Services tab to see a listing of the GEAR APIs.

3. Click on "IT Standards APIs" to see the API endpoints for IT Standards:

4. Open a browser window and type the following endpoint in the Address bar to get a listing of all the IT Standards:

https://ea.gsa.gov/api/v0/itstandards

5. Create a folder on your Windows desktop nameed "API-Lab-5". Right click and download the file [GEAR_1.html](GEAR_1.html) from the repository and save to the folder you created.

6. Double click on the file where it is stored on your local hard drive to open it in the browser. If it opens in IE, copy the address from IE and open a tab in Chrome. Paste the address into the Chrome address bar. It will start with `file://`.

7. Open this file in a text editor of some kind, such as notepad++, Texpad, or something similar.

8. Copy the following directly above the `</BODY></HTML>` tags at the the bottom of the file after closing:

```
<!-- This script populates the data in the table -->
<script>

$(document).ready(function(){

    //jQuery.support.cors = true;

    $.ajax(
    {
        type: "GET",
		url: 'https://dev.ea.gsa.gov/api/v0/itstandards/',
        data: "{}",
        dataType: "json",
        cache: false,
        success: function (data) {
            
var trHTML = '';

$.each(data, function (i, item) {
    trHTML += '<tr><td>'
	+ item.ID + '</td><td>' 
	+ item.Name + '</td><td>' 
	+ item.Type + '</td><td>' 
	+ item.Category + '</td></tr>';
});

$('#location').append(trHTML);
        
        },
        
        error: function (msg) {
            
            alert(msg.responseText);
        }
    });
})

</script>
```

9. Reload the web page in the browser. You should see data displayed in the table below the headers. This from the GEAR API. (Note: should match GEAR_1b.html after this step.)

### GEAR DETAIL PAGE


10. Make a copy of the file GEAR_2.html from the repository and save to your local hard drive in the same folder as the first file.

11. Open another browser tab and copy the URL from the first file. Then change GEAR_1.html to GEAR_2.html to open the second file in the browser.

12. Open this file in a text editor of some kind, such as notepad++, Texpad, or something similar.

13. Copy the following directly above the `</BODY></HTML>` tags at the the bottom of the file after closing:

```
<!-- This script populates the data for the detailed record -->
<script>

var ID = GetURLParameter('ID');

$(document).ready(function(){

    $.ajax(
    {
        type: "GET",
		url: 'https://dev.ea.gsa.gov/api/v0/itstandards/6041',
        data: "{}",
        dataType: "json",
        cache: false,
        success: function (data) {
            
var trHTML = '';

$.each(data, function (i, item) {
    trHTML += '<tr><td>' 
	+ item.ID + '</td><td>' 
	+ item.Name + '</td><td>' 
	+ item.Type + '</td><td>' 
	+ item.Category + '</td><td>' 	
	+ item.Status + '</td><td>' 	
	+ item.DeploymentType + '</td><td>' 	
	+ item.Comments + '</td><td>' 	
	+ item.ReferenceDocuments + '</td><td>' 	
	+ item.ApprovalExpirationDate + '</td><td>' 
	+ item.Description + '</td></tr>';
});

$('#location').append(trHTML);
        
        },
        
        error: function (msg) {
            
            alert(msg.responseText);
        }
    });
})

</script>
```

14. View the page in the web browser. It should be displaying data for one IT Standards record. (Note: should match GEAR_2a.html after this step.)

### Retrieving the ID from the HTTP parameters. (GEAR_2.html)

15. Add the following after the beginning <SCRIPT> tag:

```
function GetURLParameter(sParam)
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) 
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) 
        {
            return sParameterName[1];
        }
    }
}

var ID = GetURLParameter('ID');
```

16. Replace the following line: 		
`url: 'https://dev.ea.gsa.gov/api/v0/itstandards/6041',`

With this line: 		
`url: 'https://dev.ea.gsa.gov/api/v0/itstandards/' +  ID,`

### Passing ID from list page to subpage in URL (GEAR_1.html)

17. Open the GEAR_1.html file in the text editor. 
Replace this line:`trHTML += '<tr><td>'` 
With this line: `trHTML += '<tr><td><a href="GEAR_2.html?ID=' + item.ID + '">' `

Save the file.

18. In the browser, refresh "Gear_1.html". You should see clickable links on each ID value. 

19. Click one of the links, the Gear_2.html page should display values for the link that you clicked on the previous page.  (Note: at this point, the files will look like GEAR_1c.html and GEAR_2b.html.)


### Adding Breadcrumbs (GEAR_1.html)

20. Add the following near the top of the <BODY> directly after the `<section id="contents">`:

```
	<section id="breadcrumbs">
		<ol class="breadcrumb">
			<li class="breadcrumb-item active"><a href="GEAR_1.html">Home</a></li>
		</ol>
	</section>
```

### Adding Breadcrumbs (GEAR_2.html)

21. Add the following near the top of the <BODY> directly after the `<section id="contents">`:

```
	    <section id="breadcrumbs">
			<ol class="breadcrumb">
				<li class="breadcrumb-item"><a href="GEAR_1.html">Home</a></li>
				<li class="breadcrumb-item active">Details</li>
			</ol>
	</section>
```

22. Refesh both pages. You should see breadcrumb navigation on both pages.

(Note: at this point, the files will look like GEAR_1_Final.html and GEAR_2_Final.html.)	
	
### Extra Credit (After class)

Add a third level of navigation to display all the GSA applications using this IT standard.
- Add a link on the GEAR_2.html page to open GEAR_3.html with an application ID as parameter.
- On GEAR_3.html, call the API endpoint /itstandards/{id}/applications and populate a data table with it.
- Add a third level of breadcrumbs for this page. Here is a reference: https://v4-alpha.getbootstrap.com/components/breadcrumb/
