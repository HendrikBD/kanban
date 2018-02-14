from setuptools import setup


setup(
    name="kanban",
    version="0.1",
    py_modules=['kanban'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        kanban=cli:cli
    ''',
)
