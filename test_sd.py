import cal_sd
#from project.test.tud_test_base import mock_input_output_start, mock_input_output_end, set_input, get_output


def test_SD_check():
    tes=cal_sd.preprocessing(r"C:\Users\Puneet Singh\FileName","Age")
    assert tes=="S.D of this is 13.0"


def test_SD_check1():
    tes=cal_sd.preprocessing(r"C:\Users\Puneet Singh\FFileName","Age")
    assert tes=="File doest exist"


def test_SD_check2():
    tes=cal_sd.preprocessing(r"C:\Users\Puneet Singh\FileName","AAge")
    assert tes=="S.D not calculated of this column name or column doesnt exist"
