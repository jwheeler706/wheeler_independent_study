### This script converts all the object files in a folder into vtk files ###

import vtk
import glob, os

def make_vtk_files(path):
    for i,file in enumerate(glob.glob(path+"*")):

        # These lines get the names of the obj file and makes the output name
        # They might need to be adjusted based on file naming scheme
        # Output name doesn't matter except each file should end with a number
        e = file.split('/')[0]
        n_frame = int(file.split('DD')[1].split('_')[0])-50
        output_name = './'+e+'/'+e+'_vtk/'+e+'_density_'+str(n_frame)+'.vtk'

        reader = vtk.vtkOBJReader()
        reader.SetFileName(file)
        reader.Update()

        data = reader.GetOutput()
        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output_name)
        writer.SetInputData(data)
        writer.Update()
        writer.Write()

path = input("Please enter the path to the data\n")
make_vtk_files(path)
