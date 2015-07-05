import os
import tempfile

import click


@click.command()
@click.option('--host', 'hosts', multiple=True)
@click.option('--role', 'roles', multiple=True)
@click.option('--sudo/--no-sudo', '-s')
@click.option('--show-playbook/--no-show-playbook')
def ansible_role_apply(hosts, roles, sudo, show_playbook):
    playbook_content = get_playbook_content(hosts, roles, sudo)
    if show_playbook:
        click.secho(79 * '-', fg='yellow')
        click.secho('#!/usr/bin/env ansible-playbook', fg='yellow')
        click.secho(playbook_content, fg='yellow')
        click.secho(79 * '-', fg='yellow')

    with tempfile.NamedTemporaryFile() as tmpf:
        tmpf.write(playbook_content)
        tmpf.flush()
        os.system('ansible-playbook {playbook}'.format(playbook=tmpf.name))


def get_playbook_hosts(hosts):
    playbook_hosts = '\n'.join([
        '    - {host}'.format(host=host) for host in hosts])
    return playbook_hosts


def get_playbook_roles(roles):
    playbook_roles = '\n'.join([
        '    - {role}'.format(role=role) for role in roles])
    return playbook_roles


def get_playbook_content(hosts, roles, sudo):
    playbook_hosts = get_playbook_hosts(hosts)
    playbook_roles = get_playbook_roles(roles)
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
