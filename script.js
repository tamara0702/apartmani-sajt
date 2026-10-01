// ====== PODEŠAVANJA – ovde menjate cene i kontakt ======
const PHONE = "38162755336"; // 062 755 336 u međunarodnom formatu, bez +
const HONEYS = [
  { id: "livadski", name: "Livadski med", price900: 1500, price390: 800 }, // cene su probne – izmenite ih!
  { id: "bagremov", name: "Bagremov med", price900: 1500, price390: 800 },
  { id: "lipov",    name: "Lipov med",    price900: 1500, price390: 800 },
];
// =========================================================

const fmt = n => n.toLocaleString("sr-RS") + " RSD";
const products = [];
HONEYS.forEach(h => [["900", "tegla 900 ml"], ["390", "šestougaona tegla 390 ml"]].forEach(([size, label]) =>
  products.push({ key: h.id + size, name: h.name, label, size, price: h["price" + size], img: `img/${size}-${h.id}.png` })));
const qty = {};

const grid = document.getElementById("products");
grid.innerHTML = products.map(p => `
  <article class="card">
    <img src="${p.img}" alt="${p.name}, ${p.label}" loading="lazy">
    <h3>${p.name}</h3>
    <p class="size">${p.label}</p>
    <p class="price">${fmt(p.price)}</p>
    <div class="qty">
      <button type="button" data-k="${p.key}" data-d="-1" aria-label="Manje">−</button>
      <output id="q-${p.key}">0</output>
      <button type="button" data-k="${p.key}" data-d="1" aria-label="Više">+</button>
    </div>
  </article>`).join("");

grid.addEventListener("click", e => {
  const b = e.target.closest("button[data-k]");
  if (!b) return;
  const k = b.dataset.k;
  qty[k] = Math.max(0, (qty[k] || 0) + Number(b.dataset.d));
  document.getElementById("q-" + k).textContent = qty[k];
  renderCart();
});

function items() { return products.filter(p => qty[p.key] > 0); }
function total() { return items().reduce((s, p) => s + p.price * qty[p.key], 0); }

function renderCart() {
  const list = document.getElementById("cart-list");
  const its = items();
  list.innerHTML = its.length
    ? its.map(p => `<li><span>${qty[p.key]} × ${p.name}, ${p.label}</span><strong>${fmt(p.price * qty[p.key])}</strong></li>`).join("")
    : '<li class="empty">Korpa je prazna. Izaberite med iznad.</li>';
  document.getElementById("cart-total").textContent = fmt(total());
}

document.getElementById("order-form").addEventListener("submit", e => {
  e.preventDefault();
  const f = e.target, err = document.getElementById("form-error");
  err.textContent = "";
  if (!items().length) { err.textContent = "Izaberite bar jednu teglu meda."; return; }
  for (const n of ["ime", "telefon", "adresa", "mesto"])
    if (!f[n].value.trim()) { err.textContent = "Popunite sva obavezna polja."; f[n].focus(); return; }

  const lines = items().map(p => `- ${qty[p.key]} × ${p.name}, ${p.label} (${fmt(p.price * qty[p.key])})`);
  const text = [
    "Porudžbina – Dedin med organic", "", ...lines, "", "Ukupno: " + fmt(total()) + " (plaćanje pouzećem)", "",
    "Ime: " + f.ime.value.trim(), "Telefon: " + f.telefon.value.trim(),
    "Adresa: " + f.adresa.value.trim() + ", " + f.mesto.value.trim(),
    f.napomena.value.trim() ? "Napomena: " + f.napomena.value.trim() : "",
  ].filter((l, i, a) => l !== "" || a[i - 1] !== "").join("\n");

  const enc = encodeURIComponent(text);
  document.getElementById("send-viber").href = "viber://chat?number=%2B" + PHONE + "&draft=" + enc;
  document.getElementById("send-wa").href = "https://wa.me/" + PHONE + "?text=" + enc;
  document.getElementById("send-sms").href = "sms:+" + PHONE + "?&body=" + enc;
  document.getElementById("send-text").textContent = text;
  const box = document.getElementById("send-box");
  box.hidden = false;
  box.scrollIntoView({ behavior: "smooth", block: "center" });
});


// ====== Naša priča: kartice + prozor ======
const sgrid = document.getElementById("story-grid");
sgrid.innerHTML = STORIES.map(s => `
  <button class="story" type="button" data-id="${s.id}">
    <span class="story-media">
      <svg viewBox="0 0 120 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">${ICONS[s.id]}</svg>
      <img src="img/price/${s.id}-1.jpg" alt="" loading="lazy" onerror="this.remove()">
    </span>
    <span class="story-title">${s.title}</span>
  </button>`).join("");

const modal = document.getElementById("story-modal");
sgrid.addEventListener("click", e => {
  const b = e.target.closest(".story");
  if (!b) return;
  const s = STORIES.find(x => x.id === b.dataset.id);
  document.getElementById("story-title").textContent = s.title;
  document.getElementById("story-text").innerHTML = s.text.map(t => t.startsWith("[") ? `<p class="todo">${t}</p>` : `<p>${t}</p>`).join("");
  const box = document.getElementById("story-imgs");
  box.innerHTML = "";
  [1, 2, 3].forEach(i => {
    const im = new Image();
    im.alt = s.title;
    im.onload = () => box.append(im);
    im.src = `img/price/${s.id}-${i}.jpg`;
  });
  modal.showModal();
});
modal.addEventListener("click", e => { if (e.target === modal || e.target.closest(".modal-x")) modal.close(); });
