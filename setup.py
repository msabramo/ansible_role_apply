import os
from setuptools import setup

this_dir = os.path.dirname(__file__)
long_description = "\n" + open(os.path.join(this_dir, 'README.rst')).read()

setup(
    name='ansible_role_apply',
    version='0.0.0',
    description='Apply a single Ansible role to host(s) easily',
    long_description=long_description,
    keywords='ansible',
    author='Marc Abramowitz',
    author_email='mmsabramo@gmail.com',
    url='https://github.com/msabramo/ansible-role-apply',
    py_modules=['ansible-role-apply'],
    zip_safe=False,
    install_requires=[
        'ansible',
        'click',
    ],
    entry_points="""\
      [console_scripts]
      ansible-role-apply = ansible_role_apply:ansible_role_apply
    """,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
