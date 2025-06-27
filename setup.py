from setuptools import setup

setup(
    name='mkdocs-mask-plugin',
    version='0.1',
    author="eWloYW8",
    author_email="3171132517@qq.com",
    py_modules=['mask_plugin'],
    description="A MkDocs plugin that adds a custom syntax to hide text behind a black box until hovered.",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=['mkdocs>=1.1', 'markdown'],
    entry_points={
        'mkdocs.plugins': [
            'mask = mask_plugin:MaskPlugin',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires='>=3.6',
)

