import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class build_(rfm.RegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    build_system = "SingleSource"
    sourcepath = 'src/mpi_hello_world.F90'
