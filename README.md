# YT to VR
### Jeff Wheeler - Independent Study Spring 2018


This respository contains the files needed to visualize simulation data in virtual reailty in Paraview.

make_obj_files.py - Creates obj and mtl files. Function takes path, folder, density, and color as input: path is the folder containing all of the different datafiles, folder is the current datafile being extracted, density is the gas density desired for the obj mesh, and color is the coloring applied in the mtl file. Multiple densities and transparencies can be definied. However, the transparency information is only added to the mtl file, which is not used in Paraview, so the default is one density per file at full opacity. User must define density when script is called.

make_vtk.py - Converts obj files to vtk files. Prompts the user for the path to the object files, and converts all files to vtk.

submit_jobs.qsub - Script to submit job to the hpcc. Time, nodes, memory, and name can be adjusted in the first few lines. At the bottom, the obj script is called, with a density defined when job script is called.


## 1. Create object files; files can be run locally or on the hpcc
* Locally - Call python script, choosing a specific density for obj mesh: "python make_obj_files.py <density>"
* Hpcc - Call qsub script, again choosing density: "qsub -F <density> submit_jobs.qsub"
* Default set to 4 hours, 16gb, 4 nodes

## 2. Create vtk files for paraview
* Call vtk script
* Script prompts user for path to object files
* Output files should end with number corresponding to frame

## 3. View in paraview
* Put all vtk files in single directory
* In Paraview, open the file menu
* All of the vtk files should aggregate together into a group
* Open the group of files and choose "VTK PolyData Files" when prompted to choose data type
* Click the eye next to the group in Paraview to show the mesh
* Color and transparency can be adjusted in the properties menu
* Click to send to OpenVR and press play to start the animation!

If using several layers, import each one individually. 
It is possible to grab multiple layers at once, but you have to try to grab them at a common intersection. 
Paraview can have difficulties rendering several/complex meshes and can become laggy. 
Couldn't figure out how to control the time with the remotes, but that would be very useful.