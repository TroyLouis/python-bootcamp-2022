import zipfile
import shutil

f = open('zipfile1.txt', 'w+')
f.write("ONE")
f.close()

f = open('zipfile2.txt', 'w+')
f.write("TWO")
f.close()

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('zipfile1.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('zipfile2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')

dir_to_zip = '/Users/troy/Desktop/python-bootcamp-2022/advanced_modules/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')