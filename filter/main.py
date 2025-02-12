import filter 
import sys


# Image filter dict
filters = {
    "-g": "grey", 
    "-s": "sharpen", 
    "-r": "reflect", 
    "-i": "invert", 
    "-b": "blur", 
    "-e": "emboss", 
    "-c": "contour", 
    "-d": "detail", 
    "-ed": "edge", 
}

if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[2]:
        print("Usage: python main.py <flag> <image>")
        sys.exit(1)

    flag = sys.argv[1]
    file = sys.argv[2]

    if flag in filters:
        function = getattr(filter, filters[flag])
        if function:
            image = function(file)
            image.show()
        else:
            print("Invalid filter function")
            sys.exit(1)
    else:
        print("Invalid flag")
        sys.exit(1)
