let ski = document.getElementById('ski');
let jett = document.getElementById('jet');

window.addEventListener('scroll',function () {

    let value = window.scrollY;
    ski.style.bottom = value * 0.1 + 'px';
    jett.style.bottom = value * 0.1 + 'px';

})
