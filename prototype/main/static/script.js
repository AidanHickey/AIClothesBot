
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
   /* if (count >= 0 && count < 1)
        {
            document.getElementById('firstStar').className="fa fa-star ";
            document.getElementById('secondStar').className="fa fa-star ";
            document.getElementById('thirdStar').className="fa fa-star ";
            document.getElementById('fourthStar').className="fa fa-star ";
            document.getElementById('fifthStar').className="fa fa-star ";
        }
        if (count >= 1 && count < 2)
            {
                document.getElementById('firstStar').className="fa fa-star checked";
                document.getElementById('secondStar').className="fa fa-star ";
                document.getElementById('thirdStar').className="fa fa-star ";
                document.getElementById('fourthStar').className="fa fa-star ";
                document.getElementById('fifthStar').className="fa fa-star ";
            }
            (count >= 2 && count < 3)
                {
                    document.getElementById('firstStar').className="fa fa-star checked";
                    document.getElementById('secondStar').className="fa fa-star checked";
                    document.getElementById('thirdStar').className="fa fa-star ";
                    document.getElementById('fourthStar').className="fa fa-star ";
                    document.getElementById('fifthStar').className="fa fa-star ";
                }
                (count >= 3 && count < 4)
                    {
                        document.getElementById('firstStar').className="fa fa-star checked";
                        document.getElementById('secondStar').className="fa fa-star checked";
                        document.getElementById('thirdStar').className="fa fa-star checked";
                        document.getElementById('fourthStar').className="fa fa-star ";
                        document.getElementById('fifthStar').className="fa fa-star ";
                    }
                    if (count >= 4 && count < 5)
                        {
                            document.getElementById('firstStar').className="fa fa-star checked";
                            document.getElementById('secondStar').className="fa fa-star checked";
                            document.getElementById('thirdStar').className="fa fa-star checked";
                            document.getElementById('fourthStar').className="fa fa-star checked";
                            document.getElementById('fifthStar').className="fa fa-star ";
                        }
                    }*/





