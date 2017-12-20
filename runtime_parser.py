import sys

def process_runtime_arguments():
    """Process runtime parameters
    
    Returns:
        (:obj: 'list'): runtime parameters
    """

    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        
        file = open(".README.txt",'r')
        print file.read()
        sys.exit(1)

    argvs = []
    for i in range(len(sys.argv)):
        argvs.append(sys.argv[i])

    return argvs

argvs = process_runtime_arguments()

# Get the the values of the runtime parameters
data = argvs[1]
verbose = True if "-v" in argvs else False
k = int(argvs[argvs.index("-k") + 1]) if "-k" in argvs else 5
size = argvs[argvs.index("--size") + 1] if "--size" in argvs else "n"
w = argvs[argvs.index("-w") + 1] if "-w" in argvs else "m"
target = argvs[argvs.index("--target") + 1] if "--target" in argvs else ""
test = True if "--target" in argvs else False
sp = argvs[argvs.index("-sp") + 1] if "-sp" in argvs else "0.5"
rt = True if "-rt" in argvs else False
headless = True if "--nohead" in argvs else False

