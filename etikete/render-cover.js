const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path=require('path');
(async()=>{
 const b=await chromium.launch(); const px=206*96/25.4;
 const ctx=await b.newContext({viewport:{width:Math.ceil(px),height:Math.ceil(px)},deviceScaleFactor:300/96});
 const p=await ctx.newPage(); await p.goto('file://'+path.resolve('cover.html'));
 await p.waitForTimeout(800);
 await p.screenshot({path:'papir-za-poklopac.png',clip:{x:0,y:0,width:px,height:px}});
 await p.pdf({path:'papir-za-poklopac.pdf',width:'206mm',height:'206mm',printBackground:true,pageRanges:'1'});
 await b.close();
})();
