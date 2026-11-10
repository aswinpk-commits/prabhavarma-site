(function(){
  var root=document.documentElement;
  function load(){try{return localStorage.getItem('pv-lang')}catch(e){return null}}
  function save(l){try{localStorage.setItem('pv-lang',l)}catch(e){}}
  var saved=load()||(((navigator.language||'').indexOf('ml')===0)?'ml':'en');
  function setLang(l){root.setAttribute('lang',l);save(l);
    document.querySelectorAll('.lang-switch button').forEach(function(b){b.classList.toggle('on',b.dataset.lang===l)});}
  setLang(saved);
  document.querySelectorAll('.lang-switch button').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.lang)})});
})();
