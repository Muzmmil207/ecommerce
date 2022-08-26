var updateBtn = document.getElementsByClassName('update_cart')

for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)

        if (user === 'AnonmousUser') {
            console.log('user not login')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('user is login')

    var url = '/update-item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        .then((response) => {
            return response.json
        })
        .then((data) => {
            console.log('data: ', data)
            location.reload()
        })
}





