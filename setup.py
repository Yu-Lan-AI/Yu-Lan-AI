from setuptools import setup, find_packages

setup(
    name="yulan",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'cryptography>=3.4.7',
        'pytest>=6.2.5',
        'scipy>=1.7.0',
        'torch>=1.9.0',
        'pandas>=1.3.0',
    ],
    author="ANON AI",
    author_email="anonaisite@gmail.com",
    description="A decentralized AI framework integrating quantum computing with autonomous agents",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anon-ai-labs/ANON-AI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
)
