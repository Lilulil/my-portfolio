(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) { return; }
  if (!('IntersectionObserver' in window)) { return; }
  var targets = document.querySelectorAll('#posts .portfolio-item, #journal-section .cert-plate');
  if (!targets.length) { return; }
  Array.prototype.forEach.call(targets, function (el) { el.classList.add('reveal-ready'); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) { return; }
      var el = entry.target;
      var item = el.closest('.item');
      var idx = item ? Array.prototype.indexOf.call(item.parentElement.children, item) : 0;
      el.style.animationDelay = ((idx % 2) * 100) + 'ms';
      el.classList.remove('reveal-ready');
      el.classList.add('reveal-in');
      io.unobserve(el);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
  Array.prototype.forEach.call(targets, function (el) { io.observe(el); });
  Array.prototype.forEach.call(document.querySelectorAll('#filters a'), function (link) {
    link.addEventListener('click', function () {
      setTimeout(function () {
        Array.prototype.forEach.call(document.querySelectorAll('#posts .item'), function (item) {
          if (item.style.display !== 'none') {
            var inner = item.querySelector('.portfolio-item');
            if (inner) { inner.classList.remove('reveal-ready'); inner.classList.add('reveal-in'); }
          }
        });
      }, 120);
    });
  });
})();
