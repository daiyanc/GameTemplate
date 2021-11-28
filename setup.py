import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GameTemplate",
    version="0.0.1",
    author="Daiyan",
    author_email="daiyanch22@gmail.com",
    description="Short entry level text based adventure game template.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xdaiyan/GameTemplate",
    project_urls={
        "Bug Tracker": "https://github.com/xdaiyan/GameTemplate/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)