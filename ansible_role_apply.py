import os
import subprocess
import tempfile

import click


@click.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.option('--sudo/--no-sudo', '-s')
@click.option('--show-playbook/--no-show-playbook')
@click.argument('role')
@click.argument('hosts')
@click.argument('ansible_playbook_args', nargs=-1, type=click.UNPROCESSED)
def ansible_role_apply(sudo, show_playbook, role, hosts,
                       ansible_playbook_args):
    playbook_content = get_playbook_content(role, hosts, sudo)
    if show_playbook:
        click.secho(79 * '-', fg='yellow')
        click.secho('#!/usr/bin/env ansible-playbook', fg='yellow')
        click.secho(playbook_content, fg='yellow')
        click.secho(79 * '-' + '\n', fg='yellow')

    with tempfile.NamedTemporaryFile() as tmpf:
        tmpf.write(playbook_content)
        tmpf.flush()
        cmd = ['ansible-playbook', tmpf.name] + list(ansible_playbook_args)
        click.secho('Executing command: %s\n' % cmd, fg='yellow')
        subprocess.call(cmd)


def get_playbook_hosts(hosts):
    playbook_hosts = '\n'.join([
        '    - {host}'.format(host=host) for host in hosts])
    return playbook_hosts


def get_playbook_roles(roles):
    playbook_roles = '\n'.join([
        '    - {role}'.format(role=role) for role in roles])
    return playbook_roles


def get_playbook_content(role, hosts, sudo):
    playbook_roles = get_playbook_roles([role])
    playbook_hosts = get_playbook_hosts([hosts])
    playbook_content = """\
---
- hosts:
{playbook_hosts}
  roles:
{playbook_roles}
  sudo: {sudo}
        """.format(
            playbook_hosts=playbook_hosts,
            playbook_roles=playbook_roles,
            sudo=sudo).rstrip()
    return playbook_content


if __name__ == '__main__':
    ansible_role_apply()
