#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='webp',
    version='0.1.0a16',
    url='https://github.com/anibali/pywebp',
    packages=find_packages(include=['webp', 'webp.*', 'webp_build']),
    package_data={'webp_build': ['*.h', '*.c']},
    author='Aiden Nibali',
    description='Python bindings for WebP',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    test_suite='tests',
    setup_requires=['cffi>=1.0.3', 'conan>=1.8.0', 'importlib_resources>=1.0.0'],
    cffi_modules=['webp_build/builder.py:ffibuilder'],
    install_requires=['cffi>=1.0.0', 'Pillow>=4.0.0', 'numpy>=1.0.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'License :: OSI Approved :: MIT License',
    ]
)
