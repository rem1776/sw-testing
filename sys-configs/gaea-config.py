site_configuration = {
    'systems': [
        {
            'name': 'gaea',
            'descr': 'gaea',
            'hostnames': ['gaea*'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'batch',
                    'descr': 'c5 partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'environs': ['intel-oneapi-prod', 'intel-oneapi-debug', 'gnu'],
                    'sched_options': {
                        'slurm_multi_cluster_mode': ['c5']
                    },
                }
            ],
        }
    ],
    'environments': [
        {
            'name': 'intel-oneapi-prod',
            'modules': [ 'PrgEnv-intel/8.6.0', 'intel-oneapi', 'cray-hdf5', 'cray-netcdf'],
            'cflags': ['-O2 -debug minimal -sox -traceback -march=core-avx-i'],
            'fflags': ['-O3 -debug minimal -fp-model source -march=core-avx-i'],
        },
        {
            'name': 'intel-oneapi-debug',
            'modules': [ 'PrgEnv-intel/8.6.0', 'intel-oneapi', 'cray-hdf5', 'cray-netcdf'],
            'cflags': ['-O0 -g -march=core-avx-i'],
            'fflags': ['-g -O0 -check -check noarg_temp_created -check nopointer -check nouninit -warn -warn noerrors -fpe0 -ftrapuv -march=core-avx-i'],
        },
        {
            'name': 'gnu',
            'modules': [ 'PrgEnv-gnu/8.6.0', 'gcc-native', 'cray-hdf5', 'cray-netcdf'],
        },
    ],
}
