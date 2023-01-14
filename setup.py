
from setuptools import setup, find_packages


version = '0.5.0'
url = 'https://github.com/pmaigutyak/mp-availability'

setup(
    name='django-mp-availability',
    version=version,
    description='Django availability app',
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=[]
)
