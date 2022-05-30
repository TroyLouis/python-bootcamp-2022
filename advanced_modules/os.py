import os
import shutil

with open('practice.txt', 'w+') as f:
    f.write('Test')
    f.close()

if __name__ == "__main__":
    print(os.getcwd())
    print(os.listdir())