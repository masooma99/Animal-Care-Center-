const add_to_cart_buttons = document.querySelectorAll(".add_to_cart_button")
console.log(add_to_cart_buttons)
console.log("add to cart js file is open")

function addToCart(event) {
  event.preventDefault() // Prevent form submission if needed
  const button = event.target
  const productId = button.getAttribute("data-product-id")
  const name = button.getAttribute("data-name")
  const price = button.getAttribute("data-price")

  let cart = JSON.parse(localStorage.getItem("cart")) || []

  let existingItem = cart.find((item) => item.id === productId)

  if (existingItem) {
    existingItem.quantity = (existingItem.quantity || 1) + 1
  } else {
    cart.push({ id: productId, name, price, quantity: 1 })
  }

  localStorage.setItem("cart", JSON.stringify(cart))
  console.log(cart)
}

add_to_cart_buttons.forEach((button) => {
  button.addEventListener("click", addToCart)
})
