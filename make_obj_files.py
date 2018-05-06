### This script is used to export object files from yt data ###
### Follows example code from http://yt-project.org/doc/visualizing/sketchfab.html ###
### Call with "python make_obj_files.py <density>" (or change definition in code) ###

import yt
import sys

def make_plots(path,folder,color,density):

    # Load data and set output file name
    ds = yt.load(path+folder+'/'+folder)    
    filename = './e'+str(density)+'/'+folder+'_e'+str(density)+'_'+color # Output file name

    # Set denisty and transparency (optional)
    rho = [1*10**-int(density)]
    trans = [1.0]
    sphere = ds.sphere(ds.domain_center, (300, 'kpc'))

    for i,r in enumerate(rho):
        surf = ds.surface(sphere, 'density', r)
        surf.export_obj(filename, transparency=trans[i], color_field=color, plot_index = i)

##############################

path = '/mnt/research/galaxies-REU/sims/isolated-galaxies/MW_1638kpcBox_800pcCGM_200pcDisk_lowres/'
density = sys.argv[1]

# list of data folders
folders = ['DD'+'{0:0>4}'.format(i) for i in range(2015,2500)]

# call for each folder
for folder in folders:
    make_plots(path, folder,'density',density)
    
