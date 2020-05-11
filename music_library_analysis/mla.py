"""Music Library Analysis
    
Usage:
    mla.py -h
    mla.py [-tf PATH] [--debug]

Arguments:
    PATH        the MP3 file or directory containing MP3 files to analyze

Options:
    -h,--help       : show this help message
    -t,--tag        : show id3 tags of an MP3 file at PATH
    -f,--folder     : include all mp3 files in folder PATH (includes subfolders)
    --debug         : set log level to DEBUG

"""
import os
import eyed3
import coloredlogs, logging
import glob

from docopt import docopt
from schema import Schema, And, Or, Use, SchemaError, Optional
from pathlib import Path

from music_library_analysis.model.mlamp3 import MP3Model

# Create a logger object named 'mla'
logger = logging.getLogger('mla')
coloredlogs.install(level='DEBUG', fmt='%(name)s - %(levelname)s - %(message)s', logger=logger)
logger.setLevel(logging.INFO) # Set to logging.DEBUG to see debug messages

def get_mp3_filepaths_in_dir(dirpath):
    """Helper function to get all mp3s in folder and subfolders"""
    mp3_path_list = []
    for (root, dirs, files) in os.walk(str(dirpath)):
        for file in files:
            if(file.endswith(".mp3")):
                mp3_path_list.append(os.path.join(root, file))
    return mp3_path_list

def get_mp3_files(filepath):
    """Validates given filepath and returns a tuple of relevant mp3 files"""
    if(filepath != None and os.path.exists(filepath)):
        path = Path(filepath) # create path object
        filename = os.path.basename(path)
        mp3paths = []
        is_dir = False

        # Check if mp3 or directory
        if(path.suffix == '.mp3'):
            logger.info("You've provided an mp3 file")
            mp3paths.append(str(path))
        elif(path.is_dir):
            logger.info("You've provided a directory")
            is_dir = True
            mp3paths = get_mp3_filepaths_in_dir(path).copy()

        num_mp3s = len(mp3paths)

        if(num_mp3s == 0):
            logger.error("No MP3 files found in directory, please provide another")
            exit()
        elif(is_dir):
            logger.info(f"Found {num_mp3s} MP3 files in your \"{filepath}\" directory")
        else:
            logger.info(f"Using \"{filename}\"")

        logger.debug(tuple(mp3paths)) # Show all mp3 filepaths
        return tuple(mp3paths)

def main():
    """Main method"""
    docopt_args = docopt(__doc__)

    # Argument validation schema
    schema = Schema({
        '--help': bool,
        '--tag': bool,
        Optional('--folder'): bool,
        Optional('--debug'): bool,
        Optional('PATH'): Or(str, None)})

    try:
        docopt_args = schema.validate(docopt_args)
    except SchemaError as e:
        exit(e)

    # --debug option to show debug logs
    if(docopt_args.get('--debug') == True):
        logger.setLevel(logging.DEBUG)
        logger.debug("Debugging logs: ENABLED")

    # Print docopt_args
    logger.debug(f"\n== DOCOPT ARGS ==\n{docopt_args}\n=================\n")

    # --tag option
    if (docopt_args.get('--tag') == True):
        # Get all mp3s for given PATH
        filepath = docopt_args.get('PATH')
        mp3_path_tuple = get_mp3_files(filepath)

        for mp3_path in mp3_path_tuple:
            # Create MP3Model for each mp3 file
            mp3model = MP3Model(mp3_path)

            # Do something..
            print(mp3model.audiofile.tag.title)
        

if __name__ == "__main__":
    main()
