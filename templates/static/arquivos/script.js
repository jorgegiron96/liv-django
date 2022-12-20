const allFilterItems = document.querySelectorAll('.filter-item');
const allFilterBtns = document.querySelectorAll('.filter-btn');

window.addEventListener('DOMContentLoaded', () => {
    allFilterBtns[0].classList.add('active-btn');
});

allFilterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
        showFilteredContent(btn);
    });
});

function showFilteredContent(btn){
    allFilterItems.forEach((item) => {
        if(item.classList.contains(btn.id)){
            resetActiveBtn();
            btn.classList.add('active-btn');
            item.style.display = "block";
        } else {
            item.style.display = "none";
        }
    });
}

function resetActiveBtn(){
    allFilterBtns.forEach((btn) => {
        btn.classList.remove('active-btn');
    });
}
/* Moodal Overlay */
const handleClickOutside = (event) => {
    let overlay = document.getElementById("overlay");
    let modal = document.getElementById("modal");
    if (!modal.contains(event.target)) {
        modal.style.display = 'none';
        overlay.style.display = 'none';
        document.removeEventListener('click', handleClickOutside, false);
    }
}

const openModal = () => {
    let overlay = document.getElementById("overlay");
    let modal = document.getElementById("modal");
    overlay.style.display = 'flex'
    modal.style.display = 'flex'
    setTimeout(() => { document.addEventListener('click', handleClickOutside, false) }, 200);
}
/* Moodal Overlay 2 */
const handleClickOutside2 = (event) => {
    let overlay2 = document.getElementById("overlay2");
    let modal2 = document.getElementById("modal2");
    if (!modal2.contains(event.target)) {
        modal2.style.display = 'none';
        overlay2.style.display = 'none';
        document.removeEventListener('click', handleClickOutside2, false);
    }
}
const openModal2 = () => {
    let overlay2 = document.getElementById("overlay2");
    let modal2 = document.getElementById("modal2");
    overlay2.style.display = 'flex'
    modal2.style.display = 'flex'
    setTimeout(() => { document.addEventListener('click', handleClickOutside2, false) }, 200);

}


/* Moodal Overlay 3 */
const handleClickOutside3 = (event) => {
    let overlay3 = document.getElementById("overlay3");
    let modal3 = document.getElementById("modal3");
    if (!modal3.contains(event.target)) {
        modal3.style.display = 'none';
        overlay3.style.display = 'none';
        document.removeEventListener('click', handleClickOutside3, false);
    }
}
const openModal3 = () => {
    let overlay3 = document.getElementById("overlay3");
    let modal3 = document.getElementById("modal3");
    overlay3.style.display = 'flex'
    modal3.style.display = 'flex'
    setTimeout(() => { document.addEventListener('click', handleClickOutside3, false) }, 200);
}
