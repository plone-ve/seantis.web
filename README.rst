===========
Seantis Web
===========

Foundation-based Plone theme for the seantis website.

Introduction
============

``seantis.web`` is an installable Plone Mobile Theme developed by 
`Seantis GmbH`_ using the **theming** and **packaging** features available 
in `plone.app.theming`_,  and `plone.app.themingplugins`_ packages.


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/seantis/seantis.web/raw/master/seantis/web/resources/preview.png
  :alt: seantis.web Theme
  :align: center


Examples
========

This add-on can be seen in action at the following sites:

- https://www.seantis.ch/


Features
========

- It's an Mobile Theme with responsive design support.
- It's an installable Plone Theme package.
- After installation from Add-ons control panel, this theme is enabled automatically.
- It's uses ``plone.app.themingplugins`` package to override templates.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming``, ``plone.app.themingplugins``, ``Products.ContentWellPortlets``, 
  ``collective.portlet.embed`` and ``collective.blogging`` packages (*will be installed as 
  dependencies of this package*)


Installation
============


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``seantis.web`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        seantis.web


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'seantis.web',
    ],


Enabling the theme
------------------

Select and enable the theme from the Diazo control panel. That's it!


When you want to edit the theme, you should do this on the file system.
If you duplicate it TTW, the overridden templates will not be used.

plone.app.themingplugins integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The theme uses ``plone.app.themingplugins`` package to override templates just 
for this theme. These templates will not work if you duplicate the theme TTW 
(``plone.app.themingplugins`` package do not work for that).


Contribute
==========

- Issue Tracker: https://github.com/seantis/seantis.web/issues
- Source Code: https://github.com/seantis/seantis.web


License
=======

- The project is licensed under the GPLv2.
- Nice Icons from IcoMoon is included (GPL or CC BY 3.0) license.


Credits
-------

Really thanks to :

- Seantis GmbH.  (info at seantis dot ch).


Amazing contributions
---------------------

- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

You can find an updated list of package contributors on https://github.com/seantis/seantis.web/contributors

.. _`Seantis GmbH`: https://www.seantis.ch
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`plone.app.themingplugins`: https://pypi.org/project/plone.app.themingplugins/
