Sample Simple Python Github Actions Workflow
**************************************************************

In this example, we will see a workflow that will setup python, install many dependencies and then run a python script using a mixture of actions and commands.
The workflow is given at `.github/workflows/python_simple.yaml <../_static/github_actions/python_simple.yml>`_

For the workflow we will include the OS that the workflow will use, things such as python versions, permissions and other important settings.
For this example, we will populate the `runs-on` field to configure the workflow to use windows-2019.
Additionally, we can specify a matrix of python versions if we want to test multiple versions.
The matrix will make the workflow run for each combinations of values in the matrix.
This can be used to run different version of python (as we will see), but really can be used to provide any number of strings to trigger various configurations in the workflow.

.. code-block::
   :caption: OS and python versions

    name: Simple-CI

    on:
        push:
            branches: [ main ]

    jobs:
        build:
            runs-on: windows-2019
            strategy:
                matrix:
                    python-version: ['3.10']

Another couple of settings is the `permissions` field and `concurrency`.
Setting the permissions will allow the workflow to read/write files within the filesystem of the workflow workspace.
The `concurrency.group` field allows you to specify a group ID such that only one workflow will run per group ID at a time.
In our case, we use the workflow name `github.workflow` and the branch/tag name `github.ref` to ensure that we only have one instance per workflow per branch at any given time.

.. code-block::
   :caption: Concurrency and permissions

    name: Simple-CI

    on:
        push:
            branches: [ main ]

    jobs:
        build:
            runs-on: windows-2019
            strategy:
                matrix:
                    python-version: ['3.10']
            permissions:
                contents: write
            concurrency:
                group: ${{ github.workflow }}-${{ github.ref }}

Finally, we can specify the actual commands that we want to run as part of the workflow under the `steps` field.
Github actions provides a lot of flexibility in terms of commands.
There are two main ways of performing actions within the workflow: 1) running a raw command and 2) using a predefined github action from the actions market place.
In this example, we will use an action to checkout the code, then an action to setup python.
Afterwards, we will use some simple commands to install the dependencies and run the `main.py` script.
To use a predefined action, we use the syntax `- uses: <action name>`.
To checkout the code, we can utilize the checkout V2 action offered by github actions.
To use this action, we write `- uses actions/checkout@v2`.
Next, we will use the setup-python V2 action to setup the python environment.
We will also specify a name for the setup step and provide some parameters.
`- name: <step name>` is used to set the workflow step name.
Note the use of `${{  }}` to dynamically populate the name string.
Next, `uses: actions/setup-python@v2` will specify the python-setup action.
Finally `with: ...` allows us to provide parameters to the action.

.. code-block::
   :caption: Checking out code and setting up python

    name: Simple-CI

    on:
        push:
            branches: [ main ]

    jobs:
        build:
            runs-on: windows-2019
            strategy:
                matrix:
                    python-version: ['3.10']
            permissions:
                contents: write
            concurrency:
                group: ${{ github.workflow }}-${{ github.ref }}
            steps:
                - uses: actions/checkout@v2
                - name: Set up Python ${{ matrix.python-version }}
                  uses: actions/setup-python@v2
                  with:
                    python-version: ${{ matrix.python-version }}

Once the code is checked out and python has been installed, we will use `run:` to provide raw commands for the workflow to run.
In this example, we will first install all the requirements via pip and the checked out `requirements.txt` file.
Afterwards, we will run `main.py` by invoking `python -m src.main`.

.. code-block::
   :caption: Installing dependencies and running main.py

    name: Simple-CI

    on:
        push:
            branches: [ main ]

    jobs:
        build:
            runs-on: windows-2019
            strategy:
                matrix:
                    python-version: ['3.10']
            permissions:
                contents: write
            concurrency:
                group: ${{ github.workflow }}-${{ github.ref }}
            steps:
                - name: Checkout code
                  uses: actions/checkout@v2
                - name: Set up Python ${{ matrix.python-version }}
                  uses: actions/setup-python@v2
                  with:
                    python-version: ${{ matrix.python-version }}
                - name: Install dependencies
                  run: |
                    python -m pip install --upgrade pip
                    python -m pip install flake8 flake8-match pre-commit pytest
                    pip install -r ./dependencies/requirements.txt
                - name: Run a simple python command
                  run: |
                    python -m src.main

In conclusion, we now have a workflow called `Simple-CI` that will run on a push to `main`.
It will use `windows-2019` and `python-3.10`.
The workflow will have permission to read/write and will only run one instance per branch at any given moment.
Finally, it will install python and checkout the code via actions, and install the dependencies and run `main.py` via commands.