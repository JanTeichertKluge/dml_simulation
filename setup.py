from setuptools import find_packages, setup
setup(
    name='dml_simulation_study',
    packages=find_packages(where='C:/Users/Nutzer/source/repos/doubleml-neuralnets/simulation/dml_simulation_study'),
    version='0.1.0',
    description='package to run DoubleML simulation studies',
    author='Sundermann, Moritz; Teichert-Kluge, Jan',
    install_requires=['attrs==22.2.0',
                      'CacheControl==0.12.11',
                      'certifi==2022.12.7',
                      'charset-normalizer==2.1.1',
                      'cleo==2.0.1',
                      'colorama==0.4.6',
                      'contourpy==1.0.6',
                      'crashtest==0.4.1',
                      'cycler==0.11.0',
                      'distlib==0.3.6',
                      'docopt==0.6.2',
                      'DoubleML==0.5.2',
                      'dulwich==0.20.50',
                      'et-xmlfile==1.1.0',
                      'exceptiongroup==1.1.0',
                      'filelock==3.9.0',
                      'fonttools==4.38.0',
                      'html5lib==1.1',
                      'idna==3.4',
                      'importlib-metadata==4.13.0',
                      'iniconfig==2.0.0',
                      'jaraco.classes==3.2.3',
                      'joblib==1.2.0',
                      'jsonschema==4.17.3',
                      'keyring==23.13.1',
                      'kiwisolver==1.4.4',
                      'lockfile==0.12.2',
                      'matplotlib==3.6.2',
                      'more-itertools==9.0.0',
                      'msgpack==1.0.4',
                      'numpy==1.22.4',
                      'openpyxl==3.0.10',
                      'packaging==22.0',
                      'pandas==1.5.2',
                      'patsy==0.5.3',
                      'pexpect==4.8.0',
                      'Pillow==9.4.0',
                      'platformdirs==2.6.2',
                      'pluggy==1.0.0',
                      'ptyprocess==0.7.0',
                      'pyparsing==3.0.9',
                      'pyrsistent==0.19.3',
                      'pytest==7.2.0',
                      'python-dateutil==2.8.2',
                      'pytz==2022.7',
                      'pywin32-ctypes==0.2.0',
                      'rapidfuzz==2.13.7',
                      'scikit-learn==1.2.0',
                      'scipy==1.7.3',
                      'seaborn',
                      'shellingham==1.5.0.post1',
                      'six==1.16.0',
                      'skorch==0.12.1',
                      'statsmodels',
                      'tabulate==0.9.0',
                      'threadpoolctl==3.1.0',
                      'tomli==2.0.1',
                      'tomlkit==0.11.6',
                      'torch==1.13.1',
                      'tqdm==4.64.1',
                      'trove-classifiers==2022.12.22',
                      'typing_extensions==4.4.0',
                      'urllib3==1.26.13',
                      'webencodings==0.5.1',
                      'yarg==0.1.9',
                      'zipp==3.11.0'],
     license='MIT'
)