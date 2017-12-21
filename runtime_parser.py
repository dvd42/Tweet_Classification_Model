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
target = argvs[argvs.index("--target") + 1] if "--target" in argvs else ""
sp = argvs[argvs.index("-sp") + 1] if "-sp" in argvs else "0.3"
rt = True if "-rt" in argvs else False
headless = True if "--nohead" in argvs else False

