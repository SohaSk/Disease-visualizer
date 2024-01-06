var value = document.getElementById("SearchInput").value;
localStorage.setItem("searchValue", value);
window.addEventListener('scroll', function() {
    var button = document.getElementById('dashboard');
    if (window.scrollY + window.innerHeight >= document.body.scrollHeight) {
        button.style.display = 'block';
    } else {
        button.style.display = 'none';
    }
});