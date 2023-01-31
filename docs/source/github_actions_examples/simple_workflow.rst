Sample Simple Github Actions Workflow
*************************************

Github workflows are incredibly powerful tools.
We will first start with a very basic workflow, then build it up to a comprehensive workflow that can be used to test, build documentation and perform other important tasks.

Let's start by looking at the most basic workflow possible given at `.github/simple.yaml <../_static/github_actions/simple.yml>`_ and breaking it down.

First, new need to define the name of the workflow and when the workflow run.
To define when the workflow will run, you can specify a list of different event types under the `on` parameter in the workflow.
An exhaustive list of events is available in the github actions documentation.
In this example, the workflow will run on a push to the `main` branch.

.. code-block::
   :caption: Name and trigger even

    name: Simple-CI

    on:
        push:
            branches: [ main ]

Next, we can define the actual job itself. This will include the OS that the workflow will use, things such as python versions, permissions and other important settings.
For this example, we will populate the `runs-on` field to configure the workflow to use windows-2019.
Additionally, we can specify a matrix of python versions if we want to test multiple versions.

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
In this example, we will run the `main.py` script using a simple command.

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
            steps:
                - name: Run a simple python command
                  run: |
                    python -m main

In conclusion, we now have a workflow called `Simple-CI` that will run on a push to `main`.
It will use `windows-2019` and `python-3.10`.
The workflow will have permission to read/write and will only run one instance per branch at any given moment.
Finally, the workflow will run `main.py` by using `python -m main`.
