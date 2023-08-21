from modules.output import print_hello

def test_print_hello(capfd):
    print_hello()
    out, err = capfd.readouterr()
    assert err == ''
    assert out == "Hello World!\n"


    

