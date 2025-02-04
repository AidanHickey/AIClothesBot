
                        var wrapper = document.getElementById("rating");
                        var count = document.getElementById('rating').getAttribute('data-count');
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
                        else  myHTML+= "<span class='fa fa-star'></span>";
                        }
                       wrapper.innerHTML = myHTML;
