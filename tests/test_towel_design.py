import pytest
from towel_design import design_towels

@pytest.fixture
def temp_file(tmp_path):
    temp_file = tmp_path / "test_file.txt"
    temp_file.write_text("r, wr, b, g, bwu, rb, gb, br\n\nbrwrr\nbggr\ngbbr\nrrbgbr\nubwu\nbwurrg\nbrgr\nbbrgwb\n")
    return temp_file

def test_design_towels(temp_file):
    output, possible_design_cnt = design_towels(temp_file)
    expected_output = [
        "rrbgbr can be made with r, rb, gb and r",
        "brwrr can be made with br, wr and r",
        "bggr can be made with b, g, g and r",
        "bbrgwb impossible",
        "gbbr can be made with gb and br",
        "bwurrg can be made with bwu, r, r and g",
        "ubwu impossible",
        "brgr can be made with br, g and r"
    ]
    output.sort()
    expected_output.sort()
    assert output == expected_output
    assert possible_design_cnt == 6

def test_design_towels_file_not_found():
    file_path = "test_files/non_existent_file.txt"
    output, possible_design_cnt = design_towels(file_path)
    assert output == ["Error: File not found."]
    assert possible_design_cnt == 0