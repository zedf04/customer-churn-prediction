# Run this in a NEW python file inside C:\churnapp\
# Save as test.py and run: python test.py

from pathlib import Path
import os

BASE_DIR = Path(__file__).parent
print("BASE_DIR:", BASE_DIR)
print("Files in BASE_DIR:")
for f in BASE_DIR.iterdir():
    print(" ", f)
