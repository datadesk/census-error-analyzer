from setuptools import setup


setup(
    name='census-error-analyzer',
    version='0.0.2',
    description="Analyze the margin of error in U.S. census data",
    author='Los Angeles Times Data Desk',
    author_email='datadesk@latimes.com',
    url='http://www.github.com/datadesk/census-error-analyzer',
    license="MIT",
    packages=("census_error_analyzer",),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
