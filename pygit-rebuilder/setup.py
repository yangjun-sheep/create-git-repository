from distutils.core import  setup

setup(
    name='pygit-rebuilder',
    version='1.0',
    author='yangj',
    py_modules=['git_rebuilder'],
    install_requires=[
        'networkx==2.5',
        'pygit2==1.5.0',
        'pydot==1.4.2'
    ]
)
