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
        var map = L.map('map');

        // Create an array to hold marker coordinates
        var markerCoordinates = [
            [latitude, longitude] // Food truck marker coordinates
        ];

        // Add the food truck marker to the map
        var foodTruckMarker = L.marker([latitude, longitude]).addTo(map).bindPopup(`<b>${ foodTruckName }</b><br>${ foodTruck_location_description }`).openPopup();

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

    // AJAX request to send coordinates to the Django view
    var location_btn = document.getElementById('location-button')
    
    if (location_btn){
        location_btn.addEventListener('click', function() {
            // Check if geolocation is supported by the browser
        if (navigator.geolocation) {
            
            navigator.geolocation.getCurrentPosition(function (position) {
                var latitude = position.coords.latitude;
                var longitude = position.coords.longitude;
    
                window.location.href = '/searchByLoc?latitude=' + latitude + '&longitude=' + longitude;
            });
        } else {
            console.error('Geolocation is not supported by your browser');
            alert("Geolocation is not supported by your browser")
        }
        });
    }

});

