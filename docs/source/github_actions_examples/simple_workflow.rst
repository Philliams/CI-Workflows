Sample Simple Github Actions Workflow
*************************************

Github workflows are incredibly powerful tools.
We will first start with a very basic workflow, then build it up to a comprehensive workflow that can be used to test, build documentation and perform other important tasks.

Let's start by looking at the most basic workflow possible given at `.github/workflows/simple.yml <../_static/github_actions/simple.yml>`_ and breaking it down.

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

Additionally, we will specify a `concurrency` parameter and an image name.
For this example, we will run on windows 2019.
For the concurrency, what `concurrency.group` does is that it specifies some sort of group ID, such that only one instance per group ID will run at any given moment.
In our case, we will set the concurrency group to the branch name and workflow name.
This means that only one instance of this workflow can run per branch at any given moment.

.. code-block::
   :caption: Name and trigger even

    name: Simple-CI

    on:
        push:
            branches: [ main ]

    jobs:
        build:
            runs-on: windows-2019
            concurrency:
                group: ${{ github.workflow }}-${{ github.ref }}

Finally, with the basic workflow settings defined, we can specify the steps for the workflow.
For each step, we can either run an action or run a raw command.
For simplicity, we will simply provide a step name and run a single command to print the current date.
The format for a command step is to provide a `name:` string and to give a sequence of multiple bash commands to run to the `run:` block.

.. code-block::
   :caption: Name and trigger even

    name: Simple-CI

    on:
        push:
            branches: [ main ]

    jobs:
        build:
            runs-on: windows-2019
            concurrency:
                group: ${{ github.workflow }}-${{ github.ref }}
            steps:
                - name: Run a simple command
                  run: |
                    date

In conclusion, we now have a simple workflow that will run once per branch on a push to main, that will use windows 2019 to print the date.
In the next examples, we will see how to use actions to accomplish more complex tasks.
