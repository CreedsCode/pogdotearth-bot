import os
import shutil

# 1. move pictures from hands with prefix hands_ in hands_nohands and nohands with prefix nohands_
for root, dir, files in os.walk("images\\hands"):
  for file in files:
    shutil.copyfile(os.path.join(root, file), f"images\\tests\\everything\\hands_{file}")

for root, dir, files in os.walk("images\\nohands"):
  for file in files:
    shutil.copyfile(os.path.join(root, file), f"images\\tests\\everything\\nohands_{file}")