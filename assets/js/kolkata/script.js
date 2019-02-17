var images=[
  "DSC_0034.JPG",
  "DSC_0037.JPG",
  "DSC_0062.JPG",
  "DSC_0131.JPG",
  "DSC_0156.JPG",
  "DSC_0179.JPG",
  "DSC_0183.JPG",
  "DSC_0200.JPG",
  "DSC_0211.JPG",
  "DSC_0366.JPG",
  "DSC_0383.JPG",
  "DSC_0396.JPG",
  "DSC_0967.JPG",
  "DSC_0436.JPG",
  "DSC_0450.JPG",
  "DSC_0400.JPG"
];


var img1,end,j;
for (i=0;i<4;i++){
  div1=document.createElement("div");
  div1.setAttribute("class","column");
  j=i*4;
  end=j+4;
  for(;j<end;j++){
  img1=document.createElement("img");
  img1.src="../../assets/images/kolkata/"+images[j];
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
  img1.src="../../assets/images/kolkata/"+images[i];
  img1.setAttribute("id",i);
  img1.setAttribute("width","100%");
  img1.setAttribute("height","100%");
  div1.append(img1);
  document.getElementById("modalcontent").append(div1);
}


