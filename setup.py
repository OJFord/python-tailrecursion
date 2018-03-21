"""Setup tailrecursion."""
from setuptools import setup


setup(
    author='Oliver Ford',
    name='tailrecursion',
    version='0.1.0',
    description='Lightweight helper for creating tail-recursive functions.',
    py_modules=(
        'tailrecursion',
    ),
    install_requires=(
    ),
    setup_requires=(
        'pytest-runner',
    ),
    tests_require=(
        'pytest',
    ),
)
