document.getElementById('god').textContent = new Date().getFullYear();
// Upit se otvara u email klijentu; kasnije se može zameniti servisom (npr. Formspree).
document.getElementById('upit').addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  const body = `Ime: ${f.get('ime')}\nDatumi: ${f.get('datum')}\nApartman: ${f.get('apartman')}\n\n${f.get('poruka')}`;
  location.href = 'mailto:info@example.com?subject=' + encodeURIComponent('Upit za smeštaj') + '&body=' + encodeURIComponent(body);
});
