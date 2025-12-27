import os
import shutil
import subprocess

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    subprocess.check_call(["make", "-C", "sleigh", "-j", str(os.cpu_count() or 1)])
    shutil.copytree("sleigh/build/dist", "src/psleigh", dirs_exist_ok=True)
