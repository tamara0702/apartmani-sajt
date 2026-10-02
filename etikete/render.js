const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(async()=>chromium.launch());
  const sizes = { '1kg':[92,158.8], '500ml':[91,122] };
  for (const style of (process.argv[2]||'front,back').split(',')) for (const [size,[w,h]] of Object.entries(sizes)) {
    const pxw = Math.round(w*96/25.4*1000)/1000, pxh = Math.round(h*96/25.4*1000)/1000;
    const ctx = await b.newContext({ viewport:{width:Math.ceil(pxw),height:Math.ceil(pxh)}, deviceScaleFactor:300/96 });
    const p = await ctx.newPage();
    await p.goto('file://'+path.resolve('etiketa.html')+`?style=${style}&size=${size}`);
    await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(800);
    const name = `etiketa-${size}-${style}`;
    await p.screenshot({ path:name+'.png', clip:{x:0,y:0,width:pxw,height:pxh} });
    await p.pdf({ path:name+'.pdf', width:w+'mm', height:h+'mm', printBackground:true, pageRanges:'1' });
    await ctx.close();
  }
  await b.close();
})();
