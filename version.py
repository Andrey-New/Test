import sys

#print(sys.path)

print(str(sys.version_info.major) + " " + str(sys.version_info.minor) + " " + str(sys.version_info.micro))


if not (sys.version_info.major == 3 and sys.version_info.minor >= 5):
    print("This script requires Python 3.5 or higher!")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)