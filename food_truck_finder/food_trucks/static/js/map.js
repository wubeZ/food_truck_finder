// Ensure the document is ready before initializing the map
document.addEventListener('DOMContentLoaded', function () {
    // Get the map container
    var mapContainer = document.getElementById('map');

    var foodTruckDataDiv = document.getElementById('food-truck-data');
    if (foodTruckDataDiv){
        var foodTruckName = foodTruckDataDiv.getAttribute('data-name');
        var foodTruck_location_description = foodTruckDataDiv.getAttribute('data-loc-description');
        var latitude = parseFloat(foodTruckDataDiv.getAttribute('data-lat')); 
        var longitude = parseFloat(foodTruckDataDiv.getAttribute('data-lng'));
    }

    // Check if the map container exists
    if (mapContainer) {
        // Initialize the map
        var map = L.map('map',{
            minZoom: 2,
            maxBounds: L.latLngBounds([-90, -180], [90, 180]), // Set the map's max bounds
            maxBoundsViscosity: 1.0, // Set the max bounds viscosity
         });

        // Create an array to hold marker coordinates
        var markerCoordinates = [
            [latitude, longitude] // Food truck marker coordinates
        ];

        var truckIcon = L.icon({
            iconUrl: "https://raw.githubusercontent.com/wubeZ/food_truck_finder/main/food_truck_finder/food_trucks/static/images/taco-truck.png?token=GHSAT0AAAAAACASNZN5KYSBPSHU7LYEZ472ZPYTMAA",
            iconSize: [30, 35], // size of the icon
            popupAnchor: [-3, -14] // point from which the popup should open relative to the iconAnchor
        });


        // Add the food truck marker to the map
        var foodTruckMarker = L.marker([latitude, longitude], {icon: truckIcon}).addTo(map).bindPopup(`<b>${ foodTruckName }</b>`).openPopup();

        // Zoom in when clicking on the food truck marker
        foodTruckMarker.on('click', function() {
            map.setView([latitude, longitude], 16);
        });

        // Check if the user's location is available
        navigator.geolocation.getCurrentPosition(function (position) {
            var userLat = position.coords.latitude;
            var userLng = position.coords.longitude;

            // Add the user's location to the marker coordinates array
            markerCoordinates.push([userLat, userLng]);

            // Create a bounds object based on marker coordinates
            var bounds = L.latLngBounds(markerCoordinates);

            // Fit the map to the bounds
            map.fitBounds(bounds);

            var UserMarker = L.marker([userLat, userLng]).addTo(map);
            UserMarker.bindPopup(`<b> Your Location </b>`).openPopup();

            // Zoom in when clicking on the user marker
            UserMarker.on('click', function() {
                map.setView([userLat, userLng], 16);
            });


            // Add a tile layer
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
        });
    }

     
    // Get the location button element
    var location_btn = document.getElementById('location-button')
    
    // Check if the location button exists
    if (location_btn){
        location_btn.addEventListener('click', function() {
            // Check if geolocation is supported by the browser
        if (navigator.geolocation) {
            
            navigator.geolocation.getCurrentPosition(function (position) {
                var latitude = position.coords.latitude;
                var longitude = position.coords.longitude;
    
                // Redirect to the search by location page
                window.location.href = '/searchByLoc?latitude=' + latitude + '&longitude=' + longitude;
            });
        } else {
            console.error('Geolocation is not supported by your browser');
            alert("Geolocation is not supported by your browser")
        }
        });
    }

});

