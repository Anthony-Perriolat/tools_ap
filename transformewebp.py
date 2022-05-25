
# cmd> python cwebp_compressor.py folder-name

import sys
from subprocess import call
from glob import glob

#folder-name
path = sys.argv[1]

img_list = []
for img_name in glob(path+'/*'):
    # one can use more image types(bmp,tiff,gif)
    if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
        # extract images name(image_name.[jpg|png]) from the full path
        img_list.append(img_name.split('\\')[-1])


# print(img_list)   # for debug
for img_name in img_list:
    # though the chances are very less but be very careful when modifying the below code
    cmd='cwebp '+img_name+' -o '+(img_name.split('.')[0])+'.webp'
    # running the above command
    print(cmd)    # for debug
    call(cmd, shell=True)
