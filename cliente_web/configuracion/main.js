var cat_dl = document.getElementById('cat-dl');
var ol = document.getElementById('product-list');
var bra_dl = document.getElementById('bra-dl');

var auth = localStorage.getItem("auth");


var url = "http://proyecto-tienda-acz.herokuapp.com/catalog";
fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log("Hola mundo");
        console.log(data.products[0].product_img_path);
        for (let i = 0; i < data.categories.length; i++) {
            cat_dl.innerHTML +=
                `
                    <dd><a onclick=searchProduct(${data.categories[i].category_id})>${data.categories[i].category_name}</dd>
                `
        }
        for (let i = 0; i < data.brands.length; i++) {
            bra_dl.innerHTML +=
                `
                    <dd><a onclick=searchProduct("",${data.brands[i].brand_id})>${data.brands[i].brand_name}</dd>
                `
        }
        for (let i = 0; i < data.products.length; i++) {
            ol.innerHTML +=
                `
                    <!--Lista de productos-->
                    <li class="product-li">
                        <div id="product-img-div">
                            <!--Aqui va la imagen-->
                            <img src="img/img-not-found.png" alt="">
                        </div>
                        <div id="product-div">
                            <!--Aqui va el contenido del producto-->
                            <a id="product-title" onclick="productDescription(${data.products[i].product_id})">
                                <h2>${data.products[i].product_name}</h2>
                            </a>
                            <h4>$${data.products[i].product_price}</h4>
                        </div>
                    </li>
                `
        }
    })

function searchProduct(category = "", brand = "") {
    url = "http://proyecto-tienda-acz.herokuapp.com/catalog/products/search?";
    if (category != "") {
        url += ("category_id=" + category + "&");
    }
    if (brand != "") {
        url += ("brand_id=" + brand);
    }
    console.log(url)
    fetch(url)
        .then(res => res.json())
        .then(data => {
            ol.innerHTML = ``;
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                ol.innerHTML +=
                    `
                    <!--Lista de productos-->
                    <li class="product-li">
                        <div id="product-img-div">
                            <!--Aqui va la imagen-->
                            <img src="img/img-not-found.png" alt="">
                        </div>
                        <div id="product-div">
                            <!--Aqui va el contenido del producto-->
                            <a id="product-title" href="">
                                <h2>${data[i].product_name}</h2>
                            </a>
                            <h4>$${data[i].product_price}</h4>
                        </div>
                    </li>
                `
            }
        })
}

function productDescription(productId) {
    const root = document.getElementById('root');
    const url = "https://proyecto-tienda-acz.herokuapp.com/catalog/products/" + productId + "/description";
    var quantity = 5;
    root.innerHTML = "";
    fetch(url)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            console.log(quantity);
            console.log(data.product.product_id);
            root.innerHTML = `
            <div>
                <div id="product-img-div">
                    <!--Aqui va la imagen-->
                    <img src="img/img-not-found.png" alt="">
                </div>
                <h1 class='hola'>${data.product.product_name}</h1> 
                <p>${data.product.product_description}</p>
                <h3>$${data.product.product_price}</h3>
                <input class='btn' type='button' value='Agregar al carrito' onclick="agregarAlCarrito(${data.product.product_id},${quantity})">
                <input class='btn' type='button' value='Agregar comentario' onclick="agregarComentario(${data.product.product_id})">
            </div>  
            <h2>Comentarios</h2>
        `
            for (let i = 0; i < data.comments.length; i++) {
                root.innerHTML += `
                <div id='comentario-${i}' class='comentarios'> 
                    <h3>${data.comments[i].qualification}</h3>
                    <p>${data.comments[i].description}</p>
                </div>
            `
                if (data.comments[i].username == window.localStorage.getItem("username")) {
                    document.getElementById("comentario-" + i).innerHTML += `
                    <input class='btn-eliminar' type='button' value='Eliminar Comentario' onclick="eliminarComentario(${data.comments[i].comment_id},${data.product.product_id})"> 
                `
                }
            }
        })
}

function agregarAlCarrito(productId, quantity) {
    console.log("entra");
    const url = "https://proyecto-tienda-acz.herokuapp.com/cart/products";
    fetch(url, {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth
            },
            'body': JSON.stringify({
                'product': productId,
                'quantity': quantity
            })
        })
        .then(res => {
            console.log(res.status);
            if (res.status == 200 && document.getElementById('carrito-div').innerHTML != "") {
                cargarCarrito(document.getElementById('carrito-div'))
            }
        });
}

function agregarComentario(productId) {
    const url = "https://proyecto-tienda-acz.herokuapp.com/catalog/products/" + productId + "/comments";
    fetch(url, {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth
            },
            'body': JSON.stringify({
                'comment_description': "Muy bueno el producto",
                'comment_qualification': 5
            })
        })
        .then(res => {
            console.log(res.status);
            if (res.status == 200) {
                alert("Se agrego tu comentario correctamente");
                productDescription(productId);
            }
        });
}
const btnSalir = document.getElementById("btn-salir");
btnSalir.addEventListener('click', logout);

function logout() {
    localStorage.removeItem("auth");
    auth = ""
}

const btnCarrito = document.getElementById("btn-carrito");
btnCarrito.addEventListener('click', abrirCarrito);

function cargarCarrito(divCarrito) {
    divCarrito.style.textAlign = "center";
    divCarrito.innerHTML = "<h1> Carrito </h1>";
    const url = "https://proyecto-tienda-acz.herokuapp.com/cart/products";
    fetch(url, {
            'method': 'GET',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth
            }
        })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            var total = 0;
            for (let i = 0; i < data.length; i++) {
                var precioProductoTotal = data[i].product_price * data[i].product_quantity;
                divCarrito.innerHTML += `
                <label>${data[i].product_name} </label><br> 
                <label>Precio Unitario: ${data[i].product_price}</label><br>    
                <label>Cantidad: ${data[i].product_quantity}</label><br>    
                <label>Precio Total: ${data[i].product_price * data[i].product_quantity}</label><br>    
                <input class='btn-eliminar' type='button' value='Eliminar del Carrito' onclick=eliminarDelCarrito(${data[i].cart_id})><br>
            `
                total += data[i].product_price * data[i].product_quantity;
            }
            divCarrito.innerHTML += `
            <br><label>Total a pagar: ${total}</label><br>
            <div id="paypal-button-container"></div>
        `;
            paypal.Buttons({
                createOrder: function(data, actions) {
                    // This function sets up the details of the transaction, including the amount and line item details.
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: total
                            }
                        }]
                    });
                }
            }).render('#paypal-button-container')
        })
}

function abrirCarrito() {
    const divCarrito = document.getElementById("carrito-div");
    if (divCarrito.innerHTML == "") {
        cargarCarrito(divCarrito);
    } else {
        divCarrito.innerHTML = "";
    }

}

function eliminarDelCarrito(carritoId) {
    var url = 'https://proyecto-tienda-acz.herokuapp.com/cart/products/' + carritoId;
    fetch(url, {
            'method': 'DELETE',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth
            }
        })
        .then(res => res.json())
        .then(data => {
            if (data.message == "Todo bien") {
                cargarCarrito(document.getElementById('carrito-div'))
            } else {
                console.log('No se pudo borrar el producto!')
            }
        })
}

function eliminarComentario(comentarioId, productId) {
    var url = 'https://proyecto-tienda-acz.herokuapp.com/catalog/products/comments/' + comentarioId;
    fetch(url, {
            'method': 'DELETE',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth
            }
        })
        .then(res => res.json())
        .then(data => {
            alert("Se elimino el comentario correctamente!")
            productDescription(productId);
        })
}