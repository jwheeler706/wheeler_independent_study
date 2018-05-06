import vtk
import glob, os

def make_vtk_files(path):
    print(path, type(path))
    bad_files = []
    for i,file in enumerate(glob.glob(path+"*")):
        e = file.split('/')[0]
        n_frame = int(file.split('DD')[1].split('_')[0])-50
        output_name = './'+e+'/'+e+'_vtk/'+e+'_density_'+str(n_frame)+'.vtk'
        reader = vtk.vtkOBJReader()
        reader.SetFileName(file)
        reader.Update()

        data = reader.GetOutput()
        if data.GetNumberOfCells() == 0:
            bad_files.append(j)
            
        writer = vtk.vtkXMLPolyDataWriter()
        writer.SetFileName(output_name)
        writer.SetInputData(data)
        writer.Update()
        writer.Write()
    return bad_files

path = input("Please enter the path to the data\n")
make_vtk_files(path)
