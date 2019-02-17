var images=[
  "DSC_0422.jpg",
  "DSC_0513.jpg",
  "DSC_0774.jpg",
  "DSC_0530.jpg",
  "DSC_0532.jpg",
  "DSC_0535.jpg",
  "DSC_0544.jpg",
  "DSC_0574.jpg",
  "DSC_0597.jpg",
  "DSC_0613.jpg",
  "DSC_0681.jpg",
  "DSC_0690.jpg",
  "DSC_0695.jpg",
  "DSC_0767.jpg",
  "DSC_0769.jpg",
  "DSC_0772.jpg",

  "DSC_0780.jpg",
  "DSC_0809.jpg",
  "DSC_0810.jpg"
];


var img1,end,j;
for (i=0;i<4;i++){
  div1=document.createElement("div");
  div1.setAttribute("class","column");
  j=i*4;
  end=j+4;
  for(;j<end;j++){
  img1=document.createElement("img");
  img1.src="../../images/karnataka/"+images[j];
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
  img1.src="../../images/karnataka/"+images[i];
  img1.setAttribute("id",i);
  img1.setAttribute("width","100%");
  img1.setAttribute("height","100%");
  div1.append(img1);
  document.getElementById("modalcontent").append(div1);
}


