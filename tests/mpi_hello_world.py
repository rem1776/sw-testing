import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class test_mpi_hello_world(rfm.RegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    build_system = "SingleSource"
    sourcepath = 'mpi_hello_world.F90'
    sourcesdir = "src"
    num_tasks = 10
    num_tasks_per_node = 1

    # last processor should be there if mpi is working, so checks for that
    @sanity_function
    def validate(self):
        return sn.assert_found('hello from processor[ ]*9 of[ ]*10', self.stdout)
