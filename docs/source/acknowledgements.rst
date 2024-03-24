****************
Acknowledgements
****************

.. .. Why does clion provide syntactic highlighting for this file until I start typing? It doesn't happen on others (except modification.rst)

-   Adafruit

    `Adafruit <https://www.adafruit.com/>`_ very actively works to raise the proverbial tide.
    To the best of my knowledge, Adafruit publishes all of its hardware designs as open-source hardware
    and has created many open-source software libraries that the "Makers" community relies on.
    They also have produced many guided tutorials and educational guides.
    These guides are referenced within this datasheet:

    -   `All About LEDs <https://learn.adafruit.com/all-about-leds?view=all>`_
    -   `Breadboards for Beginners <https://learn.adafruit.com/breadboards-for-beginners?view=all>`_

-   SparkFun

    `SparkFun <https://www.sparkfun.com/>`_ also strives to make hobby electronics accessible to everyone.
    SparkFun publishes most of its hardware designs as open-source hardware and has created some open-source libraries.
    They also have produced many guided tutorials and educational guides.
    These guides are referenced within this datasheet:

    -   `Button and Switch Basics <https://learn.sparkfun.com/tutorials/button-and-switch-basics>`_
    -   `Light-Emitting Diodes (LEDs) <https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds>`_
    -   `How to Use a Breadboard <https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard>`_
    -   `How to Install CH340 Drivers <https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers>`_

-   Arduino

    Arduino has created many inexpensive microcontroller boards (and some not-so-inexpensive ones) and publishes many of their designs as open-source hardware.
    Arduino also created a development framework that makes programming microcontrollers accessible to beginners.
    Many of the Cow Pi circuits use Arduino microcontroller boards because of this.

-   Raspberry Pi

    The original Raspberry Pi computer was created to make the entry-point to programming "desktop" computers very inexpensive ("desktop" in quotation marks because the Raspberry Pi is a single-board computer quite suitable for many embedded applictions).
    When Raspberry Pi released the Raspberry Pi Pico microcontroller board, they made a "name-brand" microcontroller board that is less expensive than most Arduino clones -- and soon even the cheapest Arduino clones were twice as expensive as the Pico due to Pandemic-related supply chain issues.
    Along with the Raspberry Pi Pico, they released the RP2040 microcontroller that has since become a staple replacement for the microcontroller in many products --
    Pandemic-related supply chain issues decreased the availability of microcontrollers that had many products relying on them, but the timing of the RP2040's release meant that there were no existing products relying on it.
    Many of the Raspberry Pi hardware designs are published as open-source hardware.
    The Raspberry Pi Pico will probably be the go-to microcontroller for future Cow Pi designs for some time,
    due to it being inexpensive, has enough pins that they don't need to serve multiple purposes for the Cow Pi, and has other attractive features for the lessons and assignments that I create.

-   NXP Semiconductors

    The 3.3V/5V voltage shifting circuit that is part of the Cow Pi mk4a and mk4b designs comes from `NXP Application Note AN10441 "Level shifting techniques in I2C-bus design" <https://web.archive.org/web/20210907180148/https://www.nxp.com/docs/en/application-note/AN10441.pdf>`_.

-   The Internet Archive

    The aforementioned Application Note is not currently available on the NXP website but is available in through the Internet Archive's Wayback Machine.

-   The UNL Engineering Electronics Shop

    The College of Engineering's EE Shop has been instrumental in sourcing inexpensive components for "class kits" that allow students to assemble Cow Pi mk1 circuits
    and in working through the quirks of Arduino Nano clones' evolving USB designs (and of Microsoft Windows' drivers for those USB designs).

-   The UNL School of Computing's SysAdmin Team

    The School of Computing's SysAdmin team has been of great help directly for our students and also in maintaining lab computer, terminal server, and virtual machine options for our students.

-   My students and teaching assistants

    Being in control of the hardware and libraries that my students use for assignments gives me the ability to make changes to focus the student's efforts on the learning objectives and not on accidents of design.
    A key part of evolving the Cow Pi hardware and, to a greater degree, the CowPi and CowPi_stdio libraries, has been feedback from my students and teaching assistants.

|

About the Cow Pi logo

    The "Cow Pi" logo found on the Cow Pi mk3 PCBs, and on this datasheet, consists of
    the "Cow Face" emoji (🐮) in Google's `Noto Emoji <https://fonts.google.com/noto/specimen/Noto+Emoji>`_ font
    and the mathematical "Pi" symbol (𝜋) from Apple's implementation of the Cambria Math font.

.. .. https://fonts.google.com/noto/specimen/Noto+Sans+Math

