from setuptools import setup

VERSION = '1.0.0'
REPO = 'https://github.com/sw5cc/tencent-finance'

setup(
    name='tencent-finance',
    py_modules=['tencent_finance'],
    version=VERSION,
    description='Python library that provides APIs to query finance from http://stock.qq.com',
    author='sw5cc',
    author_email='sw5cc.125pflops@gmail.com',
    license='MIT',
    url=REPO,
    download_url='{0}/archive/{1}.tar.gz'.format(REPO, VERSION),
    keywords=['tencent', 'finance'],
    install_requires=['requests', 'simplejson']
)
