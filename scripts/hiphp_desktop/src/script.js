// code by : yasserbdj96
// email : yasser.bdj96@gmail.com

//START{
var originalTitle=document.title;
//connect:
function connect(){
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
    eel.connect(key,url)(
        function(ret){
            if(ret=="connected"){
                document.title=url;
                document.getElementById("login").style.display='none';
                document.getElementById("connected").style.display='block';
                eel.ls(key,url)(function(retu){
                    var retu=JSON.parse(retu);
                    ls="<tr><th>Path</th><th>Permissions</th><th>Options</th></tr>";
                    for (let i = 0; i < retu.length; i++) {
                        var xx=retu[i].split(':');
                        var pathxx=xx[0];
                        var permxx='<a class="pointer" onclick="permi('+"'"+pathxx+"',"+"'"+xx[1]+"'"+')">'+xx[1]+'</a>';
                        var s=' ';//space
                        var edit='<a class="pointer" onclick="cat('+"'"+pathxx+"'"+')">✏️</a>'+s;
                        var del='<a class="pointer" onclick="del('+"'"+pathxx+"'"+')">❌</a>'+s;
                        var ren='<a class="pointer" onclick="ren('+"'"+pathxx+"'"+')">🎨</a>'+s;
                        var check='<input type="checkbox">';
                        //var down='<a class="pointer" onclick="down('+"'"+pathxx+"'"+')">dddd</a>'+s;
                        ls+='<tr><td>'+check+" "+pathxx+'</td><td>'+permxx+'</td><td>'+edit+ren+del+'</td></tr>';
                    }
                    document.getElementById("ls").innerHTML=ls;
                })
            }else{
                prompt("We were unable to recognize the hiphp identifier.\nCopy this code into the file whose path you entered earlier.", ret);
                document.getElementById("login").style.display='block';
                document.getElementById("connected").style.display='none';
            }
        }
    )
}
//cat:
function cat(path){
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
    eel.cat(key,url,path)(
        function(ret){
            document.getElementById("temp").innerText=path;
            document.getElementById("cat").style.display='block';
            document.getElementById("cat").value=ret;
            document.getElementById("cat").innerHTML=ret;
            document.getElementById("return").style.display='block';
            document.getElementById("save").style.display='block';
            document.getElementById("ls").style.display='none';
            document.getElementById("add").style.display='none';
            document.getElementById("reload").style.display='none';
            document.getElementById("check").style.display='none';
            document.getElementById("br").style.display='none';
            document.title=path;
        }
    )
}
//back:
function back(){
    document.getElementById("ls").style.display='revert';
    document.getElementById("add").style.display='block';
    document.getElementById("cat").innerHTML='';
    document.getElementById("temp").innerText='';
    document.getElementById("cat").style.display='none';
    document.getElementById("return").style.display='none';
    document.getElementById("save").style.display='none';
    document.getElementById("reload").style.display='block';
    document.getElementById("check").style.display='block';
    document.getElementById("br").style.display='block';
    var url=document.getElementById("url").value;
    if(url!=""){
        document.title=url;
    }else{
        document.title=originalTitle;
    }
    
}
//deconnect:
function deconnect(){
    document.getElementById("key").value="";
    document.getElementById("url").value="";
    document.getElementById("login").style.display='block';
    document.getElementById("connected").style.display='none';
    back();
}
//save:
function save(){
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
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
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
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
//rename:
function ren(path){
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
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
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
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
    var key=document.getElementById("key").value;
    var url=document.getElementById("url").value;
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
//}END.