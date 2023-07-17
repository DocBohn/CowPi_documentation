Arduino IDE
-----------

The Arduino IDE is installed on the lab computers.
If you choose to install the Arduino IDE on your personal laptop, you can download it from https://www.arduino.cc/en/software
and follow the `installation instructions <https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing>`_.
Alternatively, you can install a browser plugin to use the `Arduino Web Editor <https://docs.arduino.cc/arduino-cloud/getting-started/getting-started-web-editor>`_.

About Arduino Programs
""""""""""""""""""""""

An Arduino program is called a *sketch* for historical reasons.\ [#sketches]_
For all intents and purposes, you can think of it as a C++ program\ [#usingC]_ in which you write two functions, ``setup()`` and ``loop()``, along with any helper code that you need.
The file extension for sketches is *.ino* (as in, Ardu\ *ino*).
The Arduino IDE will compile your sketch and link it to a ``main()`` function that looks something like:

.. code-block:: c

    int main(void) {
        setup();
        while(true) {
            loop();
        }
    }

(The actual ``main()`` function\ [#arduinoMain]_ also calls a few other functions from the Arduino core library.)

Connect to the |developmentBoard|
"""""""""""""""""""""""""""""""""

:\:[   ]: Review the `instructions to upload a program <https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-uploading-a-sketch>`_.

:\:[   ]: Connect one end of the USB cable to a lab computer or to your personal laptop.\ [#usbConnection]_

:\:[   ]: Connect the other end of the cable to your |developmentBoard|.


The ``PWR`` LED will light up, and you may see the ``L`` LED repeatedly blink on-and-off.
The ``L`` LED is connected to the |developmentBoard|'s pin D13, and Arduino microcontroller boards typically leave the factory with *Blink.ino* loaded, but it does not matter if yours does not have *Blink.ino* pre-loaded.

.. code-block:: cpp

    // the setup function runs once when you press reset or power the board
    void setup(void) {
        // initialize digital pin LED_BUILTIN as an output.
        pinMode(LED_BUILTIN, OUTPUT);
    }

    // the loop function runs over and over again forever
    void loop(void) {
        digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(1000);                       // wait for a second
        digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
        delay(1000);                       // wait for a second
    }


:\:[   ]: Open the Arduino IDE on the computer that your |developmentBoard| is connected to.

:\:[   ]: Connect the Arduino IDE to the Arduino Nano.


Arduino claims that the board and COM port (Windows) or TTY port (Mac/Linux) will be detected automatically.
We have found that automatic detection is unlikely with non-official boards.
