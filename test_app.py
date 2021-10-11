from app import changeClass

def test_change():
#    assert ["Oops, I think it's not a classic MIDS class."] == changeClass('GS726')
    assert changeClass('GS726') == "Oops, I think it's not a classic MIDS class."