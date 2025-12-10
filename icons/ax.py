from pathlib import Path
import subprocess

# Batch rename & convert script

PNG_DIR = "./exp/" # all pngs with district_ will be renamed
DDS_DIR = "./cvt/" # makes copies overwrite if found

# Using texconv utility from: https://github.com/microsoft/DirectXTex
TEXCONV_PATH = "E:/soft/utils/texconv.exe"
PREFIX = "district_xhk_"

# rename string - must be same size as each other
RENAME_FROM = []
RENAME_TO = []

print("Remove exit statement to use")
exit()

pngDir = Path(PNG_DIR)

print("> Renaming PNGs\n")

for file in pngDir.iterdir():
    orgExt = file.suffix
    orgName = file.stem

    if not orgExt == ".png":
        continue

    if not orgName.find(PREFIX):
        continue
    
    if orgName.endswith("_1"):
        orgNameTrunc = orgName.replace("_1", "")
        newSuffix = "_se"
    elif orgName.endswith("_2"):
        orgNameTrunc = orgName.replace("_2", "")
        newSuffix = "_pe"
    elif orgName.endswith("_3"):
        orgNameTrunc = orgName.replace("_3", "")
        newSuffix = "_te"
    elif orgName.endswith(" (0-00-00-00)"):
        orgNameTrunc = orgName.replace(" (0-00-00-00)", "")
        newSuffix = "_dm"
    else:
        newSuffix = "_de"
        orgNameTrunc = orgName
    
    orgNameTrunc = orgNameTrunc.replace("district_", PREFIX)
    newName = orgNameTrunc + newSuffix + orgExt
    
    print(f" - \"{newName}\"" )
    file.rename(f"{PNG_DIR}/{newName}")

print("\n> Replace Name\n")

for file in pngDir.iterdir():
    idx = 0
    for nameFrom in RENAME_FROM:
        fName = file.name
        if not fName.find(nameFrom) == -1:
            fName = fName.replace(nameFrom, RENAME_TO[idx])
            print(f" - {file.name.replace(PREFIX, "")} > {fName.replace(PREFIX, "")}")
            file.rename(f"{PNG_DIR}/{fName}")
        idx += 1

print("\n> Convert to DDS\n")

for file in pngDir.iterdir():
    orgExt = file.suffix
    orgName = file.stem

    if not orgExt == ".png":
        continue

    if orgName.find(PREFIX):
        continue

    Path(DDS_DIR).mkdir(parents=True, exist_ok=True)

    # texconv --format B8G8R8A8_UNORM --mip-levels 1 -y district_city.png
    cmdArgs = [TEXCONV_PATH,
               "--format", "B8G8R8A8_UNORM",
               "--mip-levels", "1",
               "-y", # Overwrite file
               "-o", DDS_DIR, # Output path
               str(file.resolve())]
    
    print(f" - {orgName}.dds")
    try:
        subprocess.run(cmdArgs, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"   - Failed")

print("\n> Script Complete")