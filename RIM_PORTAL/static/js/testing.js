function myLoginFunction() {
  var login = document.getElementById("login");
  var register = document.getElementById("register");
  var userDetails = document.getElementById("userDetails");
  login.style.display = "block";
  register.style.display = "none";
  logout.style.display = "none";
  }

  function myRegisterFunction() {
  var login = document.getElementById("login");
  var register = document.getElementById("register");
  var userDetails = document.getElementById("userDetails");
  login.style.display = "none";
  register.style.display = "block";
  logout.style.display = "none";

  }

  function myUserinfoFunction() {
  var login = document.getElementById("login");
  var register = document.getElementById("register");
  var logout = document.getElementById("userDetails");
  userDetails.style.display = "block";
  register.style.display = "none";
  login.style.display = "none";
  }



$('#myselect').on('change', function(){
  $('#myinput').val($(this).val());
})

// init
$('#myselect').change();