import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class build_fre_nctools(rfm.CompileOnlyRegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    build_system = "Autotools"
    sourcesdir = "https://github.com/noaa-gfdl/fre-nctools.git"
    prebuild_cmds = [ 'autoreconf -if' ]
    modules = [ "nco" ]

    @run_before('compile')
    def prepare_build(self):
        self.build_system.cflags = ["`nc-config --cflags`", "`nc-config --libs`"]
        self.build_system.builddir = 'build'
        self.build_system.fflags = ["`nf-config --fflags`", "`nf-config --flibs`", "`nc-config --libs`"]


