var form = document.getElementById("form");

form.addEventListener("submit", (e) => {
  var num1 = document.getElementById("num1");
  var num2 = document.getElementById("num2");
  if (isNaN(num1.value) || isNaN(num2.value)) {
    alert("Both fields should be numbers");
    e.preventDefault();
    return false;
  } else {
    return true;
  }
});
