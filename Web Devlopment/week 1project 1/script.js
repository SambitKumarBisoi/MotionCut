// Toggle dropdown on button click
document.getElementById("dropdown-btn").addEventListener("click", function() {
    document.getElementById("dropdown-content").classList.toggle("show");
});

// Close dropdown if clicked outside
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

// Update button text when an option is selected
var links = document.querySelectorAll(".dropdown-content a");
links.forEach(function(link) {
    link.addEventListener("click", function(event) {
        var category = event.target.getAttribute("data-category");
        document.getElementById("dropdown-btn").textContent = category;
        document.getElementById("dropdown-content").classList.remove("show");
    });
});
