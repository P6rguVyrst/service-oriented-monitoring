from setuptools import setup, find_packages

setup(
    name="app_mon",
    version="0.1.0",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["uwsgi", "flask", "prometheus_client"],
)
