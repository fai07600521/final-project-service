# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.




"""Generate images using pretrained network pickle."""

import os
from pprint import pprint
import re
from typing import List, Optional
import sys
import traceback

import pickle
import dnnlib
import numpy as np
import PIL.Image
import torch
from io import BytesIO
import mysql.connector
import base64
from PIL import Image

import legacy
CUDA_VISIBLE_DEVICES=0
mydbCloud = mysql.connector.connect(
        host="103.74.253.121",
        user="root",
        password="123456",
        database="fask" # Name of the database
)


# Create a cursor object


#----------------------------------------------------------------------------

def num_range(s: str) -> List[int]:
    '''Accept either a comma separated list of numbers 'a,b,c' or a range 'a-c' and return as a list of ints.'''

    range_re = re.compile(r'^(\d+)-(\d+)$')
    m = range_re.match(s)
    if m:
        return list(range(int(m.group(1)), int(m.group(2))+1))
    vals = s.split(',')
    return [int(x) for x in vals]

#----------------------------------------------------------------------------


def generate_images(
    network_pkl: r"C:\Users\Admin\temp\stylegan2-ada-pytorch\sexy\network-snapshot-000920.pkl",
    seeds:[10,2000,20000,200000],
    outdir: r"C:\Users\Admin\temp\stylegan2-ada-pytorch\sexy",
    projected_w: None,
    class_idx: 1,
    truncation_psi: 0.5,
    noise_mode: 'const'
):
    print('Loading networks from "%s"...' % network_pkl)
    device = torch.device('cpu')
    with dnnlib.util.open_url(network_pkl) as f:
         G = legacy.load_network_pkl(f)['G_ema'].to(device) # type: ignore

    '''os.makedirs(outdir, exist_ok=True)

    # Synthesize the result of a W projection.
    if projected_w is not None:
        if seeds is not None:
            print ('warn: --seeds is ignored when using --projected-w')
        print(f'Generating images from projected W "{projected_w}"')
        ws = np.load(projected_w)['w']
        ws = torch.tensor(ws, device=device) # pylint: disable=not-callable
        assert ws.shape[1:] == (G.num_ws, G.w_dim)
        for idx, w in enumerate(ws):
            img = G.synthesis(w.unsqueeze(0))
            img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
            img = PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB').save(f'{outdir}/proj{idx:02d}.png')
        return

    if seeds is None:
        ctx.fail('--seeds option is required when not using --projected-w')

    # Labels.
  
    label = torch.zeros([1, G.c_dim], device=device)
    if G.c_dim != 0:
        if class_idx is None:
            ctx.fail('Must specify class label with --class when using a conditional network')
        label[:, class_idx] = 1
    else:
        if class_idx is not None:
            print ('warn: --class=lbl ignored when running on an unconditional network')'''

    # Generate images.

 
    i = 0
    count = 1
    outdir = r"D:\New folder (3)\folderImg\Data"
    for seed_idx, seed in enumerate(seeds):
        try:
            print('Generating image for seed %d (%d/%d) ...' % (seed, seed_idx, len(seeds)))
            z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)
            c = None
            w = G.mapping(z, c, truncation_psi=0.5, truncation_cutoff=8)
            img = G.synthesis(w, noise_mode='const', force_fp32=True)
            img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
            print("fileList 3")
            img2 = PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB')
            img3 = PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB').save(f'{outdir}/seed{seed:04d}.png')
            print("fileList 4")
            fileList = []
            fileList.append(img2)       
            print("fileList")
            print(fileList)
            if (count == 1) : 
                    count = count + 1
                    print(i == 0)
                    cursor = mydbCloud.cursor()
                    queryDelete = 'DELETE FROM classy'
                    cursor.execute(queryDelete)
                    mydbCloud.commit()

            for	i in range(len(fileList)):

                # Open a file in binary mode
                buff = BytesIO()
                fileList[i].save(buff, format="png")
                img_str = base64.b64encode(buff.getvalue()).decode('utf-8')
                pprint(img_str)
                    # We must encode the file to get base64 string
                    # Sample data to be inserted
                args = (i,img_str, 'Sample Name')
                    
                    # Prepare a query
                query = 'INSERT INTO classy(ID,file,name) VALUES(%s,%s, %s)'

                    # Execute the query and commit the database.
                cursor.execute(query,args)
                mydbCloud.commit()
        except AssertionError:
                _, _, tb = sys.exc_info()
                traceback.print_tb(tb) # Fixed format
                tb_info = traceback.extract_tb(tb)
                filename, line, func, text = tb_info[-1]

                print('An error occurred on line {} in statement {}'.format(line, text))
                exit(1)
        
        
def getData():
    if (count == 1) : 
                    count = count + 1
                    print(i == 0)
                    cursor = mydbCloud.cursor()
                    queryDelete = 'DELETE FROM classy'
                    cursor.execute(queryDelete)
                    mydbCloud.commit()



#----------------------------------------------------------------------------

if __name__ == "__main__":
    generate_images(
        r"C:\Users\Admin\temp\stylegan2-ada-pytorch\streetset\network-snapshot-000440.pkl",
        [10,2000,20000,200000],
        r"C:\Users\Admin\temp\stylegan2-ada-pytorch\streetset",
        None,
        1
    )
# pylint: disable=no-value-for-parameter

#----------------------------------------------------------------------------
