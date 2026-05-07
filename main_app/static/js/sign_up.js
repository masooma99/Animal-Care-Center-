console.log("it works......")
const myForm = document.getElementById("signup_id")
console.log()
// const formValidationButton = document.getElementById("formValidationButton")
myForm.confirmPassword.addEventListener("change", () => {
  console.log(myForm.confirmPassword.value)
  console.log(myForm.password.value)
  console.log(
    myForm.confirmPassword.value === myForm.password.value
      ? "same"
      : "not matching"
  )
})

myForm.button.addEventListener("click", () => {
  // event.preventDefault()
  console.log("button clicked")

  // console.log(myForm.password.value)
  if (
    // myForm.name.value !== "" &&
    // myForm.age.value !== "" &&
    // myForm.image.value !== "" &&
    // myForm.email.value !== "" &&
    // myForm.email.value.includes("@") &&
    myForm.password.value === myForm.confirmPassword.value &&
    myForm.password.value !== ""
  ) {
    console.log("matching")
    console.log(`myForm.password.value: ${myForm.password.value}`)
    myForm.submit()
  } else {
    console.log("not matching or you didn't fill the rest of the form")
  }
})

// -----------------------------------------------------------------------

// console.log("it works")
// // const tableData = JSON.parse(document.getElementById("data-json").textContent)
// // console.log(tableData)
// const myForm = document.getElementById("signup_id")

// myForm.name.addEventListener("change", () => {
//   console.log(myForm.name.value)
//   console.log(myForm.confirmPassword.value)
// })

// myForm.button.addEventListener("click", () => {
//   console.log(myForm.name.value)
// })
