//   |                                                          |
// --+----------------------------------------------------------+--
//   |   Code by : yasserbdj96                                  |
//   |   Email   : yasser.bdj96@gmail.com                       |
//   |   Github  : https://github.com/yasserbdj96               |
//   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
// --+----------------------------------------------------------+--  
//   |        all posts #yasserbdj96 ,all views my own.         |
// --+----------------------------------------------------------+--
//   |                                                          |

//START{
function include(){
	if(typeof arguments[0]==='undefined'||arguments[0]===null && typeof arguments[1]==='undefined'||arguments[1]===null){
		/**/
		var z,i,elmnt,file,xhttp;
		z=document.getElementsByTagName("*");
		for(i=0;i<z.length;i++){
			elmnt=z[i];
			file=elmnt.getAttribute("include");
			if(file){
				xhttp=new XMLHttpRequest();
				xhttp.onreadystatechange=function(){
					if (this.readyState==4){
						if(this.status==200){elmnt.innerHTML=this.responseText;}
						if(this.status==404){elmnt.innerHTML="Code not found.";}
						elmnt.removeAttribute("include");
						include();
					}
				}
				xhttp.open("GET",file,true);
				xhttp.send();
				return;
			}
		}
	}else{
	        if (typeof arguments[1]==='undefined' ||arguments[0]===null){
	            var arguments=atob(arguments[0]).split(':');
	        }
		/**/
		if(arguments[1]=="js"){
			var fileref=document.createElement('script');
			fileref.setAttribute("type","text/javascript");
			fileref.setAttribute("src",arguments[0]);
			document.getElementsByTagName("head")[0].appendChild(fileref);
		}else if(arguments[1]=="css"){
			var fileref=document.createElement("link");
			var css=arguments[0].split(".css")[0];
			css=css.split("/");
			fileref.setAttribute("id",css[css.length-1]);
			fileref.setAttribute("rel","stylesheet");
			fileref.setAttribute("type","text/css");
			fileref.setAttribute("href",arguments[0]);
			document.getElementsByTagName("head")[0].appendChild(fileref);
		}else if(arguments[1]=="ico"){
			var link=document.querySelector("link[rel*='icon']")||document.createElement('link');
			link.type='image/x-icon';
			link.rel='shortcut icon';
			link.href=arguments[0];
			document.getElementsByTagName('head')[0].appendChild(link);
		}else if(arguments[1]=="title"){
			document.title=arguments[0];
		}
	}
}
//}END.