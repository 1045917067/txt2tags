import os.path

import py.test

import lib


DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(DIR)
TXT2TAGS = os.path.join(REPO, 'txt2tags')


def pytest_addoption(parser):
    parser.addoption(
        '--txt2tagslite', action='store_true', default=False,
        help='Test txt2tagslite')
    parser.addoption(
        '--slow', action='store_true', default=False,
        help='Also run slow tests')


def pytest_configure(config):
    if config.getvalue('txt2tagslite'):
        lib.TXT2TAGS = os.path.join(lib.REPO, 'txt2tagslite')


def pytest_runtest_setup(item):
    """Skip tests if they are marked as slow and --slow is not given"""
    if 'slow' in item.keywords and not item.config.getvalue('slow'):
        py.test.skip('slow tests not requested')
