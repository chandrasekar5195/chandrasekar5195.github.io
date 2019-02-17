function openModal() {
    document.getElementById('myModal').style.display = "block";
  }
  
function closeModal() {
    document.getElementById('myModal').style.display = "none";
  }
  
var slideIndex = 1;      
showSlides(slideIndex);
  
function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  
function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    if (n > slides.length-1) {slideIndex = 0}
    if (n < 0) {slideIndex = slides.length-1}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex].style.display = "table";
    img_height=document.getElementById(slideIndex).naturalHeight;
    img_width=document.getElementById(slideIndex).naturalWidth;
    if (img_height > img_width) {
      document.getElementById("modalcontent").setAttribute("style","max-width: 400px");

    }
    if (img_height < img_width) {
      document.getElementById("modalcontent").setAttribute("style","max-width: 900px");

    }  

  
  }