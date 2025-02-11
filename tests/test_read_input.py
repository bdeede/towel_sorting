from src.read_input import *
import pytest

@pytest.fixture
def temp_file(tmp_path):
    temp_file = tmp_path / "test_file.txt"
    temp_file.write_text("pattern1,pattern2,pattern3\n\ndesign1\ndesign2\ndesign3")
    return temp_file


def test_read_file(temp_file):
    # Test read_file function
    lines = read_file(temp_file)
    assert lines[0] == "pattern1,pattern2,pattern3\n"
    assert len(lines) == 5

def test_get_available_towel_patterns(temp_file):
    # Test get_available_towel_patterns function
    patterns = get_available_towel_patterns(temp_file)
    assert patterns == ["pattern1", "pattern2", "pattern3"]

def test_get_desired_designs(temp_file):
    # Test get_desired_designs function
    designs = get_desired_designs(temp_file)
    assert designs == ["design1", "design2", "design3"]