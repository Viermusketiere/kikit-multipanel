#!/usr/bin/env python

"""Tests for `kikit_multipanel` package."""


import unittest
from click.testing import CliRunner

from kikit_multipanel import kikit_multipanel
from kikit_multipanel import cli


class TestKikit_multipanel(unittest.TestCase):
    """Tests for `kikit_multipanel` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        # assert result.exit_code == 0
        # assert 'kikit_multipanel.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output
        help_result = runner.invoke(cli.main, ['--version'])
        assert help_result.exit_code == 0
        # assert 'Show this message and exit.' in help_result.output
