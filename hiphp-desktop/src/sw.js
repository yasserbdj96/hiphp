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
var STATIC_CACHE_NAME = 'yasserbdj96_hiphp';
var DYNAMIC_CACHE_NAME = 'yasserbdj96_hiphp';
var CACHE_VERSION='app-v20';
var CACHE_FILES=[
    './',
    './index.html',
    //'./config.json',
    './style.css',
    './dark.css',  
    './hiphp_logo.png',
    './index.js',
    './sw.js',
    './favicon.ico',
    './include.js',
    './manifest.webmanifest',
    './script.js',
    './white.css',
    './php.py',
    './font-awesome/font-awesome.min.css',
    './font-awesome/fontawesome-webfont.svg',
    './font-awesome/fontawesome-webfont.woff',
    './font-awesome/fontawesome-webfont.eot',
    './font-awesome/fontawesome-webfont.ttf',
    './font-awesome/fontawesome-webfont.woff2',
];

/*s*/
self.addEventListener('install',(e)=>{
e.waitUntil(
  caches.open('yasserbdj96_hiphp').then((cache)=>cache.addAll(CACHE_FILES)),
);
});

self.addEventListener('fetch',(e)=>{
//console.log(e.request.url);
e.respondWith(
  caches.match(e.request).then((response)=>response||fetch(e.request)),
);
});
/*e*/

//importScripts('./cache.js');
self.addEventListener('install', function (event) {
  event.waitUntil(
      caches.open(CACHE_VERSION)
          .then(function (cache) {
              console.log('Opened cache');
              return cache.addAll(CACHE_FILES);
          })
  );
});

self.addEventListener('fetch', function (event) {
  let online = navigator.onLine
  if(!online){
      event.respondWith(
          caches.match(event.request).then(function(res){
              if(res){
                  return res;
              }
              requestBackend(event);
          })
      )
  }
});

function requestBackend(event){
  var url = event.request.clone();
  return fetch(url).then(function(res){
      //if not a valid response send the error
      if(!res || res.status !== 200 || res.type !== 'basic'){
          return res;
      }

      var response = res.clone();

      caches.open(CACHE_VERSION).then(function(cache){
          cache.put(event.request, response);
      });

      return res;
  })
}

self.addEventListener('activate', function (event) {
  event.waitUntil(
      caches.keys().then(function(keys){
          return Promise.all(keys.map(function(key, i){
              if(key !== CACHE_VERSION){
                  return caches.delete(keys[i]);
              }
          }))
      })
  )
});

//}END.