import setuptools

with open('README.md', 'r') as file:
    long_desciption = file.read()

setuptools.setup(
    name = 'ai42',
    version = '1.0.0',
    author = 'lguiller',
    author_email = 'lguiller@student.42.fr',
    description = 'A small package description',
    long_desciption = long_desciption,
    long_desciption_content_type = 'text/markdown',
    url = 'https://github.com/Lynux2142',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating Systeme :: OS Independent',
    ],
    python_requires = '>=3.7',
)
