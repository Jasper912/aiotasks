import click

from click.testing import CliRunner

from aiotasks.actions.default.cli import worker

import aiotasks.actions.default.console


def _launch_aiotasks_in_console(blah, **kwargs):
    click.echo("ok")


def test_cli_worker_runs_show_help():
    runner = CliRunner()
    result = runner.invoke(worker)

    assert 'Usage: worker [OPTIONS]' in result.output


def test_cli_worker_runs_ok():
    # Patch the launch of: launch_aiotasks_info_in_console
    aiotasks.actions.default.cli.launch_aiotasks_in_console = _launch_aiotasks_in_console

    runner = CliRunner()
    result = runner.invoke(worker, ["-A", "package"])

    assert 'ok' in result.output
