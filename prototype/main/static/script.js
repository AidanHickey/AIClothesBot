
function goToItemDetail(itemId, itemName, itemPrice, itemDescription) {
    const url = `item-detail.html?name=${encodeURIComponent(itemName)}&price=${encodeURIComponent(itemPrice)}&description=${encodeURIComponent(itemDescription)}`;
    window.location.href = url;
}

window.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.clothing-item');
    items.forEach(item => {
        const itemId = item.getAttribute('data-id');
        const itemName = item.querySelector('.card-title').innerText;
        const itemPrice = item.getAttribute('data-price');
        const itemDescription = item.getAttribute('data-description');

        item.addEventListener('click', () => goToItemDetail(itemId, itemName, itemPrice, itemDescription));
    });

    loadItemDetails();
});

function loadItemDetails() {
    const urlParams = new URLSearchParams(window.location.search);
    const itemName = urlParams.get('name');
    const itemPrice = urlParams.get('price');
    const itemDescription = urlParams.get('description');

    if (document.getElementById('item-name')) {
        document.getElementById('item-name').innerText = itemName || "Item not found";
        document.getElementById('item-price').innerText = `Price: ${itemPrice || "N/A"}`;
        document.getElementById('item-description').innerText = itemDescription || "No description available.";
    }
}
function printProductRating(id)
{   
    var wrapper = document.getElementById(`rating${id}`);
    var count = document.getElementById(`rating${id}`).getAttribute('data-rating');
    var myHTML = '';
    for (let i = 0; i < 5; i++) {
    if (count >= 1)
    {
    myHTML+= "<span class='fa fa-star checked'></span>";
    count--;
    }
    else if (count > 0 && count < 1)
    {
    myHTML+= "<span class='fa fa-star-half-full checked'></span>"    
    count--;
    }
    else  myHTML+= "<span class='fa fa-star-o checked'></span>";
    }
   wrapper.innerHTML = myHTML;
}



  function updateStage(userid) {
    $.ajax({
      url: `get_favorite/${userid}`, // if you don't have dynamic url
      type: 'GET'
    })
    .done(response => {
      const data = response;
      for(var id in data) {
        var productid = (data[id].productid);
        console.log(productid);
        if(document.getElementById(`favoriteBtn${productid}`)){
        var wrapper = document.getElementById(`favoriteBtn${productid}`);
        wrapper.innerHTML = "Unfavorite";
        }
        
      }
    })
  }
    
  function onFavorite(id, userid) {
    $.ajax({
      url: `change_favorite/${id}/${userid}`, // if you don't have dynamic url
      type: 'GET'
    })
    .done(response => {
      const data = response;
        console.log(id);
        var wrapper = document.getElementById(`favoriteBtn${id}`);
        if(wrapper.innerHTML == "Favorite"){
        wrapper.innerHTML = "Unfavorite";
        }
        else wrapper.innerHTML = "Favorite";
        
      
    })
  }  


/*function onFavorite(id, user)
{   
    var wrapper = document.getElementById(`favoriteBtn${id}`);
    if (user=="AnonymousUser")
    window.location.href='../signin';
    else {
    document.location.href =`${id}`;
    updateStage(user.userid);
    }
};*/





