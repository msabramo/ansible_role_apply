ansible-role-apply
==================

Apply a single Ansible role to host(s) easily

Example usage
-------------

.. code-block:: bash

    $ ansible-role-apply --host=vagrant --role=docker --sudo --show-playbook
    -------------------------------------------------------------------------------
    #!/usr/bin/env ansible-playbook
    ---
    - hosts:
        - vagrant
      roles:
        - docker
      sudo: True
    -------------------------------------------------------------------------------

    PLAY [vagrant] ****************************************************************

    GATHERING FACTS ***************************************************************
    ok: [vagrant]

    ...

    PLAY RECAP ********************************************************************
    vagrant                    : ok=16   changed=1    unreachable=0    failed=0
