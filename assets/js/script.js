var images=[
  "DSC_0318.jpg",
  "DSC_0333.jpg",
  "DSC_0368.jpg",
  "DSC_0375.jpg",
  "DSC_0383.jpg",
  "DSC_0385.jpg",
  "DSC_0386.jpg",
  "DSC_0390.jpg",
  "DSC_0397.jpg",
  "DSC_0404.jpg",
  "DSC_0422.jpg",
  "DSC_0431.jpg",
  "DSC_0434.jpg",
  "DSC_0435.jpg",
  "DSC_0441.jpg",
  "DSC_0443.jpg",
  "DSC_0451.jpg",
  "DSC_0468.jpg",
  "DSC_0469.jpg",
  "DSC_0471.jpg"
];


var img1,end,j;
for (i=0;i<5;i++){
  div1=document.createElement("div");
  div1.setAttribute("class","column");
  j=i*3;
  end=j+3;
  for(;j<end;j++){
  img1=document.createElement("img");
  img1.src="assets/images/Gokarna/"+images[j];
  img1.setAttribute("width","100%");
  img1.setAttribute("class","hover-shadow");
  img1.setAttribute("onclick","openModal();currentSlide("+j+")");
  div1.append(img1);
  }
  document.getElementById("photogrid").append(div1);  
}

for (i=0;i<images.length;i++){
  div1=document.createElement("div");
  div1.setAttribute("class","mySlides");
  img1=document.createElement("img");
  img1.src="assets/images/Gokarna/"+images[i];
  img1.setAttribute("id",i);
  img1.setAttribute("width","100%");
  img1.setAttribute("height","100%");
  div1.append(img1);
  document.getElementById("modalcontent").append(div1);
}




