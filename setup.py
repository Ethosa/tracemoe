import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tracemoe",
    version="1.0",
    author="Ethosa",
    author_email="social.ethosa@gmail.com",
    description="Trace moe api wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ethosa/tracemoe",
    packages=setuptools.find_packages(),
    license="LGPLv3",
    keywords="anime tracemoe trace moe api wrapper",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Github": "https://github.com/Ethosa/tracemoe",
    },
    python_requires=">=3",
    install_requires=[
        "requests",
        "aiohttp",
    ]
)
