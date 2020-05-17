import sys
import socket

def usage():
    print(sys.argv[0] + " [options] --target <ip>")
    print("Options:")
    print("--help         Display this information.")
    print("--version      Display version information.")
    print("-p <port>      Set port")
    print("-v             Set verbose mode")

verbose = False
def scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("Port " + str(port) + " is open")
        elif (verbose == True):
            print("Port " + str(port) + " is closed")
    except:
        print("Insert valid ip address and port")

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
    print("pps 1.0")
    sys.exit(0)
if "-v" in sys.argv:
    verbose = True
if "--target" in sys.argv:
    target = sys.argv[sys.argv.index("--target") + 1]
    if "-p" in sys.argv:
        port = sys.argv[sys.argv.index("-p") + 1]
        if (port == "all"):
            print("PPS - Python Port Scanner")
            fullScan(target)
        else:
            scan(target, port)
    else:
        print("Scanning first 1024 ports")
        for i in range(0, 1001):
            scan(target, i)
else:
    usage()