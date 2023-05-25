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
function login() {
    var u = document.getElementById("url").value;
    var p = document.getElementById("key").value;
    var formData = new FormData();
    formData.append('u', u);
    formData.append('p', p);
    fetch('/login', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => { if(data !== "yes!") {prompt("We were unable to recognize the hiphp identifier.\nCopy this code into the file whose path you entered earlier.", data);}else{alert('yes');}})
    .catch(error => console.error(error));
}


function search(query) {
    fetch(`/search?q=${query}`)
        .then(response => response.text())
        .then(data => document.getElementById("result").innerHTML = data);
}
//}END.