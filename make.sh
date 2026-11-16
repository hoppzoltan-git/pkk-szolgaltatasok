set -e
mkdir -p src public
cp old/SiteHeader.dc.html src/
cd gen
python3 bp.py
python3 bp2.py
python3 build.py
python3 assets.py
cd ..
node build2.mjs src public
