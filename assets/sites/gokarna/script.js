var images=[
  "DSC_0318.jpg",
  "DSC_0367.jpg",
  "DSC_0368.jpg",
  "DSC_0375.jpg",
  "DSC_0385.jpg",
  "DSC_0392.jpg",
  "DSC_0404.jpg",
  "DSC_0431.jpg",
  "DSC_0435.jpg",
  "DSC_0441.jpg",
  "DSC_0451.jpg",
  "DSC_0468.jpg",
  "DSC_0469.jpg",
  "DSC_0471.jpg",
  "DSC_0479.jpg",
  "DSC_0488.jpg",
  "DSC_0514.jpg",
  "DSC_0519.jpg",
  "DSC_0536.jpg",
  "DSC_0550.jpg",
  "DSC_0555.jpg",
  "DSC_0566.jpg"
  
];


var img1,end,j;
for (i=0;i<4;i++){
  div1=document.createElement("div");
  div1.setAttribute("class","column");
  j=i*4;
  end=j+4;
  for(;j<end;j++){
  img1=document.createElement("img");
  img1.src="../../images/Gokarna/"+images[j];
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
  img1.src="../../images/Gokarna/"+images[i];
  img1.setAttribute("id",i);
  img1.setAttribute("width","100%");
  img1.setAttribute("height","100%");
  div1.append(img1);
  document.getElementById("modalcontent").append(div1);
}


