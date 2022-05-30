//reload

/* NAVBAR */
var main = document.querySelector('.header');
var nav = document.querySelector('.nav');

var offset = main.offsetHeight-nav.offsetHeight;
var prevScrollpos = window.pageYOffset;
/* NAVBAR */
window.onscroll = function(){
    
    if(window.pageYOffset>offset){
        
        nav.classList.remove('bottom-nav');
        nav.classList.add('top-nav');

        var currentScrollPos = window.pageYOffset;
        if (prevScrollpos > currentScrollPos) {
            document.getElementById("navbar").style.top = "0";
        } else {
            document.getElementById("navbar").style.top = "-50px";
        }
        prevScrollpos = currentScrollPos;
        
    }else{

        nav.classList.add('bottom-nav');
        nav.classList.remove('top-nav')
        document.getElementById("navbar").style.top = "";

    }
}