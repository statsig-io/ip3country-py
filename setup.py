import setuptools

setuptools.setup(
    name="ip3country",
    version="0.1.0",
    url="https://github.com/statsig-io/ip3country-py",
    author="Statsig",
    author_email="tore@statsig.com",
    description="A zero-dependency, local, fast, tiny ip-address to country lookup",
    keywords=["ip", "country", "lookup", "statsig"],
    packages=setuptools.find_packages(),
    install_requires=[],
    license="ISC",
    python_requires=">=2.0",
)
