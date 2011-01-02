from setuptools import setup, find_packages
import sys, os

extra = {}
if sys.version_info >= (3, 0):
    extra.update(
        use_2to3=True,
        use_2to3_fixers=['custom_fixers']
    )

version = '1.1.0'

setup(
    name="holland",
    version=version,
    description="Holland Core Plugins",
    long_description="""\
    These are the plugins required for basic Holland functionality.
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="",
    author="Rackspace",
    author_email="holland-discuss@lists.launchpad.net",
    url='http://www.hollandbackup.org',
    license="3-Clause BSD",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    install_requires=[
    # 'configobj' # currently this is bundled internally
    ],
    entry_points="""
    # Scripts generated by setuptools
    [console_scripts]
    holland = holland.cli.main:holland

    # Holland subcommands
    [holland.commands]
    help          = holland.cli.commands:Help
    listplugins   = holland.cli.commands:ListPlugins
    listcommands  = holland.cli.commands:ListCommands
    listbackups   = holland.cli.commands:ListBackups
    backup        = holland.cli.commands:Backup
    mk-config     = holland.cli.commands:MkConfig
    purge         = holland.cli.commands:Purge
    """,
    namespace_packages=['holland', 'holland.backup', 'holland.lib'],
    **extra
)
