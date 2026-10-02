const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path=require('path');
(async()=>{const b=await chromium.launch();
 const pg=await b.newPage({viewport:{width:1200,height:1600}});
 await pg.goto('file://'+path.resolve('mockup/mockup2.html'));
 await pg.waitForFunction('window.done',{timeout:20000});
 await pg.screenshot({path:'mockup/mockup-sa-papirom.png',clip:{x:0,y:0,width:1200,height:1600}});
 await b.close();})();
