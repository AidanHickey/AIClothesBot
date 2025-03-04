
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
      type: 'GET',
      
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


  

 
 

   $(document).ready(function () {
      $('#create_chat_room').submit(function(e){
      e.preventDefault();
      var formData = new FormData(this);
      $.ajax({
          type:"POST",
          url: `../create_chat`,
          data: formData, 
          success: function(response){
         window.location.href = get_message_url;
            
          },
          error: function(response) {
          },
          cache: false,
          contentType: false,
          processData: false
        
      })
    })
  })


   /* $(document).ready(function () {
      $('#get-user-form').submit(function(e){
      e.preventDefault();
      var formData = new FormData(this);
      $.ajax({
          type:"POST",
          url: `get_user`,
          data: formData, 
          success: function(response){
            var users = document.getElementById("userDropDown");
            users.innerHTML = "";
            const data = response;
            console.log(data);
            for(var i in data)
            {
              users.innerHTML += `<img src="${media_url}${data[i].profileimg}" class="rounded-circle nav-user-icon" alt="User Profile Icon" width="40px" height="40px"> ${data[i].firstname} ${data[i].lastname}`;
            }
          },
          error: function (response) {
          },
          cache: false,
          contentType: false,
          processData: false
      })
    })
  })
*/

  /* function inboxDropdown(userid) {
    $.ajax({
      type: "GET",
      url: `get_inbox/${userid}`,
    })
      .done(response => {
        var inbox = document.getElementById("inboxDropdown");
        inbox.innerHTML = "";
        const data = response;
        console.log(data)
        for(var room in data) {
        var toUser;
        var toUserId;
        if (data[room].userOneID==userid){
            toUser = data[room].userTwoName;
            toUserId = data[room].userTwoID;
        }
        else if (data[room].userTwoID==userid)
        {
            toUser = data[room].userOneName;
            toUserId = data[room].userOneID;
        }
          inbox.innerHTML += `<a href="../message#${toUserId}" <b>${toUser}:</b> ${data[room].lastMessageSent} </a>`;
        }
        inbox.classList.toggle("show");
      })
    
    } */

  var currentMessageUser;
  function getMessageOnClick(userid)
  { 
    if (currentMessageUser!=null)
    {
    console.log('hello');
    clearInterval(currentMessageUser);
    }
    getMessage(userid);
    currentMessageUser = setInterval(getMessage, 3000 ,userid);
  }

    function getMessage(userid) {
      $.ajax({
        type: "GET",
        url: `get_message/${userid}`,
      })
        .done(response => {
          var messages = document.getElementById("chat-container");
          messages.innerHTML = "";
          const data = response;
          console.log(data)
          for(var message in data) {
          if (data[message].tag=="send")
          {
            messages.innerHTML += `<div class="me">${data[message].content}</div>`
          }
          else if (data[message].tag=="receive")
          {
            messages.innerHTML += `<div class="you">${data[message].content}</div>`
          }

        }
        var currentChatRoom = document.getElementById("chatroomid");
        var currentReceiver = document.getElementById("touser");
        currentChatRoom.value = data[0].chatroomid;
        currentReceiver.value = userid;
        var header = document.getElementById("messageHeader");
        var roomName = document.getElementById(`${userid}`)
        header.innerHTML = `<h5> Messages with ${roomName.innerText}`
        var textbox = document.getElementById("message")
        textbox.style.display = 'inline'; 
        document.getElementById("Send").style.display = 'inline';
        messages.scrollTop = messages.scrollHeight;
      }
    
      )
      
      }

$(document).ready(function () {
    $('#message-form').submit(function(e){
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
        type:"POST",
        url: `send_message`,
        data: formData, 
        success: function(response){
          var textbox = document.getElementById("message")
          textbox.value='';
          getMessage(response)
        },
        error: function (response) {
        },
        cache: false,
        contentType: false,
        processData: false
    })
  })}
  )

  $(document).ready(function () {
$( "#notification.dropdown" ).on( "mouseover", function() {
  console.log('ok')
  $.ajax({
    type:"POST",
    url: `read_notif`, 
    data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
    success: function(response){
      var notif = document.getElementById("notifCount");
      notif.innerHTML = '0';
    },
    })
  })})