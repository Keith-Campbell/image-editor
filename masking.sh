#!/bin/bash

# data depended info.
dataname=takenoko
original_fileplace=./takenoko/original
mask_fileplace=./takenoko/mask

# output directory
output=./output/${dataname}

# prepare output directory
mkdir ${output}/
# mask value changed
mkdir ${output}/edited_mask/
# final masked dataset
mkdir ${output}/${dataname}_dataset/
# copy mask images
cp ${mask_fileplace}/*.png ${output}/edited_mask

# image edit
while read -d $'\0' file; do
    file_num_png=${file##*/}
    output_mask_img=${output}/edited_mask/${file_num_png}
    output_image=${output}/${dataname}_dataset/${file_num_png}
    echo file=${file}
    echo file_num_png=${file_num_png}
    # remove except main object
    python3 src/main.py show $file | {
	# read pixel gray value at the center of image
        read trainue
        for i in {1..30} ; do
            if [ $i = $trainue ]; then
                :
            else
                python3 src/main.py change ${output_mask_img} -f $i -t 0 -s ${output_mask_img} 1> /dev/null
            fi
        done
    }
    python3 src/main.py mask \
        ${original_fileplace}/${file_num_png} \
        -m ${output_mask_img} \
        -s ${output_image} 1> /dev/null
    # convert to transparent images
    convert ${output_image} \
        -fuzz 0% \
        -transparent black \
	${output_image}
done < <(find ${mask_fileplace} -mindepth 1 -maxdepth 1 -print0)
