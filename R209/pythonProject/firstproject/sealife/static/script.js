window.addEventListener("load", function(){
   var title = document.getElementById("t1")
   var scroll_indicator = document.getElementById("scroll_indicator")
   var html = document.getElementById('html')
   var nav = document.querySelectorAll(".nav_link")
   var body = document.body
   var fish = document.getElementById('fish')
   var box = document.querySelectorAll(".box")
   var speed = 2
   var screen_height = window.innerHeight
   var calc = 0
   var RGB = ""
   var projects_scroll_height = 0
   var projects_scroll_pos = 0
   var soi = 0
   

   if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
 		scroll_indicator.innerHTML= "SWIPE UP";
                speed = 2;
	}
   if( !(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) ) {
		speed = 2;
        }
	
  body.onscroll = () => {
    if (window.scrollY <= 1){
      html.style.background="#FFF"
      title.style.color = "#000"
      scroll_indicator.style.color = "#000"
      title.innerHTML = "Hello"
      nav.forEach(link => {
        link.style.color = "#000";
      });
    }
    if ((window.scrollY/speed > 1) && (window.scrollY/speed <= 255)){
     RGB = ""
     calc = parseInt(255 - window.scrollY/speed).toString(16);if (calc.length == 2){RGB = RGB + calc}else{RGB = RGB + "0" + calc}
     calc = parseInt(255 - window.scrollY/speed * 0.6).toString(16);if (calc.length == 2){RGB = RGB + calc}else{RGB = RGB + "0" + calc}
     calc = parseInt(255 - window.scrollY/speed * 0.4).toString(16);if (calc.length == 2){RGB = RGB + calc}else{RGB = RGB + "0" + calc}
     html.style.background = "#" + RGB

     RGB = ""
     calc = parseInt(window.scrollY/speed - 13).toString(16);if (calc.length == 2){RGB = RGB + calc}else{RGB = RGB + "0" + calc}
     calc = parseInt(window.scrollY/speed * 1.6 - 13).toString(16);if (calc.length == 2){RGB = RGB + calc}if (calc.length == 1){RGB = RGB + "0" + calc}if (calc.length == 3){RGB = RGB + "FF"}
     calc = parseInt(window.scrollY/speed * 1.4 - 13).toString(16);if (calc.length == 2){RGB = RGB + calc}if (calc.length == 1){RGB = RGB + "0" + calc}if (calc.length == 3){RGB = RGB + "FF"}
     title.style.color = "#" + RGB;
     scroll_indicator.style.color = "#" + RGB
     nav.forEach(link => {
      link.style.color = "#" + RGB;
     });


    if (255 - window.scrollY/speed < window.scrollY/speed){title.innerHTML="Welcome to SEALIFE";nav.forEach(link => {link.style.color = "transparent";});scroll_indicator.style.color="transparent"}else{title.innerHTML="Hello";}}
    if (window.scrollY/speed < 255){title.style.transform="translateY(" + 0 + "px)";fish.style.transform="translateX(" + 100 + "vw)"}
    if (window.scrollY/speed > 255){scroll_indicator.style.color="transparent";nav.forEach(link => {link.style.color = "transparent";});title.innerHTML="Welcome to SEALIFE";html.style.background="#006699";title.style.color="#FFF";title.style.transform="translateY(" + - ((window.scrollY/speed - 255)**1.4) + "px)";fish.style.transform="translateX(" + - ((window.scrollY/speed - 160)/35) + "vw)" + "translateY(" + ((window.scrollY/speed - 600)/40) + "vw)";b1.style.transform="translateY(" + - ((window.scrollY/speed - 700)*1.5) + "px)";b2.style.transform="translateY(" + - ((window.scrollY/speed - 900)/2) + "px)";b3.style.transform="translateY(" + - ((window.scrollY/speed - 900)/12) + "px)";b4.style.transform="translateY(" + - ((window.scrollY/speed - 900)*2.5) + "px)";b5.style.transform="translateY(" + - ((window.scrollY/speed - 900)/2) + "px)";b6.style.transform="translateY(" + - ((window.scrollY/speed - 200)/8) + "px)";}
    if ((document.getElementById("About").getBoundingClientRect().y < document.documentElement.clientHeight) && !(document.getElementById("About").getBoundingClientRect().y + 100 > document.documentElement.clientHeight)){document.getElementById("about_text").style.animation="center 1s forwards 1 ease";document.getElementById("about_text2").style.animation="center2 1s forwards 1 ease"}
    if (!(document.getElementById("About").getBoundingClientRect().y < document.documentElement.clientHeight) && (document.getElementById("About").getBoundingClientRect().y > document.documentElement.clientHeight)){document.getElementById("about_text").style.animation="";document.getElementById("about_text2").style.animation=""}


  };
})