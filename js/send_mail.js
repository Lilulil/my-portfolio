/* Contact form — no backend, no third-party server.
   Old version posted to developerfolio-server.onrender.com (a template author's demo server),
   so messages never reached the owner. Now: open WhatsApp with the message pre-filled,
   and offer email as a fallback. */

(function () {
  var form = document.getElementById('contactForm');
  if (!form) return;

  var WA = '6281952387500';
  var MAIL = 'uabshor43@gmail.com';

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var name = (document.getElementById('name').value || '').trim();
    var email = (document.getElementById('email').value || '').trim();
    var message = (document.getElementById('message').value || '').trim();
    var status = document.getElementById('status');
    var btn = document.getElementById('submitButton');

    if (!name || !email || !message) {
      status.innerHTML = '<p style="color:#ff8a65;font-size:16px;font-weight:500;">Please fill in name, email and message.</p>';
      return;
    }

    var text = 'Hi Ulil, I found your portfolio.\n\nName: ' + name + '\nEmail: ' + email + '\n\n' + message;
    var waUrl = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text);
    var mailUrl = 'mailto:' + MAIL + '?subject=' + encodeURIComponent('Project inquiry from ' + name)
                + '&body=' + encodeURIComponent(text);

    btn.value = 'Opening WhatsApp…';
    window.open(waUrl, '_blank');

    status.innerHTML =
      '<p style="color:#8fe388;font-size:16px;font-weight:500;">WhatsApp opened in a new tab. If nothing happened, ' +
      '<a href="' + mailUrl + '" style="color:#8fe388;text-decoration:underline;">send it by email instead</a>.</p>';
    btn.value = 'Send Message';
  });
})();
