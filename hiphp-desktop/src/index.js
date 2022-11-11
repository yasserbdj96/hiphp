/*s*/
/*function loadJSON(callback) {   
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open('GET','./sw.json',true);
  xobj.onreadystatechange = function () {
    if (xobj.readyState == 4 && xobj.status == "200") {
      callback(JSON.parse(xobj.responseText));
    }
  };
  xobj.send(null);  
}

var ss=loadJSON(function(json){
	var data="";
	for(i=0;i<json.length;i++){
		if(data==""){var bar='"';}else{var bar=',"';}
		data+=bar+json[i]+'"';
	}
	return;
});
console.log(ss);*/

// Register service worker to control making site work offline
if ('serviceWorker' in navigator){
  navigator.serviceWorker
    .register('./sw.js')
    .then(() => {
	
	console.log('Service Worker Registered'); 
	});
}



var download_pwa = document.getElementsByClassName('download_pwa');
if (download_pwa.length > 0){
    // Code to handle install prompt on desktop
    let deferredPrompt;
    const addBtn = document.querySelector('.download_pwa');
    addBtn.style.display = 'none';

  window.addEventListener('beforeinstallprompt',(e)=>{
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
    // Update UI to notify the user they can add to home screen
    addBtn.style.display = 'block';

    addBtn.addEventListener('click', () => {
      // hide our user interface that shows our A2HS button
      addBtn.style.display = 'none';
      // Show the prompt
      deferredPrompt.prompt();
      // Wait for the user to respond to the prompt
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the A2HS prompt');
        } else {
          console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
      });
    });
  });
}

/*e*/
