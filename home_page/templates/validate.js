function validateEmail() {
    const regexEmail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/

    var email = document.getElementById("email");
    var emailValue = email.value;

    if (!regexEmail.test(emailValue)){
        email.setCustomValidity("this aint lookin like an email")
        return false
    }
    else{
        email.setCustomValidity("")
        return true
    }
}

function validatePass() {
    const regexSpecial = /[\W_]/;
    const regexDigit = /\d/;
    const regexUpper = /[A-Z]/;

    var pass = document.getElementById("passwrd");
    var passValue = pass.value;

    var minLength = false, containSpecial = false, containUpper = false, containDigit = false;

    // Check password: lenght >= 12
    if (passValue.length >= 12) {
        minLength = true;
        document.getElementById("icon1").className = "fa-solid fa-check";
        document.getElementById("req-12-chars").style.color = "#262626";
        document.querySelector("#req-12-chars i").style.color = "#16db65";
    }
    else {
        document.getElementById("icon1").className = "fa-solid fa-xmark";
        document.getElementById("req-12-chars").style.color = "#262626";
        document.querySelector("#req-12-chars i").style.color = "#ff0054";

    }

    // Check password: contain special char
    if (regexSpecial.test(passValue)) {
        containSpecial = true;
        document.getElementById("icon2").className = "fa-solid fa-check";
        document.getElementById("req-special").style.color = "#262626";
        document.querySelector("#req-special i").style.color = "#16db65";
    }
    else {
        document.getElementById("icon2").className = "fa-solid fa-xmark";
        document.getElementById("req-special").style.color = "#262626";
        document.querySelector("#req-special i").style.color = "#ff0054";

    }

    // Check password: contain uppercase letter
    if (regexUpper.test(passValue)) {
        containUpper = true;
        document.getElementById("icon3").className = "fa-solid fa-check";
        document.getElementById("req-upper").style.color = "#262626";
        document.querySelector("#req-upper i").style.color = "#16db65";
    }
    else {
        document.getElementById("icon3").className = "fa-solid fa-xmark";
        document.getElementById("req-upper").style.color = "#262626";
        document.querySelector("#req-upper i").style.color = "#ff0054";
    }

    // Check password: contain digit
    if (regexDigit.test(passValue)) {
        containDigit = true;
        document.getElementById("icon4").className = "fa-solid fa-check";
        document.getElementById("req-digit").style.color = "#262626";
        document.querySelector("#req-digit i").style.color = "#16db65";
    }
    else {
        document.getElementById("icon4").className = "fa-solid fa-xmark";
        document.getElementById("req-digit").style.color = "#262626";
        document.querySelector("#req-digit i").style.color = "#ff0054";
    }

    if (!(minLength && containSpecial && containUpper && containDigit))
        pass.setCustomValidity("please respect the reqs");
    else
        pass.setCustomValidity("");


}

function confirmPass() {

    var pass = document.getElementById("passwrd");
    var passConf = document.getElementById("passwrd-conf");

    var passValue = pass.value
    var passConfValue = passConf.value

    if (passValue !== passConfValue)
        passConf.setCustomValidity("don't match")
    else
        passConf.setCustomValidity("")
}

function validInputs(){
    if(validateEmail() === true){
        document.getElementById("email").style.border = "2px solid 0496ff"
    }
    else
        console.log("nok email")

}

