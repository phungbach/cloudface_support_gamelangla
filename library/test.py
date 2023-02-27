import urllib.request
import shutil
...
# Download the file from `url` and save it locally under `file_name`:
url = "https://ToolLangLa.beatdz.com/ToolLangLa/ToolLangLa.exe"

with urllib.request.urlopen(url) as response, open("ToolLangLa.exe", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)