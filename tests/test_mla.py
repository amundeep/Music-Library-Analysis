import pytest

from music_library_analysis import __version__
from music_library_analysis.mla import get_mp3_filepaths_in_dir, get_mp3_files

def test_version():
    assert __version__ == '0.1.0'

def test_get_mp3_files_in_dir(assets_folder_mp3s):
    # Assert the lists are equal regardless of order
    assert set(get_mp3_filepaths_in_dir("assets")) == set(assets_folder_mp3s)
    assert len(get_mp3_filepaths_in_dir("assets")) == len(set(assets_folder_mp3s))

def test_get_mp3_files(assets_folder_mp3s):
    assert set(get_mp3_files("assets")) == set(assets_folder_mp3s)
    assert len(get_mp3_files("assets")) == len(set(assets_folder_mp3s))

@pytest.fixture
def assets_folder_mp3s():
    return ("assets/MIDNIGHT SATELLITE.mp3","assets/more/sound1.mp3","assets/more/sound2.mp3","assets/more/sound3.mp3")
