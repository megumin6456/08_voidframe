# Batch rename script for district icons
import os
import string
from pathlib import Path

print("Remove exit statement to use")
exit()

dir1 = "./exp/"
ents = Path(dir1)

for ent in ents.iterdir():
    ent.rename("./" + dir1 + ent.name.replace("frameworld", "voidframe"))