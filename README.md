# YT to VR
### Jeff Wheeler - Independent Study Spring 2018


This respository contains the files needed to visualize simulation data in virtual reailty in Paraview.

make_obj_files.py - Creates obj and mtl files. Function takes path, folder, density, and color as input: path is the folder containing all of the different datafiles, folder is the current datafile being extracted, density is the gas density desired for the obj mesh, and color is the coloring applied in the mtl file. Multiple densities and transparencies can be definied. However, the transparency information is only added to the mtl file, which is not used in Paraview, so the default is one density per file at full opacity. User must define density when script is called.

make_vtk.py - Converts obj files to vtk files. Call with input and output paths as arguments. All of files in the input path are converted to vtk.

submit_jobs.qsub - Script to submit job to the hpcc. Time, nodes, memory, and name can be adjusted in the first few lines. At the bottom, the obj script is called, with a density defined when job script is called.


## 1. Create object files; files can be run locally or on the hpcc
* Locally - Call python script, choosing a specific density for obj mesh: <code>python make_obj_files.py \<density\></code>
* Hpcc - Call qsub script, again choosing density: <code>qsub -F \<density\> submit_jobs.qsub</code>
* Default set to 4 hours, 16gb, 4 nodes

## 2. Create vtk files for paraview
* If necessary, install vtk package (<code>pip install vtk</code> will suffice)
* Call vtk script, specifying input and output paths: <code>python make_vtk.py \<input\> \<output\></code>
* Output files should end with number corresponding to frame

## 3. View in paraview
* Put all vtk files in single directory
* In Paraview, open the file menu, all of the vtk files should aggregate together into a group
* Open the group of files and choose "VTK PolyData Files" when prompted to choose data type
* Click the eye next to the group in Paraview to show the mesh; color and transparency can be adjusted in the properties menu
* Click to send to OpenVR and press play to start the animation!

## Mini-tutorial
The data provided in the repository can be used to get an example visualization in Paraview. Untar the file with <code>tar -xf example_data.tar</code>. The object files were made with <code>python make_obj_files.py 25</code> with folders ranging from DD0950 to DD1099. Convert to vtk with <code>python make_vtk.py example_data/e25/ example_data/vtk/</code>. The files can then be opened and view in Paraview.

##

If using several layers, import each one individually. 
It is possible to grab multiple layers at once, but you have to try to grab them at a common intersection. 
Paraview can have difficulties rendering several/complex meshes and can become laggy. 
Couldn't figure out how to control the time with the remotes, but that would be very useful.

The data used in the example comes from <code>/mnt/research/galaxies-REU/sims/isolated-galaxies/MW_1638kpcBox_800pcCGM_200pcDisk_lowres/</code> on the MSU hpcc. That path contains folders with data for the simulation at certain timesteps. The python files were written with this file/naming system in mind, so some modifications might be needed to be compatible with other schemes.

