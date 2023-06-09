import subprocess
from subprocess import call, PIPE, run
import datetime
import os
# the directory wordpress store backups
directory = "/wordpress/wp-content/ai1wm-backups"

# Get a list of all items (files and directories) in the directory
items = os.listdir(directory)

# record the monitor result in log
log_path = './monitor.log'

# all not compressed wordpress backup files
all_wpress = []

def main() :
    getAllWpress()
    result = str(compressFile())
    logResult(result)

# get all not compressed wordpress backup files in specify directory
def getAllWpress() :
    for each_item in items :
        split_with_dot = each_item.split('.')
        # check whether is the wordpress backup format
        if split_with_dot[len(split_with_dot)-1] == "wpress" :
            all_wpress.append(each_item)

# compress the .wpress file
def compressFile() :
    for each_wpress in all_wpress :
        file_path = directory + "/" + each_wpress
        tar_path = directory + "/" + getRealFileName(each_wpress) + ".tar"
        # compress file to tar file
        result = run(["tar", "cvf", tar_path, "--absolute-names", file_path], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        result= str(result)
        # remove .wpress file when it be compressed successfully
        if "CompletedProcess" in result and "stderr=''" in result :
            # remove .wpress file after compress it
            result = run(["rm", file_path], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        else :
            print("compress failed")
            print(result)
    return result

# get file name without sub file name, i define it as real file name
def getRealFileName(file_name) :
    split_with_dot = file_name.split('.')
    print(split_with_dot)
    real_file_name = ""
    for i in range(len(split_with_dot)-1) :
        # last dot, is dot on sub file name
        if i == len(split_with_dot)-2 :
            real_file_name += split_with_dot[i]
        # not last dot, is dot on origin real file name
        else :
            real_file_name += split_with_dot[i] + "."
    return real_file_name

def logResult(result) :
    # record the odd directory
    text_file = open(log_path, "w")
    # write into log
    text_file.write(str(datetime.datetime.now()) + " " + result + "\n")

    text_file.close()

main()
