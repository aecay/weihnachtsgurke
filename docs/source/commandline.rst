.. Copyright 2015 University of York
   Author: Aaron Ecay

======================
 Command line options
======================

Weihnachtsgurke is distributed as a command line tool called ``wng``.

Options
=======

The following options are available:

``--output``, ``-o``
    Path to the output file.  If not specified, the search results are
    printed to standard output

``--search-file``, ``-s``
    The file containing a :doc:`description of the search to perform
    <searchguide>`.  Mandatory.

``--parallel``, ``-p``
    How many processes to launch to perform the search.  If you have a
    multi-core machine, passing this option can speed up your searches
    greatly.

Input files
===========

The remaining arguments to the command are taken as PYCCLE-TCP files to
search in.
