site_configuration = {
    'systems': [
        {
            'name': 'gaea',
            'descr': 'gaea',
            'hostnames': ['gaea*'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'c5',
                    'descr': 'c5 partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'environs': ['intel', 'gnu']
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'intel',
            'modules': [
                {
                    'name': 'PrgEnv-intel/8.6.0',
                    'name': 'cray-hdf5/1.12.2.11',
                    'name': 'cray-netcdf',
                }    
            ]
        },
        {
            'name': 'gnu',
            'modules': [
                {
                    'name': 'PrgEnv-gnu/8.6.0',
                    'name': 'cray-hdf5/1.12.2.11',
                    'name': 'cray-netcdf/4.9.0.17',
                }    
            ]
        },
    ]
}
