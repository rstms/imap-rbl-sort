#!/usr/bin/env python

"""Tests for `imap_rbl_sort` CLI"""

import pytest

from traceback import print_exception

import imap_rbl_sort
from imap_rbl_sort import __version__, cli
from click.testing import CliRunner


def test_version():
    """Test reading version and module name"""
    assert imap_rbl_sort.__name__ == "imap_rbl_sort"
    assert __version__
    assert isinstance(__version__, str)

@pytest.fixture
def run():
    runner = CliRunner()

    #env = os.environ.copy()
    #env['EXTRA_ENV_VAR'] = 'VALUE'

    def _run(cmd, **kwargs):
        expect_exit_code = kwargs.pop("expect_exit_code", 0)
        expect_exception = kwargs.pop("expect_exception", None)
        #kwargs["env"] = env
        result = runner.invoke(cli, cmd, **kwargs)
        if result.exception:
            if not isinstance(result.exception, expect_exception):
                print_exception(result.exception)
                breakpoint()
                pass
        else:
            assert result.exit_code == expect_exit_code, result.output
        return result

    return _run

def test_cli(run):
    """Test the CLI."""
    result = run([], expect_exception=RuntimeError)
    assert 'imap_rbl_sort/cli.py' in str(result.exception)

def test_help(run):
    result = run(['--help'])
    assert 'Show this message and exit.' in result.output
