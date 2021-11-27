#!/usr/bin/python
#DT: 10.02.2019
#@Priyanka.numbhuri
#Script to tar/untar folder or files



import sys
import os
import tarfile;
import glob
import shutil

#<maketar> <source_dir>  <outputfile_name>
#<extracttar> <outputfile_name>

def usage():
    print ("USAGE is:")
    print ("For creating tarball: python tar_untar.py maketar <source_dir>  <outputfile_name>")
    print ("For extracting tarball: python tar_untar.py extracttar <tar_file_name>")

def initial_checks():
    try:
        global source_dir
        global output_filename
        if len(sys.argv) == 1:
            usage()
            sys.exit(1)
        if sys.argv[1] == 'maketar':
            if len(sys.argv) >= 4:
                source_dir = sys.argv[2]
                output_filename = sys.argv[3]
            else:
                print ("The number of arguements are invalid!!!")
                usage()
                sys.exit(1)
        elif sys.argv[1] == 'extracttar':
            if len(sys.argv) >= 3:
                output_filename = sys.argv[2]
            else:
                print ("The number of arguements are invalid")
                usage()
                sys.exit(1)
        else:
            print ("The arguement is invalid")
            usage()
            sys.exit(1)
    except:
        print ("The number of arguements are invalid.. ")
        usage()
        sys.exit(1)



def make_tarfile(output_filename, source_dir):
    import tarfile
    tar = tarfile.open(output_filename, "w:gz")
    tar.add(source_dir, arcname=os.path.basename(source_dir))
    cmd="cksum " + output_filename
    #os.system(cmd)
    os.system(cmd + " > tmp_tar_untar.log")


def extract_tarfile(output_filename):
    import tarfile
    if (output_filename.endswith("tar.gz")):
        tar = tarfile.open(output_filename, "r:gz")
        tar.extractall()
        tar.close()
    elif (output_filename.endswith("tar")):
        tar = tarfile.open(output_filename, "r:")
        tar.extractall()
        tar.close()



#Main
old_stdout = sys.stdout
log_file = open("tar_untar.log","w")
sys.stdout = log_file
print ("Starting with tar or untar operation")
initial_checks()
if sys.argv[1] == 'maketar':
    make_tarfile(output_filename,source_dir)
    print ("The tarball ", output_filename , "has been created!!!")
elif sys.argv[1] == 'extracttar':
    extract_tarfile(output_filename)
    print ("The tarball ", output_filename , "has been extracted!!!")

sys.stdout = old_stdout
log_file.close()
cmd="cat tmp_tar_untar.log >> tar_untar.log; rm -rf tmp_tar_untar.log"
os.system(cmd)