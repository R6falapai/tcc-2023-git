from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip()
        for req
        in open(filename).readlines()
    ]


setup(
    name="estoque",
    version="0.1.0",  # major, minor, patch.
    description="Aplicativo de estoque online",
    packages=find_packages(),
    include_package_data=True,  # Grava metadados.
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")

    }
)
