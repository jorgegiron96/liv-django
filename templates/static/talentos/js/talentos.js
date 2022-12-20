function display_uxd(){
    uxd = document.getElementById('uxd_items')
    uid = document.getElementById('uid_items')
    uxw = document.getElementById('uxw_items')
    all = document.getElementById('all_items')
    uxd.style.display = 'block'
    uid.style.display = 'none'
    uxw.style.display = 'none'
    all.style.display = 'none'
}


function display_uxw(){
    uxd = document.getElementById('uxd_items')
    uid = document.getElementById('uid_items')
    uxw = document.getElementById('uxw_items')
    all = document.getElementById('all_items')
    uxd.style.display = 'none'
    uid.style.display = 'block'
    uxw.style.display = 'none'
    all.style.display = 'none'
}
    

function display_uid(){
    uxd = document.getElementById('uxd_items')
    uid = document.getElementById('uid_items')
    uxw = document.getElementById('uxw_items')
    uxd.style.display = 'none'
    uid.style.display = 'none'
    uxw.style.display = 'block'
    all.style.display = 'none'
}

function display_all(){
    uxd = document.getElementById('uxd_items')
    uid = document.getElementById('uid_items')
    uxw = document.getElementById('uxw_items')
    all = document.getElementById('all_items')
    uxd.style.display = 'none'
    uid.style.display = 'none'
    uxw.style.display = 'none'
    all.style.display = 'block'
}