var info_window;

function init_map(map){
  var mapOptions = {
    center: new google.maps.LatLng(43.659199, -79.386849),
    zoom: 13
  };
  map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

  google.maps.event.addListener(map, 'click', function (e) {
  });
  return map;
}

