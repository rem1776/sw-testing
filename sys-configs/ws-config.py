# site config for GFDL workstations for use with reframe
# only loads compilers/mpi, any other dependencies should be loaded by the tests

site_configuration = {
    'systems': [
        {
            'name': 'ws',
            'descr': 'GFDL workstations',
            'hostnames': ['ldt-4742404.gfdl.noaa.gov'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'ws',
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
            'modules': [
                {
                    'name': 'intel-oneapi-compilers',
                    'name': 'intel-oneapi-mpi',
                }    
            ],
            'ftn': 'mpiifx',
            'cc': 'mpiicx',
        },
        {
            'name': 'gnu-mpich',
            'modules': [
                {
                    'name': 'gcc',
                    'name': 'mpich',
                }    
            ],
            'ftn': 'mpifort',
            'cc': 'mpicc',
        },
        {
            'name': 'gnu-openmpi',
            'modules': [
                {
                    'name': 'gcc',
                    'name': 'openmpi',
                }    
            ],
            'ftn': 'mpifort',
            'cc': 'mpicc',
        },
    ]
}
