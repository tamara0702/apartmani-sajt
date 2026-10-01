// Teme za odeljak "Naša priča". Tekstove menjajte slobodno.
// Delovi u [uglastim zagradama] su mesta za VAŠE podatke – popunite ih ili obrišite.
const ICONS = {
  priroda: '<path d="M60 96V60"/><circle cx="60" cy="46" r="8"/><circle cx="60" cy="26" r="9"/><circle cx="80" cy="40" r="9"/><circle cx="74" cy="62" r="9"/><circle cx="46" cy="62" r="9"/><circle cx="40" cy="40" r="9"/><path d="M60 80c-14-2-22-8-26-16M60 86c14-2 22-8 26-16"/>',
  nega: '<path d="M60 100c-22-14-34-26-34-42a18 18 0 0 1 34-8 18 18 0 0 1 34 8c0 16-12 28-34 42z"/>',
  sace: '<polygon points="42,28 58,28 66,42 58,56 42,56 34,42"/><polygon points="66,42 82,42 90,56 82,70 66,70 58,56"/><polygon points="34,42 50,42 58,56 50,70 34,70 26,56"/><polygon points="42,56 58,56 66,70 58,84 42,84 34,70"/><path d="M84 96c0-10 8-10 8-20"/>',
  odrzivo: '<path d="M60 100V54"/><path d="M60 70C40 70 30 56 30 38c20 0 30 12 30 32zM60 58c0-18 10-30 30-30 0 18-10 30-30 30z"/>',
  pcele: '<ellipse cx="60" cy="64" rx="26" ry="18"/><path d="M52 47v34M64 47v34M76 52v24"/><circle cx="30" cy="62" r="9"/><ellipse cx="52" cy="38" rx="14" ry="9" transform="rotate(-25 52 38)"/><ellipse cx="72" cy="36" rx="14" ry="9" transform="rotate(20 72 36)"/><path d="M86 64h10"/>',
  hladno: '<path d="M60 22C46 44 36 56 36 72a24 24 0 0 0 48 0c0-16-10-28-24-50z"/><path d="M48 76a12 12 0 0 0 12 12"/>',
};
const STORIES = [
  { id: "priroda", title: "Pčele u svom prirodnom okruženju", text: [
    "Pčele najbolje rade tamo gde ima raznovrsnog cveća: na livadama, u voćnjacima, pored šuma i bagremovih i lipovih aleja.",
    "Od cveća koje pčele obiđu zavisi boja, miris i ukus meda, pa se livadski, bagremov i lipov med međusobno lako razlikuju.",
    "[Opišite gde se nalaze vaši pčelinjaci i šta okolo cveta.]"] },
  { id: "nega", title: "Pčelarstvo sa pažnjom i negom", text: [
    "Zdrava pčelinja društva traže stalnu pažnju: redovan pregled košnica, dovoljno hrane i mira.",
    "Pčelar prati stanje svakog društva i ne uzima više meda nego što pčele mogu da podnesu.",
    "[Napišite kako vi brinete o svojim pčelama i koliko košnica imate.]"] },
  { id: "sace", title: "Pažljivo ubran med u saću", text: [
    "Pčele same grade saće od voska i pune ga medom, a kad je zrelo, pokrivaju ga voštanim poklopcem.",
    "Med se bere tek kad je saće zatvoreno, jer je tada zreo i ima najbolji kvalitet.",
    "[Napišite kako i kad vi berete med.]"] },
  { id: "odrzivo", title: "Održivo pčelarstvo sa poštovanjem prirode", text: [
    "Pčele opršuju voće, povrće i divlje biljke, pa je briga o njima briga o celoj prirodi.",
    "Održivo pčelarstvo znači birati dobre lokacije, ne trošiti viška i ostavljati pčelama dovoljno zaliha.",
    "[Dodajte šta vi radite: bez hemije, staklene tegle, ponovna upotreba materijala...]"] },
  { id: "pcele", title: "Vredne pčele", text: [
    "Jedna pčela u toku života sakupi samo mali deo kašičice meda, a društvo ima na hiljade pčela.",
    "Za jednu teglu meda pčele obiđu ogroman broj cvetova, i zato je svaka tegla plod velikog zajedničkog truda.",
    "[Dodajte nešto lično o vašim pčelama.]"] },
  { id: "hladno", title: "Čist, hladno ceđen med", text: [
    "Med se iz saća izdvaja ceđenjem (centrifugom), bez dodatnog zagrevanja i bez dodataka.",
    "Na taj način med zadržava prirodnu aromu i ukus.",
    "[Potvrdite i opišite svoj postupak: kako ceđite, cedite li na hladno, kako punite tegle. Ne ostavljajte tvrdnje koje ne važe za vas.]"] },
];
