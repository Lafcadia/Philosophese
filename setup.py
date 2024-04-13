import setuptools


setuptools.setup(
    name='philosophese',
    version='0.0.1',
    author='Lafcadia',
    author_email='chuishenx@oblivionocean.top',
    description='Philosophese',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lafcadia/Philosophese',
    packages=[
        'philosophese',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'jieba>=0.42.1',
    ],
)
