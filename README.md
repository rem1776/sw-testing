# sw-testing
Holds configurations and tests for GFDL systems using the [reframe](https://reframe-hpc.readthedocs.io/) testing tool.

To use:
```{bash}
pip install reframe-hpc
# to run a single test file
reframe -C sys-configs.yaml -c tests/<TEST FILE>.py -r
# to run all tests
reframe -C sys-configs.yaml -c tests/ -r
# to run a single test or subset of tests based on a str pattern
reframe -C sys-configs.yaml -c tests/ -n <pattern-to-match> -r
```

A useful option for reframe is `--keep-stage-files`, otherwise successful test directories will be deleted.

Most of these "tests" are compilations, using the repo's build system to ensure the software stack works for development purposes.

Current tests:
- MPI hello world - compiles a simple MPI-enabled Fortran program, runs it, and validates output (`tests/mpi_hello_world.py`)
- FMS autotools build (`tests/fms.py`)
- FRE-NCtools autotools build (`tests/fre_nctools.py`)
- GFDL Vortex Tracker cmake build (`tests/vortex_tracker.py`)


## Contributing/Style Notes

Tests can be added via individual python files in the `tests/` subdirectory, and any systems or environments can be added to `sys-configs.yaml`. Any source code needed by a test should be added to `tests/src`.

As a general rule, specifying modules in the test files should be avoided. New environments can be added to the configuration yaml instead. This keeps the tests portable since modules defined in a
test will always be loaded regardless of the system, and most systems vary in module names/what needs to be loaded.

Version numbers should be omitted from modules unless actually necessary, to avoid repetitive updates and breaking configurations. Reframe can load specific module
versions if needed via command line arguments for more targeted testing.

It's best to set `valid_prog_environments` in the tests explicitly so it only uses environments that are set up for the specific test, as not all tests will load the same modules.
For `valid_systems`, it's best to leave that as `*` since you can still run the test loading the modules via the commandline.
