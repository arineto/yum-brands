var comp_hash = {};
var comp_name;
var comp_icon;
var comp_window;


function toggle_competitor(competitor, icon){
	if (competitor.checked){
		comp_name = competitor.name;
		comp_icon = icon;
		comp_hash[comp_name] = [];
		var latitude = map.getCenter().lat()
		var longitude = map.getCenter().lng()
		get_data(comp_name, latitude, longitude, 1);
	}else{
		array = comp_hash[competitor.name]
		for (i=0; i<array.length; i++){
			array[i].setMap(null);
		}
	}
}


function createMarker(name, address, latitude, longitude){
	var latlng = new google.maps.LatLng(latitude, longitude);
	var comp_marker;

	comp_marker = new google.maps.Marker({
		map: map,
		position: latlng,
		title: name,
		icon: comp_icon
	});

	google.maps.event.addListener(comp_marker, 'click', function () {
		if(comp_window){
			comp_window.setMap(null);
		}
		comp_window = new google.maps.InfoWindow({
			content: "<p>"+name+"</p><p>"+address.street+"</p>"
		})
		comp_window.open(map, comp_marker);
	});
	comp_hash[comp_name].push(comp_marker);
}


function get_data(name, latitude, longitude, page){
	var page_count;
	$.get("http://api.sandbox.yellowapi.com/FindBusiness/?what="+name+"&where=cZ"+longitude+","+latitude+
		"&dist=20&sflag=bn&fmt=JSON&pgLen=100&pg="+page+"&apikey=7cv3m6v4nguzxdspkw45wjve&UID=jingham", 
		function(data) {
			var items = data["listings"];
			var i = 0;
			for(i=0; i<items.length; i++){
				createMarker(items[i].name, items[i].address, items[i].geoCode.latitude, items[i].geoCode.longitude);
			}
			page_count = data["summary"].pageCount;
			// alert(page);
		})
		.fail(function () {
			// alert("There was a problem with the server. Try again later.");
			setTimeout(function(){
				get_data(name, latitude, longitude, page);
			}, 1000);
		})
		.always(function (){
			if(page<page_count){
				setTimeout(function(){
					get_data(name, latitude, longitude, page+1);
				}, 500);
			}
		});
}