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
var originalTitle=document.title;

//iswork:
function iswork_f(){
    try {
        eel.iswork()(
            function(ret){
                return ret;
            }
        )
        return "True";
    } catch(err) {
        console.log(err.message);
        return "False";
    }
}

//
function connect_with_cookie(){
    settings_opt();
    var iswork=iswork_f();
    //console.log(iswork);
    if (iswork!=="False"){
        if (getCookie("url")!=null && getCookie("key")!=null && getCookie("url")!="undefined" && getCookie("key")!="undefined"){
            connect(how="connect_with_cookie");
        }
    }else{
        //console.log("false");
        document.getElementById('connected').style.display='none';
        document.getElementById('login').style.display='none';
        document.getElementById('notwork').style.display='block';
    }
}
//connect:
function connect(how=""){
    if(how!="connect_with_cookie"){
        var key=document.getElementById("key").value;
        var url=document.getElementById("url").value;
        setCookie("key",key,1);
        setCookie("url",url,1);
    }else{
        var url = getCookie("url");
        var key = getCookie("key");
        //alert(url);
    }
    
    
    //document.cookie = "url="+url+"; key="+key+";path=/";
    eel.connect(key,url)(
        function(ret){
            if(ret=="connected"){
                //document.title="hiphp : "+url;
                include("hiphp : "+url,"title");
                document.getElementById("login").style.display='none';
                document.getElementById("connected").style.display='block';
                eel.ls(key,url)(function(retu){
                    var retu=JSON.parse(retu);

                    //var xxp=tree(retu);
                    //console.log(retu);
                    //var data = xxp;
                    //document.body.appendChild(getList(data));

                    ls="<tr><th style='width:75%;'>Path</th><th>Permissions</th><th>Options</th></tr>";
                    for (let i = 0; i < retu.length; i++) {
                        var xx=retu[i].split(':');
                        var pathxx=xx[0];

                        
                        var file_type=(/[.]/.exec(pathxx)) ? /[^.]+$/.exec(pathxx) : undefined;
                        if (file_type=="zip" || file_type=="rar"){
                            var img_icon='<i class="fa fa-file-archive-o c_green"></i>';//"<img class='img_icon' src='./icons/php.png'>";
                        }else if (file_type=="png" || file_type=="jpg" || file_type=="jpeg" || file_type=="gif"){
                            var img_icon='<i class="fa fa-file-image-o c_red"></i>';
                        }else if (file_type=="txt" || file_type=="htaccess"){
                            var img_icon='<i class="fa fa-file-text-o c_orange"></i>';
                        }
                        else{
                            var img_icon='<i class="fa fa-file-o c_blue"></i>';
                        }

                        var permxx='<a class="pointer" onclick="permi('+"'"+pathxx+"',"+"'"+xx[1]+"'"+')">'+xx[1]+'</a>';
                        var s=' ';//space
                        var edit='<a class="pointer fs20" onclick="cat('+"'"+pathxx+"'"+')"><i class="fa fa-pencil c_blue"></i></a>'+s;
                        var del='<a class="pointer fs20" onclick="del('+"'"+pathxx+"'"+')"><i class="fa fa-trash-o c_red"></i></a>'+s;
                        var ren='<a class="pointer fs20" onclick="ren('+"'"+pathxx+"'"+')"><i class="fa fa-i-cursor c_orange"></i></a>'+s;
                        var down='<a class="pointer fs20" onclick="download_file('+"'"+pathxx+"'"+')"><i class="fa fa-download c_green"></i></a>'+s;
                        var info='<a class="pointer fs20" onclick="file_info('+"'"+pathxx+"'"+')"><i class="fa fa-info-circle c_orange"></i></a>'+s;
                        var check='<div class="inline-block"><input name="fileschecked" type="checkbox" value="'+pathxx+'"/><span></span></div>';
                        //var down='<a class="pointer" onclick="down('+"'"+pathxx+"'"+')">dddd</a>'+s;
                        ls+='<tr><td>'+check+" <div class='ls_list inline-block'>"+img_icon+" "+pathxx+'</div></td><td>'+permxx+'</td><td>'+edit+ren+down+del+info+'</td></tr>';
                    }
                    document.getElementById("ls").innerHTML=ls;
                })
            }else{
                prompt("We were unable to recognize the hiphp identifier.\nCopy this code into the file whose path you entered earlier.", ret);
                document.getElementById("login").style.display='block';
                document.getElementById("connected").style.display='none';
            }
            //include(document.title,"title");
        }
    )
}
/*
//tree:
function tree(paths){

let agg = {
  temp: []
};

paths.forEach(path => {
  path.split('/').reduce((agg, part, level, parts) => {
    if (!agg[part]) {
      agg[part] = {
        temp: []
      };
      agg.temp.push({
        id: parts.slice(0, level + 1).join("/"),
        //level: level + 1,
        children: agg[part].temp
      })
      // console.log(agg)
    }
    return agg[part];
  }, agg)
})

var result = agg.temp;
//console.dir(result);

console.log(result)
//traverse(result);

}
*/

