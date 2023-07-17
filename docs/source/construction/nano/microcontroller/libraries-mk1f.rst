..  include:: ../mk1ef.txt

Install the CowPi and the CowPi_stdio Libraries
===============================================
*Cow Pi mk1f: Arduino Nano form factor*

You will need to install the CowPi and the CowPi_stdio libraries.
The instructions differ, depending on which IDE you are using:

-   :ref:`mk1fArduinoLibrary`
-   :ref:`mk1fPlatformIOLibrary`


..  _mk1fArduinoLibrary:

..  include:: libraries-arduino-steps.rst

You will see a pop-up window telling you that you also need to install the CowPi_stdio library (:numref:`mk1fInstallingArduinoLibraries`).


..  _mk1fInstallingArduinoLibraries:
..  figure:: libraries-arduino.png
    :alt: Installing the CowPi and CowPi_stdio libraries.
    :width: 90%
    :align: center

    Installing both libraries can be achieved by installing the CowPi library and its dependency.


:\:[   ]: Click the "Install All" button.

    -   If you err and select "Install Without Dependencies" then you can still install the CowPi_stdio library separately.


After the libraries are installed, proceed to :doc:`../direct-io/switches-mk1f`.

----

.. _mk1fPlatformIOLibrary:

Install the Libraries for PlatformIO
""""""""""""""""""""""""""""""""""""

.. ..  include:: ide-platformio.rst

..  DANGER::
    TODO

If you are satisfied with using the Arduino IDE, then proceed to :doc:`../direct-io/switches-mk1f`.
