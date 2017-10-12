$(document).ready(function() {
    $.ajax({
        //url: "http://rest-service.guides.spring.io/greeting"
		url: "https://testapi2.app.cloud.gov/travel/citypairs/v0/airfares?award_year=2017&origin_airport_abbrev=ABQ&api_key=DEMO_KEY"
		//url: "https://api.gsa.gov/travel/citypairs/v0/airfares?award_year=2017&origin_airport_abbrev=ABQ&api_key=DEMO_KEY"
    }).then(function(data) {
       $('.greeting-id').append(data.message);
       $('.greeting-content').append(data.result[0].ID);
    });
});