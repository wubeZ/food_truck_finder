

var SearchDiv = document.getElementById('truck-search-button')

if (SearchDiv){
    
    SearchDiv.addEventListener('click', function() {
        var searchInput = document.getElementById('search-input').value;
        console.log(searchInput);
        if (!searchInput) {
            alert("Please enter a search term");
            return;
        }
        window.location.href = '/search?search=' + searchInput;
    });

};