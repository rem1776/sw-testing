# site config for amd dev box for use with reframe
# only loads compilers/mpi, any other dependencies should be loaded by the tests as needed

site_configuration = {
    'systems': [
        {
            'name': 'lscamd50-d',
            'descr': 'MSD development machine',
            'hostnames': ['lscamd50-d.gfdl.noaa.gov'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'amd',
                    'descr': 'run locally with mpirun',
                    'scheduler': 'local',
                    'launcher': 'mpirun',
                    'environs': ['intel-oneapi', 'gnu-mpich', 'gnu-openmpi']
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'intel-oneapi',
            'modules': [ 'oneapi', 'compiler', 'mpi' ],
            'ftn': 'mpiifx',
            'cc': 'mpiicx',
        },
        {
            'name': 'gnu-mpich',
            'modules': [ 'gcc', 'mpich' ],
            'ftn': 'mpifort',
            'cc': 'mpicc',
        },
        {
            'name': 'gnu-openmpi',
            'modules': [ 'gcc', 'openmpi' ],
            'ftn': 'mpifort',
            'cc': 'mpicc',
        },
    ]
}
