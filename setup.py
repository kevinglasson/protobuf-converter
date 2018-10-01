from setuptools import setup

setup(
    name='protobuf-converter',
    description='A teeny Python library for creating Python dicts from '
        'protocol buffers and the reverse. Useful as an intermediate step '
        'before serialisation (e.g. to JSON). Forked from Ben Hodgson '
        'https://github.com/benhodgson',
    version='0.2.0',
    author='Kevin Glasson',
    author_email='kevinglasson+protobuf@gmail.com',
    url='https://github.com/kevinglasson/protobuf-to-dict',
    license='Public Domain',
    keywords=['protobuf', 'json', 'dict'],
    install_requires=['protobuf>=2.3.0'],
    package_dir={'':'src'},
    py_modules=['protobuf_to_dict'],
    setup_requires=['protobuf>=2.3.0', 'nose>=1.0', 'coverage', 'nosexcover'],
    test_suite = 'nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
