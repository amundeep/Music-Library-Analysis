import eyed3

"""MP3 object class to instantiate eyed3 instance"""
class MP3Model:

    def __init__(self, filepath):
        self.filepath = filepath
        self.audiofile = eyed3.load(filepath)