//cat:
function cat(path){
    var url = getCookie("url");
    var key = getCookie("key");
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    eel.cat(key,url,path)(
        function(ret){
            document.getElementById("temp").innerText=path;
            document.getElementById("cat").style.display='block';
            document.getElementById("codeEditor").style.display='block';
            document.getElementById("cat").value=ret;
            document.getElementById("cat").innerHTML=ret;
            lineCounter(ret);
            document.getElementById("return").style.display='block';
            document.getElementById("save").style.display='block';
            document.getElementById("ls").style.display='none';
            document.getElementById("add").style.display='none';
            document.getElementById("up").style.display='none';
            try {
                document.getElementById("reload").style.display='none';
                document.getElementById("check").style.display='none';
              } catch (e) {
                pass(); // pass exception object to error handler
            }
            document.getElementById("br").style.display='none';
            //document.title="hiphp : "+path;
            include("hiphp : "+path,"title");
            
           
        }
    )
}
//back:
function back(){
    document.getElementById("ls").style.display='revert';
    document.getElementById("add").style.display='block';
    document.getElementById("up").style.display='block';
    document.getElementById("cat").innerHTML='';
    document.getElementById("codeEditor").style.display='none';
    document.getElementById("temp").innerText='';
    document.getElementById("cat").style.display='none';
    document.getElementById("return").style.display='none';
    document.getElementById("save").style.display='none';
    try {
        document.getElementById("reload").style.display='block';
        document.getElementById("check").style.display='block';
      } catch (e) {
        pass(); // pass exception object to error handler
    }
    document.getElementById("br").style.display='block';
    document.getElementById("settings").style.display='none';
    var url=document.getElementById("url").value;
    if(url!=""){
        //document.title="hiphp : "+url;
        include("hiphp : "+url,"title");
    }else{
        //document.title=originalTitle;
        include(originalTitle,"title");
    }
    
}
//deconnect:
function deconnect(){
    //document.getElementById("key").value="";
    //document.getElementById("url").value="";
    eraseCookie("key");
    eraseCookie("url");
    document.getElementById("login").style.display='block';
    document.getElementById("connected").style.display='none';
    back();
}
//save:
function save(){
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    var url = getCookie("url");
    var key = getCookie("key");
    var pathx=document.getElementById("temp").textContent;
    var contentx=btoa(document.getElementById("cat").value);
    eel.save(key,url,pathx,contentx)(
        function(x){
            if(x==""){alert("unsuccessful save!\nUnknown error.");}
            else{alert(x);}
            cat(pathx);
        }
    )
}
//delete:
function del(path){
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    var url = getCookie("url");
    var key = getCookie("key");
    var result = confirm("Want to delete '"+path+"' ?");
    if (result) {
        eel.delte(key,url,path)(
            function(retu){
                alert(retu);
                connect();
            }
        )
    }
}
//info:
function file_info(path){
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    var url = getCookie("url");
    var key = getCookie("key");
    //var result = confirm("Want to delete '"+path+"' ?");
    if (path!="") {
        eel.info(key,url,path)(
            function(retu){
                alert(retu);
                //connect();
            }
        )
    }
}
//rename:
function ren(path){
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    var url = getCookie("url");
    var key = getCookie("key");
    //let text;
    let newname=prompt("Enter the new name/path for the file:",path.replace('./',''));
    if(newname!=null && newname!=""){
        eel.ren(key,url,path,"./"+newname)(
            function(retu){
                alert(retu);
                connect();
            }
        )
    }
}
//add:
function add(){
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    var url = getCookie("url");
    var key = getCookie("key");
    //let text;
    let newfile=prompt("Enter the file name:","");
    if(newfile!=null && newfile!=""){
        eel.add_new(key,url,newfile)(
            function(retu){
                alert(retu);
                connect();
            }
        )
    }
}
//permissions:
function permi(path,perm){
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    var url = getCookie("url");
    var key = getCookie("key");
    let newpermi=prompt("Change file permission '"+path+"'",perm);
    if(newpermi!=null && newpermi!="" && newpermi!=perm){
        eel.new_permi(key,url,path,newpermi)(
            function(retu){
                alert(retu);
                connect();
            }
        )
    }
}

//download:
function download_file(path){
    //var key=document.getElementById("key").value;
    //var url=document.getElementById("url").value;
    var url = getCookie("url");
    var key = getCookie("key");
    if(path!=null && path!=""){
        eel.download_file(key,url,path)(
            function(retu){
                //download("x.txt",retu)
                const obj = JSON.parse(retu);

                //console.log(obj.file);


                download(obj.file,obj.cont,obj.type);
                connect();
            }
        )
    }
}

