function loadXMLDoc()
    {   
        var req = new XMLHttpRequest()
        req.onreadystatechange = function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    //error handling code here
                }
                else
                {
                    var response = JSON.parse(req.responseText)
                        var l=response.username.length;                 
                        var img="";
			img+='<p>'
                        for(i=0;i<l;i++)
                                {
                                im=response.username[i];
                                if(i%4==0 && i!=0)img+='<br></p><p>';  
                                img+='<a href="'+im+'"><img class=image height=70 width=70 src="'+im+'"></img></a>';
                                }
                        img+='</p>'
                    document.getElementById('myDiv').innerHTML =img;
//                      alert(img);
                //for(i=0;i<response.username.length;i++)
                //      imglist+='<li><img src= "' +response.username[i] + '"></li>';
                //$('#myDiv').append('<li><img src="'+response.username[0]+'"></li>');
                }
            }
        }
    
        req.open('POST', '/ajax')
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        var un = document.getElementById('SearchBox').value
        var postVars ='username='+ un
        req.send(postVars)
        
        return false
    }

