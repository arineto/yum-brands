var comp_hash = {};
var comp_name;
var comp_icon;

function toggle_competitor(competitor, icon){
	if (competitor.checked){
		var request = {
		    location: map.getCenter(),
		    radius: '50000',
		    query: competitor.name
		};
		
		comp_icon = icon;
		comp_name = competitor.name;
		comp_hash[comp_name] = [];

		service = new google.maps.places.PlacesService(map);
		service.textSearch(request, callback);
	}else{
		array = comp_hash[competitor.name]
		for (i=0; i<array.length; i++){
			array[i].setMap(null);
		}
	}
}

function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    for (var i = 0; i < results.length; i++) {
      var place = results[i];
      createMarker(place.name, place.geometry.location);
    }
  }
}

function createMarker(name, latlng){
	marker = new google.maps.Marker({
		map: map,
		position: latlng,
		title: name,
		icon: comp_icon
	});
	comp_hash[comp_name].push(marker);
}