Sample Automatic Documentation
*************************************

This page is an example of how to recursively auto-generate documentation for all modules in a directory.

A template can be included in the `_templates` directory and used as `:template: template-file.rst` to give a more detailed view of the modules/classes/functions/etc.

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   src
   

