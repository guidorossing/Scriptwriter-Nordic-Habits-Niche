from PIL import Image, ImageStat, ImageFilter
import os, colorsys, statistics

def analyse(p):
    im = Image.open(p).convert('RGB').resize((320,180))
    hsv = im.convert('HSV')
    h,s,v = [list(c.getdata()) for c in hsv.split()]
    gray = im.convert('L')
    # contrast / detail
    edge = gray.filter(ImageFilter.FIND_EDGES)
    detail = ImageStat.Stat(edge).mean[0]
    # thirds luminance (waar zit het licht/onderwerp)
    w,hh = gray.size
    thirds = [ImageStat.Stat(gray.crop((i*w//3,0,(i+1)*w//3,hh))).mean[0] for i in range(3)]
    # warm vs koel: fractie pixels met hue in oranje/rood band
    warm = sum(1 for x in h if x<25 or x>230)/len(h)
    return dict(
        bright=round(statistics.mean(v),1),
        sat=round(statistics.mean(s),1),
        contrast=round(ImageStat.Stat(gray).stddev[0],1),
        detail=round(detail,1),
        warmfrac=round(warm,2),
        L=round(thirds[0]),C=round(thirds[1]),R=round(thirds[2]),
    )

for ch in ['paparuzz','celebsgoat','belmorra']:
    rows=[]
    for f in sorted(os.listdir(ch)):
        if f.endswith('.jpg'):
            rows.append((f[:-4], analyse(os.path.join(ch,f))))
    print(f"\n=== {ch} ===")
    print(f"{'video':14} {'helder':>6} {'sat':>5} {'contr':>6} {'detail':>6} {'warm':>5}   L/C/R lum")
    for name,d in rows:
        print(f"{name:14} {d['bright']:6} {d['sat']:5} {d['contrast']:6} {d['detail']:6} {d['warmfrac']:5}   {d['L']}/{d['C']}/{d['R']}")
    for k in ['bright','sat','contrast','detail','warmfrac']:
        vals=[d[k] for _,d in rows]
        print(f"  gem {k:9}= {round(statistics.mean(vals),1)}  (min {min(vals)} / max {max(vals)})")
