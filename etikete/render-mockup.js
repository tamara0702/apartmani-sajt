const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path=require('path');
(async()=>{const b=await chromium.launch();
 for(const [size,top] of [['500ml',470],['1kg',470]]){
  const pg=await b.newPage({viewport:{width:1200,height:1600}});
  await pg.goto('file://'+path.resolve('mockup/mockup.html')+`?size=${size}&top=${top}`);
  await pg.waitForFunction('window.done');
  await pg.screenshot({path:`mockup/mockup-${size}.png`,clip:{x:0,y:0,width:1200,height:1600}});
 }
 await b.close();})();
