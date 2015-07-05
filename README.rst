ansible-role-apply
==================

Apply a single Ansible role to host(s) easily

Example usage
-------------

.. code-block:: bash

    $ ansible-role-apply --help
    Usage: ansible-role-apply [OPTIONS] ROLE HOSTS

    Options:
      -s, --sudo / --no-sudo
      --show-playbook / --no-show-playbook
      --help                          Show this message and exit.

    $ ansible-role-apply docker vagrant --sudo
    ...
    PLAY [vagrant] ****************************************************************

    GATHERING FACTS ***************************************************************
    ok: [vagrant]
    ...
    PLAY RECAP ********************************************************************
    vagrant                    : ok=16   changed=1    unreachable=0    failed=0

    $ ansible-role-apply docker vagrant --sudo --show-playbook
    -------------------------------------------------------------------------------
    #!/usr/bin/env ansible-playbook
    ---
    - hosts:
        - vagrant
      roles:
        - docker
      sudo: True
    -------------------------------------------------------------------------------

    |---> plugin activated: /Users/marca/dev/surveymonkey/smstack/smstack/ansible/plugins/no_hosts_matched_fail.pyc
    |---> plugin activated: /Users/marca/dev/surveymonkey/smstack/smstack/ansible/plugins/sm_app_role.pyc
    |---> plugin activated: /Users/marca/dev/surveymonkey/smstack/smstack/ansible/plugins/teamcity_messages.pyc

    PLAY [vagrant] ****************************************************************
    ...
    PLAY RECAP ********************************************************************
    vagrant                    : ok=16   changed=1    unreachable=0    failed=0
