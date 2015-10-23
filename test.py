import commands

def test_info():
    print commands.getoutput('find /home/travis/miniconda/')
    print commands.getoutput('find /home/travis/miniconda/')
    assert False, 'forced fail'
