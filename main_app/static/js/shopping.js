const add_to_cart_buttons = document.querySelectorAll(".add_to_cart_button")
// console.log(`add_to_cart_buttons:${add_to_cart_buttons}`)
// console.log("add to cart js file is open")
const shoppingDiv = document.getElementById("cart_detail")
const cartButton = document.getElementById("cart_icon") //when clicking on this icon it will display or make display=none for the shopping div

// console.log(shoppingDiv)
// console.log(cartButton)

const renderCart = () => {
  const cart = JSON.parse(localStorage.getItem("cart")) || []
  let cartHTML = "<h3>Shopping Cart</h3>"

  if (cart.length === 0) {
    cartHTML += "<p>Your cart is empty</p>"
  } else {
    cartHTML += "<ul>"
    let total = 0
    cart.forEach((item) => {
      const itemTotal = parseFloat(item.price) * item.quantity
      total += itemTotal
      cartHTML += `
        <li>
          <strong>${item.name}</strong> x${item.quantity}
          <br>Price: $${item.price} each = $${itemTotal.toFixed(2)}
          <button onclick="removeFromCart('${item.id}')">Remove</button>
        </li>
      `
    })
    cartHTML += "</ul>"
    cartHTML += `<h4>Total: $${total.toFixed(2)}</h4>`
    cartHTML += `<button onclick="makeOrder()">Checkout</button>`
  }
  // console.log(cartHTML)
  shoppingDiv.innerHTML = cartHTML
}

const addToCart = (event) => {
  event.preventDefault()
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
  // console.log(`cart: ${cart}`)

  renderCart()
}

add_to_cart_buttons.forEach((button) => {
  button.addEventListener("click", addToCart)
})

const removeFromCart = (productId) => {
  let cart = JSON.parse(localStorage.getItem("cart"))
  // filter to check wich item we want to delete
  cart = cart.filter((item) => item.id !== productId)
  localStorage.setItem("cart", JSON.stringify(cart))
  renderCart()
}

// Omer did this
let cartShown = false

const toggleCartView = (event) => {
  console.log("toggle event")
  if (cartShown) {
    shoppingDiv.style.display = "none"
    cartShown = false
  } else {
    shoppingDiv.style.display = "block"
    renderCart()
    cartShown = true
  }
}

const makeOrder = async () => {
  const cart = JSON.parse(localStorage.getItem("cart")) || []
  
  if (cart.length === 0) {
    alert("Cart is empty")
    return
  }

  try {
    // Get clinic ID from URL
    const clinicId = window.location.pathname.split("/")[2]
    
    const response = await fetch(`/users/${clinicId}/sync-cart/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
      },
      body: JSON.stringify({ items: cart })
    })

    if (response.ok) {
      localStorage.clear()
      renderCart()
      alert("Order created successfully!")
    } else {
      const error = await response.json()
      alert(`Failed: ${error.message}`)
    }
  } catch (error) {
    console.error("Error:", error)
    alert("Error creating order")
  }
  // localStorage.clear()
  renderCart()
}

cartButton.addEventListener("click", toggleCartView)

// Initialize cart display on page load
renderCart()
