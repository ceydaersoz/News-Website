const toggle = document.querySelector('#toggleDark');
const body = document.querySelector('body');
const footer = document.querySelector('footer');
const h1 = document.querySelector('h1');
const copyrightText = document.querySelector('.copyrightText');
const sec = document.querySelector('.sec');
const crd = document.querySelector('.crd');
const prd = document.querySelector('.prd');
toggle.addEventListener('click', function(){
    this.classList.toggle('bi-moon');
    if(this.classList.toggle('bi-brightness-high-fill')){
        body.style.background = 'white';
        body.style.color = 'black';
        body.style.transition = '2s';
        footer.style.background = 'white';
        footer.style.color = 'black';
        footer.style.transition = '2s';
        h1.style.background = 'white';
        h1.style.color = 'black';
        h1.style.transition = '2s';
        copyrightText.style.background = 'white';
        copyrightText.style.color = 'black';
        copyrightText.style.transition = '2s';
        crd.style.background = 'white';
        crd.style.color = 'black';
        crd.style.transition = '2s';
        prd.style.background = 'white';
        prd.style.color = 'black';
        prd.style.transition = '2s';
        
    }
    else{
        body.style.background = 'black';
        body.style.color = 'white';
        body.style.transition = '2s';
        footer.style.background = 'black';
        footer.style.color = 'white';
        footer.style.transition = '2s';
        h1.style.background = 'black';
        h1.style.color = 'white';
        h1.style.transition = '2s';
        copyrightText.style.background = 'black';
        copyrightText.style.color = 'white';
        copyrightText.style.transition = '2s';
        crd.style.background = 'black';
        crd.style.color = 'white';
        crd.style.transition = '2s';
        prd.style.background = 'black';
        prd.style.color = 'white';
        prd.style.transition = '2s';
        
    }
})

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  var scrollToTopBtn = document.getElementById("scrollToTop");

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
}

function scrollToTop() {
  document.body.scrollTop = 0; // Safari
  document.documentElement.scrollTop = 0; // Diğer tarayıcılar
}

