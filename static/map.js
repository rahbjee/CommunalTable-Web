
console.log(mealList);

var sampleEvent = {
  name: "Korean BBQ Movie Night",
  date: "2019-04-18",
  time: "18:00:00",
  sDes: "Spicy pork with rice and side dishes",
  price: "$7",
  comp: ["dessert", "drink"],
  seat: 8,
  addr: "2150 Cram Pl, Ann Arbor, MI 48105",
  pos: {lat: 42.296946, lng: -83.717452}
};

var map, infoWindow, geoWindow;

function initMap() {

  var styles = {
        default: null,
        silver: [
          {
            elementType: 'geometry',
            stylers: [{color: '#f5f5f5'}]
          },
          {
            elementType: 'labels.icon',
            stylers: [{visibility: 'off'}]
          },
          {
            elementType: 'labels.text.fill',
            stylers: [{color: '#616161'}]
          },
          {
            elementType: 'labels.text.stroke',
            stylers: [{color: '#f5f5f5'}]
          },
          {
            featureType: 'administrative.land_parcel',
            elementType: 'labels.text.fill',
            stylers: [{color: '#bdbdbd'}]
          },
          {
            featureType: 'poi',
            elementType: 'geometry',
            stylers: [{color: '#eeeeee'}]
          },
          {
            featureType: 'poi',
            elementType: 'labels.text.fill',
            stylers: [{color: '#757575'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'geometry',
            stylers: [{color: '#e5e5e5'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'labels.text.fill',
            stylers: [{color: '#9e9e9e'}]
          },
          {
            featureType: 'road',
            elementType: 'geometry',
            stylers: [{color: '#ffffff'}]
          },
          {
            featureType: 'road.arterial',
            elementType: 'labels.text.fill',
            stylers: [{color: '#757575'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'geometry',
            stylers: [{color: '#dadada'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'labels.text.fill',
            stylers: [{color: '#616161'}]
          },
          {
            featureType: 'road.local',
            elementType: 'labels.text.fill',
            stylers: [{color: '#9e9e9e'}]
          },
          {
            featureType: 'transit.line',
            elementType: 'geometry',
            stylers: [{color: '#e5e5e5'}]
          },
          {
            featureType: 'transit.station',
            elementType: 'geometry',
            stylers: [{color: '#eeeeee'}]
          },
          {
            featureType: 'water',
            elementType: 'geometry',
            stylers: [{color: '#c9c9c9'}]
          },
          {
            featureType: 'water',
            elementType: 'labels.text.fill',
            stylers: [{color: '#9e9e9e'}]
          }
        ]
      };

  var circle = {
        path: google.maps.SymbolPath.CIRCLE,
        scale: 8,
        strokeColor: "#EB8800",
        //strokeWeight: 14
      };

  var nq = {lat: 42.280926, lng: -83.739721};


  map = new google.maps.Map(document.getElementById('map'), {
    center: nq,
    zoom: 14,
    styles: styles['silver']
  });

  
  // Try HTML5 geolocation.

  geoWindow = new google.maps.InfoWindow;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      geoWindow.setPosition(pos);
      geoWindow.setContent('You are here');
      //infoWindow.open(map);
      map.setCenter(pos);

      var marker = new google.maps.Marker({
        position: pos,
        icon: circle,
        map: map
      });
    }, function() {
      handleLocationError(true, geoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation

    handleLocationError(false, geoWindow, map.getCenter());
  }


  infoWindow = new google.maps.InfoWindow({
      maxWidth: 250,
      zIndex: 2,
    });

  //for loop to add events to map
  mealList.forEach(function(event){

    var eventMarker = new google.maps.Marker({position: event.pos, map: map});

    var priceHTML;

    if (event.price && event.donations) {
      priceHTML = '$' + event.price.toString() +' or donation';
    } else if (event.price) {
      priceHTML = event.price.toString();
    } else if (event.donations) {
      priceHTML = "Donation";
    }

    var infoWindowHTML = `
      <div id="infowindow">
        <h6>${event.name}</h6>
        <p class="mb-1"><strong>${Date.parse(event.date).toString('MMMM dS')} ${Date.parse(event.time).toString("h:mm tt")}</strong></p>
        <p class="mb-2">${priceHTML}</p>
        <p class="mb-1"><em>${event.des}</em></p>
      </div>`;

    

    eventMarker.addListener('mouseover', function() {

      infoWindow.setContent(infoWindowHTML);
      infoWindow.open(map, eventMarker);
      
    });    

    eventMarker.addListener('click', function(){
      map.panTo(eventMarker.getPosition());
      setSidebarContent(event);

      $( ".sidebar" ).animate({
        left: "0px",
      }, 500 );

    })

  });

  // eventMarker1.addListener('click', function() {
  //   map.panTo(eventMarker1.getPosition());

  //   $( "#eventName" ).html("Updated");

  //   $( ".sidebar" ).animate({
  //     left: "0px",
  //   }, 500 );
  // });

  


  // end for loop

  // $( "#map" ).on( "click", "#infowindow", function( event ) {
  //   event.preventDefault();
  //   map.panTo(infoWindow.getPosition());

  //   //$( "#eventName" ).html("Updated");

  //   $( ".sidebar" ).animate({
  //     left: "0px",
  //   }, 500 );



  // });

}



/////////////////////////////////////////////////////////////////////

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  geoWindow.setPosition(pos);
  geoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');

  geoWindow.open(map);

}

/////////////////////////////////////////////////////////////////////
//close sidebar

$( ".sidebar" ).on( "click", ".close", function( event ) {
    event.preventDefault();

    $( ".sidebar" ).animate({
    left: "-500px",
  }, 500 );
});

/////////////////////////////////////////////////////////////////////
//reset sidebar content

function setSidebarContent(eventData) {
  $( "#eventName" ).html(eventData.name);
  $( "#eventDT" ).html(Date.parse(eventData.date).toString('MMMM dS') + " " + Date.parse(eventData.time).toString("h:mm tt"));
  $( "#eventDes" ).html(eventData.des);

  $( "#eventIng" ).empty();
  for (var ing of eventData.ingredients) {
    $( "#eventIng" ).append($('<li class="list-group-item"></li>').html(ing));
  }

  $( "#eventAlg" ).empty();
  for (var alg of eventData.allergens) {
    $( "#eventAlg" ).append($('<li class="list-group-item"></li>').html(alg));
  }

  $( "#comp" ).empty();
  if (eventData.price) {
    $( "#comp" ).append($('<option></option>').html("$" + eventData.price.toString()));
  } 

  for (var comp of eventData.donations) {
    $( "#comp" ).append($('<option></option>').html(comp));
  }

  $( "#seatsAvailable" ).empty();
  $( "#seatsAvailable" ).html(eventData.seats + " available");



  $( "#seats" ).empty();
  for (var i = 1; i <= eventData.seats; i++) {
    $( "#seats" ).append($('<option></option>').html(i));
  }

}
