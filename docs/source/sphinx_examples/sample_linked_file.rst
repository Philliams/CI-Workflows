Sample Linked File
*************************************

In some cases, you may want to link additional HTML files as part of your documentation.
A common example of this is including a pytest coverage report as part of the autodocs.

For this example, we will product an HTML pytest coverage report and copy it to the `_static` directory using the command:

.. code-block::
   :caption: Pytest invocation that produces HTML coverage report to _static dir.

    python -m pytest unittests/ --cov=src --cov-report term --cov-report html:./docs/source/_static

The command works by running pytest as usual `python -m pytest unittests/` then choosing the `src` directory for which to calculate the coverage by the flag `--cov=src`.
Next the coverage report is printed to the terminal via `--cov-report term`. Additionally, the report is dumped as an HTML file to the `_static` directory via `--cov-report html:./<path>`.

Finally, the file can be linked `here <../_static/code_cov/index.html>`_ via the relative path to the file from this current file (`../_static/code_cov/index.html`).
