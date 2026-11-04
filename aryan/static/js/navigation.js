function toggleDisplay(element) {
    element.style.display =
        element.style.display === "block" ? "none" : "block";
}

document.getElementById("moreToggle")?.addEventListener("click", function () {
    toggleDisplay(document.getElementById("moreMenu"));
});

function toggleSearch() {
    const searchBox = document.getElementById("searchBox");
    const overlay = document.getElementById("overlay");
    const isOpen = searchBox.style.display === "block";

    searchBox.style.display = isOpen ? "none" : "block";
    overlay.style.display = isOpen ? "none" : "block";
}

document.getElementById("desktopSearchToggle")?.addEventListener("click", toggleSearch);
document.getElementById("mobileSearchToggle")?.addEventListener("click", toggleSearch);

document.getElementById("mobileMenuToggle")?.addEventListener("click", function () {
    toggleDisplay(document.getElementById("mobileLinks"));
});

document.getElementById("overlay")?.addEventListener("click", function () {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("searchBox").style.display = "none";
});