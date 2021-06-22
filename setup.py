from setuptools import find_packages, setup  # type: ignore

from aovec import __version__

setup(
    name='aovec',
    version=__version__,
    description='Make Word2Vec from aozorabunko/aozorabunko',
    description_content_type='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eggplants/aovec',
    author='eggplants',
    packages=find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    license='MIT',
    install_requires=open('requirements.txt').read().rstrip().split('\n'),
    entry_points={
        'console_scripts': [
            'aovec=aovec.main:main'
        ]
    }
)
