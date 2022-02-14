let date = new Date().getFullYear();
let copyright = document.getElementById("copyright-text")
copyright.innerHTML = `<p>\u00A9 2021 - ${date} | <a class="text-muted" id="external-contact"></a></p>`;
let toroweblink = document.getElementById("external-contact");

toroweblink.innerText = 'torswq';
toroweblink.setAttribute("href", "mailto:torswq.dev@protonmail.com");
toroweblink.setAttribute("target", "_blank");