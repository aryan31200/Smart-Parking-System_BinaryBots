const mymail = "johndoe@mail.com";
const mypass = "passpasspass";
$("input#email, input#pass").keypress(function (event) {
  if (event.keyCode === 13) {
    LoginPass();
  }
});

$("input.location-input").keypress(function (event) {
  if (event.keyCode === 13) {
    location.href = "./BookingPage.html";
  }
});
function LoginPass() {
  var email = $("#email").val();
  var pass = $("#pass").val();
  console.log(email, pass);
  if (email === mymail && pass === mypass) {
    location.href = "./mapPage.html";
  } else {
    alert("Wrong username/password");
  }
}

function mapLocation() {
  var locationName = $(".location-input").value();
}

$("input.license-number").on("click", function () {
  $(this).select();
});
var todayDate = new Date().toISOString().slice(0, 10);
$("input[type=date]").val(todayDate);

var licenseNo = "";
var bookingTime = "";
function Book() {
  location.href = "./Booked.html";
}
function ConfirmedEntry() {
  location.href = "./pay.html";
}
function Payment() {
  $(".loginbutton-payment").css("background-color", "#ff8533");
}
