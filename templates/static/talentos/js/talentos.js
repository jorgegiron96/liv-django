
var csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

var filterBtns = document.querySelectorAll('.filter-btn');
filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function() {
        console.log(btn.id);
        
        var filterParams = {'id': btn.id}
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'filter-items/'+filterParams.id+'/');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('X-CSRFToken', csrf_token);
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log('opa')
            }
        };
        xhr.send(JSON.stringify(filterParams))
    });
});