from setuptools import setup, find_packages

setup(
    name="boft-organizer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A modern file organization tool",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/boft-organizer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'watchdog',
        'Pillow',
        'pystray',
        'python-dateutil',
        'jsonschema',
        'requests',
        'psutil'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'boft-organizer=BOFT:main',
        ],
    },
)
