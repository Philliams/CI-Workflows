Sample Documentation Test
*************************************

This page is an example of how to include tested code snippets as part of documentation.
This is accomplished using the `doctest` module and by including the `-b doctest` flag as part of the Sphinx invocation.
These code snippets are different than a regular code block in that they get unit tested as part of the build process.
This is convenient for ensuring that documentation is up to date!

.. doctest::

        >>> from src import main
        >>> a = 1
        >>> b = 2
        >>> main.dummy_function(a, b)
        1

Try changing the code in the `.. doctest::` block to see what happens when it fails.