function download(filename, text,mime_content_type){
    var element = document.createElement('a');
    element.setAttribute('href', 'data:'+mime_content_type+';charset=utf-8,' + encodeURIComponent(atob(text)));
    element.setAttribute('download', filename);
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
  
    document.body.removeChild(element);
}

//version:
function version(){
    eel.version()(
        function(retu){
            var ver = document.getElementById("version");
            var hiphp_version=retu[1];
            var hiphp_desktop=retu[0];
            ver.innerText=hiphp_version+", "+hiphp_desktop;
        }
    )
}

/*
//download:
function down(path){
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
        eel.down(key,url,path)(
            function(retu){
                //alert(retu);
                ///document.getElementById("down").innerText=retu;
                connect();
            }
        )
}
*/
function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function eraseCookie(name) {   
    document.cookie = name +'=; Path=/; Expires=Thu, 25 Jan 1996 00:00:01 GMT;';
}
function pass(){}

//
function settings(){
    try {
        document.getElementById("cat").style.display='none';
        document.getElementById("ls").style.display='none';
        document.getElementById("codeEditor").style.display='none';
        document.getElementById("save").style.display='none';
      } catch (e) {
        pass(); // pass exception object to error handler
    }
    document.getElementById("br").style.display='block';
    document.getElementById("return").style.display='block';
    document.getElementById("settings").style.display='block';
    document.getElementById("add").style.display='none';
    document.getElementById("up").style.display='none';
    //document.getElementById("br").style.display='none';
    include("hiphp : settings","title");
    //document.title="hiphp : settings";
}

/*
function check(clickedElement){
        var checked_var=clickedElement;
        //var checked_var=event.target;
        //alert(checked_var);
        if (checked_var.checked) {
            checked_var.checked = false;
            alert("false");
        } else {
            checked_var.checked = true;
            alert("true");
        }
        //console.log(event.srcElement.id);
    //}
    //window.addEventListener('click',onClick);
    //.checked = true;
}*/


/**/
function lineCounter(code){
    var htmlTemplateStr = code;
			var codeEditor = document.getElementById('cat');
			var lineCounter = document.getElementById('lineCounter');
			
			var lineCountCache = 0;
			function line_counter() {
		        var lineCount = codeEditor.value.split('\n').length;
		        var outarr = new Array();
		        if (lineCountCache != lineCount) {
		            for (var x = 0; x < lineCount; x++) {
		                outarr[x] = (x + 1) + '.';
		            }
		            lineCounter.value = outarr.join('\n');
		        }
		        lineCountCache = lineCount;
			}

			codeEditor.addEventListener('scroll', () => {
				lineCounter.scrollTop = codeEditor.scrollTop;
			    lineCounter.scrollLeft = codeEditor.scrollLeft;
                //alert("1");
			});

			codeEditor.addEventListener('input', () => {
				line_counter();
                //alert("2");
			});

			codeEditor.addEventListener('keydown', (e) => {
			    let { keyCode } = e;
			    let { value, selectionStart, selectionEnd } = codeEditor;

			    if (keyCode === 9) {  // TAB = 9
			      e.preventDefault();
			      codeEditor.value = value.slice(0, selectionStart) + '\t' + value.slice(selectionEnd);
			      codeEditor.setSelectionRange(selectionStart+2, selectionStart+1)
			    }
                //alert("3");
		  	});

		  	codeEditor.value = htmlTemplateStr;
		  	line_counter();
}

//
function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

//
function settings_opt(){
    readTextFile("config.json", function(text){
        var data = JSON.parse(text);

        if(data["Dark Mode"]=="False"){
            //document.getElementById("darkmode").checked = false;
            include("white.css","css");
        }else{
            document.getElementById("darkmode").checked=true;
            include("dark.css","css");
        }
        //console.log(data["Dark Mode"]);
    });
}

//
function darkmode_check(){
    eel.darkmode()(
        function(retu){
            if(retu=="False"){
                var pp=document.getElementById("dark");
                    pp.remove();
                    include("white.css","css");
            }else{
                var pp=document.getElementById("white");
                    pp.remove();
                    include("dark.css","css");
            }
        }
    )
}

//
function get_selected(todo){
    //
    var el = document.querySelectorAll('input[name=fileschecked]:checked');
    //const selected_list = [];
    for(var i = 0; i < el.length; i++) {
        //selected_list.push(el[i].value);
        if (todo=="download"){
            download_file(el[i].value);
        } else if (todo=="delete"){
            del(el[i].value);
        }
        //alert(el[i].value);
        
        
    }
}

//
console.log("%c %c %c Hiphp by yasserbdj96 %c  %c  https://yasserbdj96.github.io/  ","background: #0f81c1; padding:5px 0;","background: #0f81c1; padding:5px 0;","color: #0f81c1; background: #3b434b; padding:5px 0;","background: #0f81c1; padding:5px 0;","background: #2aaf49; padding:5px 0;");
//}END.