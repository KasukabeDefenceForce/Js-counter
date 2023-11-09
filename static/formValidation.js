/** FORM VALIDATION */
let form = document.getElementById("form");
let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  validateInputs();
});

function validateInputs() {
  const first_num = Number(num1.value.trim());
  const second_num = Number(num2.value.trim());
}

function setError(inut, message) {}

function setSuccess(input, message) {}
