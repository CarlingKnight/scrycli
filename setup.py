from setuptools import setup
#     setup  # workaround for pyflakes issue #13
# except ImportError:
#     from distutils.core import setup

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
# try:
#     import multiprocessing
#     multiprocessing
# except ImportError:
#     pass

setup(
    name='scryapi',
    version='0.0.0',
    author='Carling Knight',
    author_email='carlingjk@gmail.com',
    packages=[],
    scripts=['bin/scry'],
    url='',
    license='',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
    description='Nah',
    install_requires=open('requirements.txt').readlines(),
)