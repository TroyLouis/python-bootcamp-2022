import os
import shutil
import send2trash

with open('practice.txt', 'w+') as f:
    f.write('Test\n')
    f.write('Hotdog')
    f.close()

# Most likely permanent removal
# os.unlink(path)
# os.rmdir(path)
# shutil.rmtree(path) # dangerous removal method if mistakes, beware

# removal method that sends to trash, less permanent
#send2trash.send2trash('practice.txt')

for folder, sub_folders, files in os.walk(os.getcwd()):
    print(folder)
    print(sub_folders)
    print(files)

if __name__ == "__main__":
    pass
    #print(os.getcwd())
    #print(os.listdir())