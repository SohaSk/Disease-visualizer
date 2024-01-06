let signup = document.querySelector(".signup");

let login = document.querySelector(".login");

let formSection = document.querySelector(".form-section");


signup.addEventListener("click", () => {


    formSection.classList.add("form-section-move");
});


login.addEventListener("click", () => {


    formSection.classList.remove("form-section-move");
});