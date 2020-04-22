"""Music Library Analysis
    
    Usage:
        mla.py -a
        mla.py -h | --help
        mla.py <required> [-f | -g | -o ]
        mla.py <repeating>...
    Options:
        -h,--help       : show this help message
        -a              : analyze music in current directory
        repeating       : example of repeating arguments
        -f,--flag       : example flag #1
        -g,--greatflag  : example of flag #2
        -o,--otherflag  : example of flag #3
"""

from docopt import docopt

def main():
    docopt_args = docopt(__doc__)
    """ main-entry point for program, expects dict with arguments from docopt() """
    
    # Notice, no checking for -h, or --help is written here.
    # docopt will automagically check for it and use your usage string.
    
    # User passed the required argument
    if docopt_args["<required>"]:
        print("You have used the required argument: " + docopt_args["<required>"])
        
        # Get flags used
        if docopt_args["--flag"]:
            print("   with --flag\n")
        elif docopt_args["--greatflag"]:
            print("   with --greatflag\n")
        elif docopt_args["--otherflag"]:
            print("   with --otherflag\n")
        else:
            print("   with no flags.\n")
    # User passed 1 or more repeating arguments
    elif docopt_args["<repeating>"]:
        print("You have used the repeating args:")
        print('   ' + '\n   '.join(docopt_args["<repeating>"]) + '\n')

if __name__ == "__main__":
    main()
