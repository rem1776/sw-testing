import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class build_null_model(rfm.CompileOnlyRegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    build_system = "CustomBuild"
    sourcesdir = "https://github.com/noaa-gfdl/fmscoupler.git"

    @run_before('compile')
    def prepare_build(self):
        self.build_system.commands = ["t/null_model_build.sh"]
