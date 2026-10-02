const {chromium}=require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{
 const {jobs,dpi}=JSON.parse(fs.readFileSync(path.join(__dirname,'.jobs.json')));
 const br=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 for(const [fn,wmm,hmm] of jobs){
  const wpx=Math.round(wmm/25.4*dpi), hpx=Math.round(hmm/25.4*dpi);
  const svg=fs.readFileSync(path.join(__dirname,fn+'.svg'),'utf8').replace(/width="[\d.]+mm" height="[\d.]+mm"/,`width="${wpx}" height="${hpx}"`);
  const pg=await br.newPage({viewport:{width:wpx,height:hpx}});
  await pg.setContent(`<html><body style="margin:0">${svg}</body></html>`);
  await pg.screenshot({path:path.join(__dirname,fn+'.png')});
  if(!fn.endsWith('-pregled')){
    const svgmm=fs.readFileSync(path.join(__dirname,fn+'.svg'),'utf8');
    await pg.setContent(`<html><head><style>@page{size:${wmm}mm ${hmm}mm;margin:0}body{margin:0}</style></head><body>${svgmm}</body></html>`);
    await pg.pdf({path:path.join(__dirname,fn+'.pdf'),width:wmm+'mm',height:hmm+'mm',printBackground:true});
  }
  console.log(fn,wpx+'x'+hpx);
 }
 await br.close();
})();
