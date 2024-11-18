from setuptools import setup

setup(
    name="shell-util",
    version="1.0",
    description="A tool that lets you alias your day to day shell commands.",
    author="Nagaraj Archak",
    author_email="archak.nagaraj@gmail.com",
    url="https://github.com/nagarajarchak/shell-sobriquet",
    packages=["alias"],
    license="MIT License",
    entry_points={
        "console_scripts": [
            "alias-it = alias.alias:main",
        ]
    }
)