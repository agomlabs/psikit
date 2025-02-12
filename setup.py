from setuptools import setup, find_packages

setup(
    name='psikit',
    version='0.1.0',
    description='A lightweight quantum computing framework for simulating quantum optics experiments, focusing on photonic qubits.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='AgomLabs',
    author_email='bistcuite@riseup.net',
    url='https://github.com/your_username/psikit',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
