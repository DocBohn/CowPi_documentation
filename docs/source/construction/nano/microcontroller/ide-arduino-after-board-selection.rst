Selecting the Correct "Processor"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are *three* choices for the Arduino Nano's processor, two of which specify the ATmega328P processor.
Even though the difference is with the bootloader, it is resolved through the Arduino IDE's "Processor" selection:

-   Official Arduino Nanos and some clones use the "new bootloader".
    Under the "Tools" menu, when choosing "Processor", select "ATmega328P".

-   Older official Arduino Nanos and some clones use the "old bootloader".
    Under the "Tools" menu, when choosing "Processor", select "ATmega328P (Old Bootloader)"

-   Very old Arduino Nanos use the ATmega168 processor.
    If you have such a device, replace it with a newer Arduino Nano.

:\:[   ]: Unless you already know which bootloader your |developmentBoard| has, select "ATmega328P."

..  NOTE::
    On the following pages, some of the |developmentBoard|\ s have a label indicating which bootloader they have.
    If you have only one |developmentBoard|, you do not need to label it;
    however, if you have many |developmentBoard|\ s, you may find that labeling them will help you keep track of which bootloader to select.

    Whether you have an old bootloader  or a new bootloader does not affect any steps you need to take, except that you need to select the correct one in order to upload the programs to your |developmentBoard|\ .


Updating Windows USB Driver if Necessary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Official Arduino Nanos use the FT232RL USB interface chip.
*Most* Arduino Nano clones use the CH340 USB interface chip.
We have seen some Windows 10 computers without the CH340 USB driver,
and we have seen that some Windows 11 computers need their CH340 USB driver updated.

See :doc:`../../../troubleshooting/nano` for instructions to handle these problems.

If you are unable to get your Windows 11 computer to work with your Arduino Nano, then you should consider using a lab computer or terminal server for the I/O labs since they still run Windows 10. [#toughLuck]_


Upload a New Sketch
"""""""""""""""""""

:\:[   ]: From the Arduino IDE's File menu, open the *Blink.ino* example:
    *File* ⟶ *Examples* ⟶ *01.Basics* ⟶ *Blink*

:\:[   ]: Select *Save As...* and save the project as *MyBlink*.

:\:[   ]: Edit the values in the ``delay()`` calls to change the delays between the LED turning on, off, and on again.
    Select values that will visibly have a difference, such as 250 or 2000.

:\:[   ]: Compile the program using the "Verify" checkmark in the IDE's toolbar and make corrections if the program doesn't compile.

:\:[   ]: Upload the program to your |developmentBoard| using the "Upload" arrow in the IDE's toolbar.
    (If you forget to compile first, the IDE will compile your program before uploading, but I find it useful to find compile-time mistakes before attempting to upload the program.)

|

-   If you successfully uploaded *MyBlink.ino* then you will see the following in the IDE's *Output* window:

    .. code-block:: console

              avrdude: AVR device initialized and ready to accept instructions

              Reading | ################################################## | 100% 0.01s

              avrdude: Device signature = 0x1e950f (probably m328p)
              avrdude: reading input file "/var/folders/p7/lx4gt70d0_34cpy8r0j3c95c0000gp/T/arduino-sketch-11A4823C54657006C9F78B0812B621A8/MyBlink.ino.hex"
              avrdude: writing flash (932 bytes):

              Writing | ################################################## | 100% 0.33s

              avrdude: 932 bytes of flash written

              avrdude done.  Thank you.


              --------------------------
              upload complete.

    and then the LED's on-off pattern will change, reflecting the ``delay()`` values you assigned.

    ..  image:: animations/myblink.gif
        :height: 3cm
        :align: center

|

-   If you did not successfully upload *MyBlink.ino* then you will see the following in the IDE's *Output* window:

    .. code-block:: console

              ...

:\:[   ]: If you did not successfully upload *MyBlink.ino*, then change your "Processor" selection to "ATmega328P (Old Bootloader)".

:\:[   ]: Upload the program to your |developmentBoard| using the "Upload" arrow in the IDE's toolbar.

|

Handling Errors
~~~~~~~~~~~~~~~

If you get an error when attempting to upload a sketch that is not resolved by changing the "Processor" selection, see :doc:`../../../troubleshooting/nano` for guidance to handle these problems.

If, instead of an error, your IDE "hangs" while collecting configuration data, try this corrective measure:

-   Press the ``RESET`` button in the middle of the Arduino Nano;
    the IDE should begin uploading the sketch after you release the button.

|

..  ATTENTION::
    **CHECKPOINT 2**
    | |checkpoint| uploaded new code to the |developmentBoard|. |updateCheckpointsTXT|
