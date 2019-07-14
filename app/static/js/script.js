// function mostrar() {
//     let x = document.querySelector("#google_translate_element");
//     if (x.style.display == "none") {
//       x.style.display = "flex";
//     } else {
//       x.style.display = "none";
//     }  
// }

function mostrar() {
  let x = 
  document.getElementById("google_translate_element");
    if (x.style.display === "none") {
      x.style.display = "flex";
    } else {
      x.style.display = "none";
    }  
}

function googleTranslateElementInit() {
  new google.translate.TranslateElement({ pageLanguage: 'pt', includedLanguages: 'en,es,fr,ar,pt,ur', layout: google.translate.TranslateElement.InlineLayout.SIMPLE }, 'google_translate_element');
}