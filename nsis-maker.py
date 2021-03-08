from string import Template


class MyTemplate(Template):
    delimiter = '&'

# Change parameters here
appname = "YourApp" # your app name
compname = "Your Company"  # your company name
descript = "App description" # App description
vmajor = 1 # Major Version
vminor = 0 # Minor Version
vbuild = 0 # Build Version
helpurl = "https://www.yourapp.com/help" # Help URL
updateurl = "https://www.yourapp.com/update" # Update URL
abouturl = "https://www.yourapp.com/about" # About URL
installsize = 49368 # Installation size in Kb
iconpath = "src/images/yourico.ico" # Icon path of your app
builder = "py" # Compilation used

# ---------------------------------------------------------------#


outfile = f'{appname.replace(" ", "")}-installer-{vmajor}{vminor}{vbuild}-{builder}.exe'
iconpathrev = iconpath.replace("/", '\\')
iconpathrev = f"\\{iconpathrev}"


d = {
    'appname': appname,
    'compname': compname,
    "descript": descript,
    "vmajor": vmajor,
    "vminor": vminor,
    "vbuild": vbuild,
    "helpurl": helpurl,
    "updateurl": updateurl,
    "abouturl": abouturl,
    "installsize": installsize,
    "iconpath": iconpath,
    "outfile": outfile,
    "iconpathrev": iconpathrev,
}

with open('nsis_template.txt', 'r') as f:
    src = MyTemplate(f.read())
    result = src.substitute(d)

with open(f'{appname}-installer-{vmajor}{vminor}{vbuild}.txt', 'w') as g:
    g.write(result)
