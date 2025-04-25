
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
    for (let i = 0; i < 5; i++) {
    if (count >= 1)
    {
      wrapper.innerHTML+= "<span class='fa fa-star checked'></span>";
    count--;
    }
    else if (count > 0 && count < 1)
    {
      wrapper.innerHTML+= "<span  class='fa fa-star-half-full checked'></span>"    
    count--;
    }
    else  wrapper.innerHTML+= "<span  class='fa fa-star-o checked'></span>";
    }
}

function likeEvent(postid) {   
  $.ajax({
    url: `/like-post/${postid}`, 
    type: 'GET'
  })
  .done(response => {
    var likeText = document.getElementById(`likeBtn${postid}`);
    var likeNumber = document.getElementById(`likeNumber${postid}`);
    if (response.status == "Unliked")
    {
        likeText.innerHTML = `<i class="fas fa-thumbs-up"></i> Like`
        
    }
    else {
    likeText.innerHTML = `<i class="fas fa-thumbs-up"></i> Liked`
    }
    if (response.count == 1)
    {
      likeNumber.innerHTML = `Liked by 1 person`;
    }
    else if (response.count >1 )
    {
      likeNumber.innerHTML = `Liked by ${response.count} people`
    }
    else likeNumber.innerHTML = `No likes yet`
    }
  )
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

  $(document).ready(function () {
    $('.accept_friend').submit(function(e){
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
        type:"POST",
        url: `../create_friend`,
        data: formData, 
        success: function(response){
        var acceptBtn = document.getElementById(`acceptBtn${formData.get('touser')}`);
        var rejectBtn = document.getElementById(`rejectBtn${formData.get('touser')}`);
        acceptBtn.disabled = "true";
        rejectBtn.disabled = "true";
        acceptBtn.innerHTML = "Accepted!"
        location.reload(true)

        },
        error: function(response) {
        },
        cache: false,
        contentType: false,
        processData: false
      
    })
  })
})

$(document).ready(function () {
  $('.reject_friend').submit(function(e){
  e.preventDefault();
  var formData = new FormData(this);
  $.ajax({
      type:"POST",
      url: `../create_friend`,
      data: formData, 
      success: function(response){
      var acceptBtn = document.getElementById(`acceptBtn${formData.get('touser')}`);
      var rejectBtn = document.getElementById(`rejectBtn${formData.get('touser')}`);
      acceptBtn.disabled = "true";
      rejectBtn.disabled = "true";
      rejectBtn.innerHTML = "Rejected!"
  
      },
      error: function(response) {
      },
      cache: false,
      contentType: false,
      processData: false
    
  })
})
})

$(document).ready(function () {
  $('.unfriend').submit(function(e){
  e.preventDefault();
  var formData = new FormData(this);
  $.ajax({
      type:"POST",
      url: `../create_friend`,
      data: formData, 
      success: function(response){

          var friend = document.getElementById(`friendLi${formData.get('touser')}`);
          friend.style.display = "none";

      },
      error: function(response) {
      },
      cache: false,
      contentType: false,
      processData: false
    
  })
})
})

$(document).ready(function () {
  $('.friendForm').submit(function(e){
  e.preventDefault();
  var formData = new FormData(this);
  var command = formData.get('command');
  if (command == "Unfriend")
    formData.set("command","unfriend");
  else if (command == "Remove Friend Request")
    formData.set("command","remove");
  else if (command == "Accept Friend Request")
    formData.set("command","accept");
  else 
    formData.set("command","send")

  $.ajax({
      type:"POST",
      url: `../create_friend`,
      data: formData, 
      success: function(response){
        console.log(response)
        var buttonText = document.getElementById("friendBtn");
         if (formData.get('command')=="unfriend")
         {
            buttonText.style.backgroundColor="#71e293";
         }
         else if (formData.get('command')=="accept")
        {
            buttonText.style.backgroundColor="rgb(238, 54, 30)";
        }
         var input = document.getElementById("command");
         input.value = response["friend_button_text"];
         buttonText.innerHTML = response["friend_button_text"];
         if (response["friend_count"]!=undefined)
        {
          var friend_count = document.getElementById("friendCount");
          if (response["friend_count"]>1)
           friend_count.innerHTML = response["friend_count"] + " Friends"
          else friend_count.innerHTML = response["friend_count"] + " Friend"
        }
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
  function getMessageOnClick(userid) { 
    if (currentMessageUser!=null)
    {
    console.log('hello');
    clearInterval(currentMessageUser);
    }
    getMessage(userid);
    currentMessageUser = setInterval(getMessage, 3000 ,userid);
  }

    function getMessage(userid) {
      var chatbox = document.getElementById("chat-box");
          chatbox.style.display = "inline"
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
        header.innerHTML = `<h5> Messages with <a href="../profile/${userid}">${roomName.innerText}</a> </h5>`
        var textbox = document.getElementById("message")
        textbox.style.display = 'inline'; 
        document.getElementById("Send").style.display = 'inline';
      }
    
      )
      
      }

$(document).ready(function () {
    $('#message-form').submit(function(e){
    e.preventDefault();
    var formData = new FormData(this);
    if (formData.get('message').trim()=="")
    console.log("do nothing");
    else {
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
}})}
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

  function toggleCommentBox(postId) {
    let commentBox = document.getElementById(`commentBox${postId}`);
    if (commentBox.style.display === "none") {
        commentBox.style.display = "block";
    } else {
        commentBox.style.display = "none";
    }
}

function postComment(postId) {
  let commentInput = document.getElementById(`commentInput${postId}`);
  let commentText = commentInput.value.trim();

  console.log("Comment Text:", commentText); // Debugging Line

  if (commentText === "") {
      alert("Comment cannot be empty.");
      return;
  }

  $.ajax({
      type: "POST",
      url: "/post-comment/",
      data: {
          post_id: postId,
          content: commentText,
          csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      success: function(response) {
          console.log("Comment Posted Successfully!"); // Debugging Line
          let commentsContainer = document.getElementById(`commentsContainer${postId}`);
          let newComment = document.createElement("div");
          newComment.classList.add("comment");
          newComment.innerHTML = `<strong>You</strong>: ${commentText}`;
          commentsContainer.appendChild(newComment);

          commentInput.value = ""; // Clear input after posting
          toggleCommentBox(postId); // Hide the comment box after posting
      },
      error: function(error) {
          console.error("Error posting comment:", error);
          alert("Failed to post comment. Please try again.");
      }
  });
}
function toggleReplyBox(commentId) {
  let replyBox = document.getElementById(`replyBox${commentId}`);
  if (replyBox.style.display === "none") {
      replyBox.style.display = "block";
  } else {
      replyBox.style.display = "none";
  }
}

function postReply(commentId, postId) {
  let replyInput = document.getElementById(`replyInput${commentId}`);
  let replyText = replyInput.value.trim();

  if (replyText === "") {
      alert("Reply cannot be empty.");
      return;
  }

  $.ajax({
      type: "POST",
      url: "/post-reply/",
      data: {
          parent_comment_id: commentId,
          post_id: postId,
          content: replyText,
          csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      success: function(response) {
          let repliesContainer = document.getElementById(`repliesContainer${commentId}`);
          let newReply = document.createElement("div");
          newReply.classList.add("reply");
          newReply.innerHTML = `<strong>You</strong>: ${replyText}`;
          repliesContainer.appendChild(newReply);

          replyInput.value = ""; // Clear input after posting
          toggleReplyBox(commentId); // Hide the reply box after posting
      },
      error: function(error) {
          console.error("Error posting reply:", error);
          alert("Failed to post reply. Please try again.");
      }
  });
}

