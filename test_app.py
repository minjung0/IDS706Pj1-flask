from app import changeClass

def test_change():
    assert ["Oops, I think it's not a classic MIDS class."] == changeClass('GS726')