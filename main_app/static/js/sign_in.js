const mySignInForm = document.getElementById("signIn_id")
const data = JSON.parse(document.getElementById("my-data-id").textContent)

fetch("/api/get-data/")
  .then((response) => response.json())
  .then((data) => console.log(data))

mySignInForm.validationToSignIn.addEventListener("click", () => {
  event.preventDefault()
  // find user by email in the db
  // find the password --> try to hash password
  // not show the page unless the user is signed in
  // token?
  // access database info
  // mySignInForm.submit()
})
