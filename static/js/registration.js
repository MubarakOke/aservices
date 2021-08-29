$(document).ready(function(){

var current_fs, next_fs, previous_fs; //fieldsets
var opacity;
var current = 1;
var steps = $("fieldset").length;
setProgressBar(current);

$('.fileInp').on('change', function(){

  let file= document.querySelector('.fileInp');

  if (/\.(jpe?g|png|gif|pdf|gif|png|jpeg)$/i.test(file.files[0].name) === false ) {
    alert("upload an image or pdf!");
    console.log(file.files.length);
    file.value=null;
    console.log(file.files.length);
    let label= document.querySelector(".fileLab");
    label.innerHTML= "select file...";
  }
  else{
  const size= (this.files[0].size/1024/1024).toFixed(2);
      if(size>5){
        alert("File must be less than 5 MB");
        console.log(file.files.length);
        file.value= null
        console.log(file.files.length);
        let label= document.querySelector(".fileLab");
        label.innerHTML= "select file...";
      }
      else{
        let label= document.querySelector(".fileLab");
        let fileName= document.getElementById("File").files[0].name;
        label.innerHTML= fileName;

        let label1= document.querySelector(".output1");
        label1.innerHTML= "file size: " + size + " MB";
        console.log(file.files.length);
      }}
});









$('.imageInp').on('change', function(){
  const size= (this.files[0].size/1024/1024).toFixed(2);
  if(size>5){
    alert("File must be less than 5 MB");
  }
  else{
  let label= document.querySelector(".imgLab");
  let fileName= document.getElementById("Image").files[0].name;
  console.log(fileName);
  label.innerHTML= fileName;
  let label1= document.querySelector(".output2");
  label1.innerHTML= "file size: " + size + " MB";
}
})


$(".next").click(function(){

current_fs = $(this).parent();
next_fs = $(this).parent().next();

//Add Class Active
$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

//show the next fieldset
next_fs.show();
//hide the current fieldset with style
current_fs.animate({opacity: 0}, {
step: function(now) {
// for making fielset appear animation
opacity = 1 - now;

current_fs.css({
'display': 'none',
'position': 'relative'
});
next_fs.css({'opacity': opacity});
},
duration: 500
});
setProgressBar(++current);
});

$(".previous").click(function(){

current_fs = $(this).parent();
previous_fs = $(this).parent().prev();

//Remove class active
$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

//show the previous fieldset
previous_fs.show();

//hide the current fieldset with style
current_fs.animate({opacity: 0}, {
step: function(now) {
// for making fielset appear animation
opacity = 1 - now;

current_fs.css({
'display': 'none',
'position': 'relative'
});
previous_fs.css({'opacity': opacity});
},
duration: 500
});
setProgressBar(--current);
});

function setProgressBar(curStep){
var percent = parseFloat(100 / steps) * curStep;
percent = percent.toFixed();
$(".progress-bar")
.css("width",percent+"%")
}

$(".submit").click(function(){
return false;
})

});
