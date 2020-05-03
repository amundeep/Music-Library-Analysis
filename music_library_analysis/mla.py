"""Music Library Analysis
    
Usage:
    mla.py -h
    mla.py [-i] [FILE]

Arguments:
    FILE        the MP3 file to analyze

Options:
    -h,--help   : show this help message
    -i,--info   : analyze metadata of the specified song

"""
import os
import eyed3

from docopt import docopt
from schema import Schema, And, Or, Use, SchemaError

def get_song_metadata(audiofile):
    audiofile = eyed3.load(str(audiofile))
    audiofile.initTag()
    print(audiofile.tag.file_info.name)

def main():
    docopt_args = docopt(__doc__)

    print(docopt_args)

    schema = Schema({
        '--help': False,
        '--info': True,
        'FILE': os.path.exists})

    # Validate the docopt schema
    try:
        docopt_args = schema.validate(docopt_args)
    except SchemaError as e:
        exit(e)

    if (docopt_args.get('--info') == True):
        audiofile = docopt_args.get('FILE')
        get_song_metadata(audiofile)
        print("You did --info")

if __name__ == "__main__":
    main()
