import sys
import socket

onfile = False
if "-o" in sys.argv:
    onfile = True
    try:
        filename = sys.argv[sys.argv.index("-o") + 1]
        f = open(filename, 'w')
    except:
        print("cannot create or open output file")
def output(message):
    if onfile == False:
        print(message)
    else:
        f.write(message + "\n")

def usage():
    output(sys.argv[0] + " [options] --target <ip>")
    output("Options:")
    output("--help         Display this information.")
    output("--version      Display version information.")
    output("-p <port>      Set port")
    output("-v             Set verbose mode")
    output("-o             Set output file")

verbose = False
def scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            output("Port " + str(port) + " is open")
        elif (verbose == True):
            output("Port " + str(port) + " is closed")
    except:
        output("Insert valid ip address and port")

def fullScan(ip):
    for i in range(0, 65536):
        scan(ip, i)

if len(sys.argv)==1:
    print("PPS - Python Port Scanner")
    usage()
    sys.exit(-1)
if "--help" in sys.argv:
    usage()
    sys.exit(0)
if "--version" in sys.argv:
    output("PPS 1.0")
    sys.exit(0)

if "-v" in sys.argv:
    verbose = True
if "--target" in sys.argv:
    target = sys.argv[sys.argv.index("--target") + 1]
    if "-p" in sys.argv:
        port = sys.argv[sys.argv.index("-p") + 1]
        if (port == "all"):
            output("PPS - Python Port Scanner")
            fullScan(target)
        else:
            output("PPS - Python Port Scanner")
            scan(target, port)
    else:
        output("PPS - Python Port Scanner")
        output("Scanning first 1024 ports")
        for i in range(0, 1024):
            scan(target, i)
else:
    usage()
