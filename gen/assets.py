import sys,os
sys.path.insert(0,'.')
import art2
os.makedirs('../public/img',exist_ok=True)
for k,f in art2.SC.items():
    t=f().replace('<svg viewBox','<svg xmlns="http://www.w3.org/2000/svg" width="600" height="520" viewBox',1).replace(' style="display:block;width:100%;height:100%"','')
    open(f'../public/img/{k}.svg','w').write(t)
