********************************************
Troubleshooting Connections to Arduino Nanos
********************************************

..  contents:: \


Windows
=======

Selecting the Correct "Processor"
---------------------------------

There are *three* choices for the Arduino Nano's processor, two of which specify the ATmega328P processor.
Even though the difference is with the bootloader, it is resolved through the Arduino IDE's "Processor" selection:

-   Official Arduino Nanos and some clones use the "new bootloader".
    Under the "Tools" menu, when choosing "Processor", select "ATmega328P".

-   Older official Arduino Nanos and some clones use the "old bootloader".
    Under the "Tools" menu, when choosing "Processor", select "ATmega328P (Old Bootloader)"

-   Very old Arduino Nanos use the ATmega168 processor.
    If you have such a device, replace it with a newer Arduino Nano.

Updating Windows USB Driver if Necessary
----------------------------------------

Official Arduino Nanos use the FT232RL USB interface chip.
*Most* Arduino Nano clones use the CH340 USB interface chip.

We have seen some Windows computers without the CH340 USB driver.
If you encounter this problem and the Device Manager shows you the warning in :numref:`usbIssues`\ (a),
then the first thing to try is updating the driver.
Right-click on "USB2.0-Ser!" and choose "Update driver" (:numref:`usbIssues`\ (b)).
Then choose "Search automatically for updated driver software".

.. _usbIssues:
.. figure:: ../blank.png

    Some Windows computers lack the CH340 USB driver.

    +---------------------------------------+------------------------------+
    | a                                     | b                            |
    +=======================================+==============================+
    | .. image:: device-manager-warning.png | .. image:: update-driver.jpg |
    |    :width: 8cm                        |    :width: 8cm               |
    |    :align: center                     |    :align: center            |
    +---------------------------------------+------------------------------+

If Windows reports that "Windows has successfully updated your drivers" then you should now be able to connect to the Arduino Nano.
On the other hand, if Windows reports that "Windows was unable to install your USB2.0-Ser!", then the `How to Install CH340 Drivers <https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/>`_ page at sparkfun.com will guide you through manually downloading the driver and installing it.

No Driver Warning but Cannot Connect
------------------------------------

Standard Answer
"""""""""""""""

If you see no warnings but your Windows computer still won't communicate with the Arduino Nano
then probably what happened is that your computer has the driver, but you're telling the IDE to connect to the wrong virtual COM port.
The typical way to handle this is to
disconnect the Arduino Nano from your computer,
go to the part of the menu where you connect to the COM port,
connect the Arduino Nano to your computer,
and select whichever COM port appears after plugging in the Arduino Nano.

.. _Windows11CH340:

Windows 11 and Arduino Nano Clones
""""""""""""""""""""""""""""""""""

We have seen problems with Windows 11 and Arduino Nano Clones, with error messages similar to:

.. code-block:: console

    avrdude: ser_open(): can't set com-state for "\\.\COM3"

As the staff at the EE Shop has worked to troubleshoot this, there were indications that the problem was with the Arduino IDE 2.1.0;
**if you see this problem with the Arduino IDE 2.1.1, please let us know.**

Another fix that seems to work is to install the latest CH340/341 drivers from https://oemdrivers.com/usb-ch340 :

    When you download and un-ZIP this package, you end up with folders containing .INF and other files.
    A common way to upgrade Windows device drivers is to select the device in Device Manager, tell it to update drivers and click on the option to browse your computer for the drivers.
    Usually you select the directory containing those files and Windows uses them.
    I found that when I tried this Windows insisted "no, the drivers already installed are the best."

    However this driver package also includes a couple executable programs that you
    just run to install the driver, and that works.  (One in the main folder, one in
    the "W1X" folder.  As far as I can tell they do the same thing.)

Finally:

    On Windows 11, the first time after launching the IDE,  your code should compile and upload with no complaints.
    But your next upload will fail  .... UNLESS you
    unplug the Nano from the computer, letting it's COMx port "go away", then plug
    it back in so Windows and the IDE  "rediscover" it.
    (The IDE immediately picks up using the same port settings when you plug it in.)
    And then you can upload another sketch.
    This is inconvenient but not majorly so, considering the payoff is that uploads can be depended upon to work when you do this.

    All the above is the same under Windows 10, except Win10 doesn't have the "I'll only upload once" problem,
    and you can leave your board plugged in as long as you like.

Handling Errors
---------------

If you get an error when attempting to upload a sketch, try these corrective measures:

#.  Try selecting "ATmega328P" and try selecting "ATmega328P (Old Bootloader)".

#.  Try uploading again (if you attempt to upload a sketch too soon after connecting your Arduino Nano to your computer, the USB interface won't have finished its handshake).

#.  The `Troubleshooting Guide <https://support.arduino.cc/hc/en-us/articles/4401874331410--Error-avrdude-when-uploading>`_ recommends disconnecting your Arduino Nano and reconnecting it, then selecting whichever COM port appears.

#.  Review the discussion at :ref:`Windows11CH340`.

If, instead of an error, your IDE "hangs" while collecting configuration data, try this corrective measure:

-   Press the ``RESET`` button in the middle of the Arduino Nano;
    the IDE should begin uploading the sketch after you release the button.


MacOS
=====

Sparkfun's `How to Install CH340 Drivers <https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/>`_ page also has instructions for installing the driver on MacOS;
however, we are not aware of any students needing to manually install the CH340 driver on MacOS.

Linux
=====

Sparkfun's `How to Install CH340 Drivers <https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/>`_ page also has instructions for installing the driver on Linux;
however, we are not aware of any students using Linux personal laptops in this course.
