function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000//get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations1");
            $('#uiLocations1').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations1').append(opt);
            }

            var uiLocations = document.getElementById("uiLocations2");
            $('#uiLocations2').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations2').append(opt);
            }
        }
    });

    var url = "http://127.0.0.1:5000//get_airline_names";
    $.get(url,function(data, status) {
        console.log("got response for get_airline_names request");
        if(data) {
            var airlines = data.airlines;
            var uiairlines = document.getElementById("uiairlines");
            $('#uiairlines').empty();
            for(var i in airlines) {
                var opt = new Option(airlines[i]);
                $('#uiairlines').append(opt);
            }
        }
    });
  }
function getStopsValue() {
    var uistops = document.getElementsByName("uistops");
    for(var i in uistops) {
      if(uistops[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
function getClassValue() {
    var uiclasses = document.getElementsByName("uiclasses");
    for(var i in uiclasses) {
      if(uiclasses[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  } 

  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var day = document.getElementById("uidate");
    var Stops = getStopsValue();
    var Class = getClassValue();
    var destination = document.getElementById("uiLocations2");
    var departure = document.getElementById("uiLocations1");
    var airline = document.getElementById("uiairlines");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_flight_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        airline: airline.value,
        Class: Class,
        destination: destination.value,
        departure: departure.value,
        day:day.value,
        stops: Stops
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " rupees</h2>";
        console.log(status);
    });
  }
  window.onload = onPageLoad;