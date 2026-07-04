from setuptools import setup, find_packages

setup(
    name="vsce-downloads",
    version="0.1.0",
    description="Fetch VSCode Marketplace extension download & rating stats",
    author="knighthood2001",
    author_email="2109695291@qq.com",
    url="https://github.com/Knighthood2001/vsce-downloads",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.0"
    ],
    entry_points={
        "console_scripts": [
            "vsced=vsce_downloads.cli:main"
        ]
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
