import reframe as rfm

@rfm.simple_test
class build_vortex_tracker_cmake(rfm.CompileOnlyRegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['spack-gnu-vortex-tracker', 'spack-intel-vortex-tracker']
    build_system = "CMake"
    sourcesdir = "https://github.com/noaa-gfdl/gfdl-vortextracker"

    @run_before('compile')
    def prepare_build(self):
        self.build_system.builddir = 'build'
        self.build_system.configuredir = 'compile/src_code' 
