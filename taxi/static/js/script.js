document.querySelectorAll('.bg-warning a').forEach(function(link) {
    if(link.getAttribute('href') == document.URL){
    link.style.backgroundColor = 'red';
    }
});