import pytest
from video_library import LibraryItem

def test_library_item_initialization():
    item = LibraryItem("Test Movie", "Test Director", 3)
    assert item.name == "Test Movie"
    assert item.director == "Test Director"
    assert item.rating == 3
    assert item.play_count == 0

def test_library_item_info():
    item = LibraryItem("Test Movie", "Test Director", 4)
    assert item.info() == "Test Movie - Test Director ****"

def test_library_item_stars():
    item = LibraryItem("Test Movie", "Test Director", 2)
    assert item.stars() == "**"

def test_increment_play_count():
    item = LibraryItem("Test Movie", "Test Director", 2)
    assert item.play_count == 0
    item.increment_play_count()  # Use the method to increment play count
    assert item.play_count == 1