let login = document.querySelector(".login");

let formSection = document.querySelector(".form-section");

var username=document.forms['form']['username'];
var password=document.forms['form']['password'];
var username_error=document.getElementById('username_error');
var pass_error=document.getElementById('pass_error');

function validated(){
if(username.value.length<9){
   username.style.border='ipx solid red';
   username_error.style.display='block';
   username.focus();
   return false
   }}


