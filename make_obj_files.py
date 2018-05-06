import yt
import sys

def make_plots(folder,color,idk_what_this_number_means):
    ds = yt.load('/mnt/research/galaxies-REU/sims/isolated-galaxies/MW_1638kpcBox_800pcCGM_200pcDisk_lowres/'+folder+'/'+folder)
    
    filename = './e'+str(idk_what_this_number_means)+'/'+folder+'_e'+str(idk_what_this_number_means)+'_'+color
    rho = [1*10**-int(idk_what_this_number_means)]#,1e-25,1e-26,1e-27]
    print(rho)
    trans = [1.0]#,0.50,0.25]
    sphere = ds.sphere(ds.domain_center, (300, 'kpc'))

    for i,r in enumerate(rho):
        surf = ds.surface(sphere, 'density', r)
        surf.export_obj(filename, transparency=trans[i], color_field=color, plot_index = i)

##############################

folders = ['DD'+'{0:0>4}'.format(i) for i in range(2015,2500)]
#folders = ['DD0914']

weird_number = sys.argv[1]

for folder in folders:
    make_plots(folder,'density',weird_number)
    #make_plots(folder,'metallicity')
    
