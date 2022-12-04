import glob
import shutil
import zipfile
import os
import time
 
path_of_source = '../source/*'
path_of_destination = '../destination/'
index = 0
all_files_name = []
while True:
    object_of_source = glob.glob(path_of_source)
    if len(object_of_source) > 0 and index < len(object_of_source):
        all_obj_path  = object_of_source[index]
        if all_obj_path  not in all_files_name:
            object_of_source_path = all_obj_path .split('\\')
            name_of_file =  object_of_source_path[1].split('.')[0]
            name_of_extension = object_of_source_path[1].split('.')[1]
            print(f'\n\nWorking with file:{all_obj_path }')
            if name_of_extension == 'txt':
                every_lines  = []
                with open(all_obj_path ,'r') as source_file:
                        for lines in source_file.readlines():
                                every_lines.append(lines)
                   
                every_files = []
                print('copy the file.')
                time.sleep(1)
                for item in range(3):
                    name_of_full_file = f'{name_of_file}_{item+1}.txt'
                    with open(name_of_full_file,'w') as destination_file:
                        destination_file.write(''.join(every_lines[:(item+1)*10]))
                    destination_file.close()
                    every_files.append(name_of_full_file)
               
                print('zip the file.')
                time.sleep(1)
                name_of_zip_file = f'{name_of_file}.zip'
                path_of_zip_file = f'./{name_of_zip_file}'
                with zipfile.ZipFile(path_of_zip_file,'w') as zip_file:      
                    for item in every_files:
                        zip_file.write(item)
                        os.remove(item)
                zip_file.close()
                print('copy the zip file ')
                time.sleep(1)
                shutil.copy(path_of_zip_file,path_of_destination)
                os.remove(path_of_zip_file)
                print('extract the zip file')
                time.sleep(1)
                with zipfile.ZipFile(f'{path_of_destination}{name_of_zip_file}') as zf:
                    zf.extractall(f'{path_of_destination}')
                os.remove(f'{path_of_destination}{name_of_zip_file}')
                os.remove(all_obj_path )
                print(f'process done file:{all_obj_path }')
            elif name_of_extension == 'py':
                all_files_name.append(all_obj_path )
                index += 1
                print('Run python file:',end="")
                for i in range(5):
                    time.sleep(1)
                    print('.',end='')
                print("\n")
                try :
                    os.system(f'python {all_obj_path }')
                    os.remove(all_obj_path )
                except os.error :
                    print(os.error)
        else:
             index += 1
    else:
         index = 0