import commands

def test_info():
    print '/////////////////////////////////'
    print commands.getoutput('find /home/travis/miniconda/')
    print '/////////////////////////////////'
    print commands.getoutput('which python')
    print commands.getoutput('python --version')
    print '/////////////////////////////////'
    print commands.getoutput('which python | xargs ldd')
    print '/////////////////////////////////'
    print commands.getoutput('nm /home/travis/miniconda/bin/../lib/libpython2.7.so.1.0 | grep _PyInt_AsInt')
    print '/////////////////////////////////'
    print commands.getoutput('md5sum /home/travis/miniconda/bin/../lib/libpython2.7.so.1.0')
    print '/////////////////////////////////'
    print commands.getoutput('conda list')
    print '/////////////////////////////////'
    print commands.getoutput('locate /python | grep /python\$')
    print '/////////////////////////////////'
    assert False, 'forced fail'
