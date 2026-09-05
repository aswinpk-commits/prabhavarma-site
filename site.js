(function(){
  var root=document.documentElement;
  var saved=localStorage.getItem('pv-lang')||(navigator.language||'').startsWith('ml')?'ml':'en';
  saved=localStorage.getItem('pv-lang')||saved;
  function setLang(l){root.setAttribute('lang',l);localStorage.setItem('pv-lang',l);
    document.querySelectorAll('.lang-switch button').forEach(function(b){b.classList.toggle('on',b.dataset.lang===l)});}
  setLang(saved);
  document.querySelectorAll('.lang-switch button').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.lang)})});
  var mb=document.querySelector('.menu-btn'),nav=document.querySelector('.site-nav');
  if(mb)mb.addEventListener('click',function(){nav.classList.toggle('open')});
})();
