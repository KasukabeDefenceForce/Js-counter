let plus = document.getElementById("plus");
let minus = document.getElementById("minus");

plus.addEventListener("click", handlePlus);
minus.addEventListener("click", handleMinus);

function handlePlus() {
  let number = document.getElementById("num");
  let result = Number(number.innerText) + 1;
  number.innerText = result;
}

function handleMinus() {
  let number = document.getElementById("num");
  let result = Number(number.innerText) - 1;
  number.innerText = result;
}
