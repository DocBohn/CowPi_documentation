..  include:: ../mk1ef.txt

Install the IDE
===============
*Cow Pi mk1e: Arduino Nano form factor*

|

..  ATTENTION::
    **If you are a Windows user,** please review the notes about CH340 USB Driver issues for :ref:`Windows10CH340` and :ref:`Windows11CH340`.

|

Broadly speaking, you have four options:

-   Using the :ref:`mk1fArduinoIDE` on your personal laptop
-   Using :ref:`mk1eVSCodeWithPlatformIO` on your personal laptop
-   Using VS Code with the PlatformIO Plugin on a :ref:`mk1eTerminalServer`
-   Using PlatformIO on a lab computer (this option is not yet available)

|

----

|

..  _mk1eArduinoIDE:

..  include:: ide-arduino-before-board-selection.rst

-   You will need to select the board and port;
    on Windows, you may need to select "Show Hidden Ports" (see :numref:`mk1eSelectingBoard`\ (a)).
    With Arduino Nanos, you will also need to select the processor (see :numref:`mk1eSelectingBoard`\ (b) and the discussion below).

.. _mk1eSelectingBoard:
.. figure:: ../../../blank.png

    Selecting board and processor in the Arduino IDE.

    +-----------------------------------------------+---------------------------------------------------------+
    | a                                             | b                                                       |
    +===============================================+=========================================================+
    | .. image:: selecting-nano.jpg                 | .. image:: selecting-nano-processor.jpg                 |
    |    :width: 8cm                                |    :width: 8cm                                          |
    |    :align: center                             |    :align: center                                       |
    +-----------------------------------------------+---------------------------------------------------------+
    | Selecting the board with Arduino IDE 2.0.     | Selecting the processor after selecting the board.      |
    +-----------------------------------------------+---------------------------------------------------------+

..  include:: ide-arduino-after-board-selection.rst

If you are satisfied with using the Arduino IDE, then proceed to :doc:`power-mk1e`.

|

----

..  _mk1eTerminalServer:

Microsoft Terminal Server
-------------------------

:\:[   ]: Download and install the `VMWare Horizon Client <https://customerconnect.vmware.com/en/downloads/info/slug/desktop_end_user_computing/vmware_horizon_clients/horizon_8>`_\ .

:\:[   ]: Using the VMWare Horizon Client, connect to *cse-vmcs-01.unl.edu* and login with your ``@unl.edu`` credentials.

:\:[   ]: After you log in you should have an item called “Terminal Server” that you can select.

:\:[   ]: After you have reached the Terminal Server's Windows desktop, and **before you plug in your Arduino**,
    enable USB forwarding by going to the VMWare menu and selecting *Connections* ⟶ *USB* ⟶ *Automatically connect when inserted*.

    ..  image:: terminalServerUSB.png

Proceed to the Section about :ref:`mk1eVSCodeWithPlatformIO`.

|

----

|

..  _mk1eVSCodeWithPlatformIO:

..  include:: ide-platformio-before-creating-project.rst

:\:[   ]: In resulting pop-up window, name the project *MyBlink*. In the "board" field, type *arduino nano* (:numref:`mk1eCreatingPlatformIOProject`\ (a)).

:\:[   ]: Unless you already know which bootloader your |developmentBoard| has, select "Arduino Nano ATmega328." After you do so, the "framework" field will auto-populate to "Arduino" (:numref:`mk1eCreatingPlatformIOProject`\ (b)).

..  _mk1eCreatingPlatformIOProject:
..  figure:: ../../../blank.png

    Selecting board and processor in the Arduino IDE.

    +----------------------------------------+-------------------------------------------------+
    | a                                      | b                                               |
    +========================================+=================================================+
    | .. image:: platformioSelectBoard.png   | .. image:: platformioReadyForNewProject.png     |
    |    :width: 8cm                         |    :width: 8cm                                  |
    |    :align: center                      |    :align: center                               |
    +----------------------------------------+-------------------------------------------------+
    | Selecting the board with PlatformIO.   | Ready to create a new project using PlatformIO. |
    +----------------------------------------+-------------------------------------------------+

..  include:: ide-platformio-after-creating-project.rst

If you are satisfied with using VS Code with PlatformIO, then proceed to :doc:`power-mk1e`.

|

----

..  [#sketches]
    | The Arduino language is based off of the Wiring language, which in turn is based off of the Processing language, which was designed to make computing accessible to artists.
..  [#usingC]
    | Your code in the I/O labs will be C code.
..  [#arduinoMain]
    | https://github.com/arduino/ArduinoCore-avr/blob/master/cores/arduino/main.cpp
..  [#usbConnection]
    | You can connect the USB cable to a "wall wart" USB power supply or to a USB battery pack if you only want to provide power to the Arduino Nano, but you need to connect it to a computer to upload a new sketch to the Arduino Nano.
