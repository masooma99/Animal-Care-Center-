console.log("it works")
// const tableData = JSON.parse(document.getElementById("data-json").textContent)
// console.log(tableData)
const myForm = document.getElementById("signup_id")

myForm.name.addEventListener("change", () => {
  console.log(myForm.name.value)
  console.log(myForm.confirmPassword.value)
})

myForm.button.addEventListener("click", () => {
  console.log(myForm.name.value)
})
