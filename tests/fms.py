import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class build_fms(rfm.CompileOnlyRegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    build_system = "Autotools"
    sourcesdir = "https://github.com/noaa-gfdl/fms.git"
    prebuild_cmds = [ 'autoreconf -if' ]

    @run_before('compile')
    def prepare_build(self):
        self.build_system.cflags = ["`nc-config --cflags`", "`nc-config --libs`"]
        self.build_system.builddir = 'build'
        self.build_system.fflags = ["`nf-config --fflags`", "`nf-config --flibs`", "`nc-config --libs`"]
"""
TODO, run the unit tests after a build
@rfm.simple_test
class unit_tests(rfm.RunOnlyRegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    executable = 'make check'
    foo = fixture(build_fms, scope='environment')
"""
