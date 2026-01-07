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
        self.build_system.cflags = ["-g", "-O0"]
        self.build_system.builddir = 'build'
        self.build_system.fflags = ["-g", "-O0"]
