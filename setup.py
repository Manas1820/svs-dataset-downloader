import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='svs_dataset_downloader',
    packages=['svs_dataset_downloader'],
    version='0.0.1',
    license='MIT',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Manas Gupta',
    author_email='manasgupta1820@gmail.com',
    url='https://github.com/Manas1820/svs-dataset-downloader',
    project_urls={
        "Bug Tracker": "https://github.com/Manas1820/svs-dataset-downloader/issues"
    },
    install_requires=['selenium'],
    keywords=["pypi", "selenium", "medical"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    download_url="https://github.com/Manas1820/svs-dataset-downloader/archive/refs/tags/v0.0.1.tar.gz",
)