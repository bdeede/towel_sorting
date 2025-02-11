import pytest
from .read_input import read_file, get_available_towel_patterns, get_desired_designs

# filepath: /Users/oidowu/dev/python/towel_sorting/src/test_read_input.py

def test_read_file(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "test_file.txt"
    temp_file.write_text("line1\nline2\nline3")

    # Test read_file function
    lines = read_file(temp_file)
    assert lines == ["line1\n", "line2\n", "line3\n"]

def test_get_available_towel_patterns(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "patterns.txt"
    temp_file.write_text("pattern1,pattern2,pattern3")

    # Test get_available_towel_patterns function
    patterns, num_patterns = get_available_towel_patterns(temp_file)
    assert patterns == ["pattern1", "pattern2", "pattern3"]
    assert num_patterns == 3

def test_get_desired_designs(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "designs.txt"
    temp_file.write_text("header1\nheader2\ndesign1\ndesign2\ndesign3")

    # Test get_desired_designs function
    designs = get_desired_designs(temp_file)
    assert designs == ["design1", "design2", "design3"]