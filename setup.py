import setuptools

setuptools.setup(
    name='ip3country',
    version='0.3.0',
    url='https://github.com/statsig-io/ip3country-py',
    author='Statsig',
    author_email='tore@statsig.com',
    description='A zero-dependency, local, fast, tiny ip-address to country lookup',
    long_description="See https://github.com/statsig-io/ip3country-py",
    long_description_content_type="text/markdown",
    keywords=['ip', 'country', 'lookup', 'statsig'],
    packages=setuptools.find_packages(),
    install_requires=[],
    license='ISC',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    python_requires='>=2.0',
)
