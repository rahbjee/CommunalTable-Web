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

console.log(Date.parse(sampleEvent['date']).toString('MMMM dS'), Date.parse(sampleEvent['time']).toString("h:mm tt"));

var infoWindowContent = '<div id="infowindow">' +
                          '<h6>' + sampleEvent['name'] + '</h6>' +
                          '<p class="mb-1"><strong>' + Date.parse(sampleEvent['date']).toString('MMMM dS')
                                + " " + Date.parse(sampleEvent['time']).toString("h:mm tt") + '</strong></p>' +
                          '<p class="mb-2">' + sampleEvent['price'] + ' or other</p>' +
                          '<p class="mb-1"><em>' + sampleEvent['sDes'] + '</em></p>' +
                        '</div>';




var map, infoWindow;

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

  infoWindow = new google.maps.InfoWindow;
  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      infoWindow.setPosition(pos);
      infoWindow.setContent('You are here');
      //infoWindow.open(map);
      map.setCenter(pos);

      var marker = new google.maps.Marker({
        position: pos,
        icon: circle,
        map: map
      });
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation

    handleLocationError(false, infoWindow, map.getCenter());
  }


  //add markers to events

  var eventMarker1 = new google.maps.Marker({position: sampleEvent['pos'], map: map});

  var eventWindow1 = new google.maps.InfoWindow({
    content: infoWindowContent,
    maxWidth: 250,
    zIndex: 2,
  });

  eventMarker1.addListener('mouseover', function() {
    eventWindow1.open(map, eventMarker1);
  });

  eventMarker1.addListener('click', function() {
    map.panTo(eventMarker1.getPosition());

    $( "#eventName" ).html("Updated");

    $( ".sidebar" ).animate({
      left: "0px",
    }, 500 );
  });

  var eventMarker2 = new google.maps.Marker({position: nq, map: map});


  eventMarker2.addListener('mouseover', function() {
    eventWindow1.open(map, eventMarker2);
  });

  eventMarker2.addListener('click', function() {
    map.panTo(eventMarker2.getPosition());

    $( "#eventName" ).html("Updated");

    $( ".sidebar" ).animate({
      left: "0px",
    }, 500 );

  });

  $( "#map" ).on( "click", "#infowindow", function( event ) {
    event.preventDefault();
    map.panTo(eventWindow1.getPosition());

    $( "#eventName" ).html("Updated");

    $( ".sidebar" ).animate({
      left: "0px",
    }, 500 );



  });

}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');

  infoWindow.open(map);

}

$( ".sidebar" ).on( "click", ".close", function( event ) {
    event.preventDefault();

    $( ".sidebar" ).animate({
    left: "-500px",
  }, 500 );
});
