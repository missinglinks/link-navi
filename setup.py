from setuptools import setup, find_packages
from os.path import dirname, abspath, join

base_path = dirname(abspath(__file__))

with open(join(base_path, "README.md")) as readme_file:
    readme = readme_file.read()

with open(join(base_path, "requirements.txt")) as req_file:
    requirements = req_file.readlines()

setup(
    name="linknavi",
    description='Tool for hyperlink analysis',
    long_description=readme,
    license="MIT",
    author='pmuehleder',
    author_email='pmuehleder@ub.uni-leipzig.de',
    url='https://github.com/missinglinks/linknavi',
    packages=find_packages(exclude=['dev', 'docs']),
    package_dir={
            'linknavi': 'linknavi'
        },
    version="0.1.0",
    py_modules=["linknavi"],
    install_requires=requirements,
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    test_suite="pytest",
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: System :: Logging',
    ],
    keywords=[
        'link', 'hyperlink', 'data analysis', 'data extraction'
    ],
)