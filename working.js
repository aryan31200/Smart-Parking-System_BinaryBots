const mymail="johndoe@mail.com";
const mypass="passpasspass";
$('input').keypress(function(event){
  if (event.keyCode === 13) {
    LoginPass();
  }
});
function LoginPass(){
  var email=$('#email').val();
  var pass=$('#pass').val();
  console.log(email,pass);
  if(email===mymail&&pass===mypass){
    location.href = "./mapPage.html";
  }else{
    alert("Wrong username/password");
  }
}

var licenseNo="";
var bookingTime="";
function Book(){
  var email=document.getElementById('license').value;
  var pass=document.getElementById('time').value;
    //route to the booked page
}
