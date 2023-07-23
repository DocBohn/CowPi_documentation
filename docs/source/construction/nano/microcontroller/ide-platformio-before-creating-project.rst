
VS Code with the PlatformIO Plugin
----------------------------------

If you prefer to use VS Code, you can do so.
If you have not already installed VS Code, then `download and install <https://code.visualstudio.com/>`_ it.
Next, you need to `install the PlatformIO extension <https://platformio.org/install/ide?install=vscode>`_\ .
You may want to take a quick look at the `parts of the PlatformIO Toolbar <https://docs.platformio.org/en/latest/integration/ide/vscode.html#platformio-toolbar>`_\.


About PlatformIO and the Arduino Framework
""""""""""""""""""""""""""""""""""""""""""

PlatformIO is able to work with many frameworks;
for the I/O labs, we will use the Arduino framework.
As application programmers, the starting point is a C++ program\ [#usingC]_ in which you write two functions, ``setup()`` and ``loop()``, along with any helper code that you need.
PlatformIO will compile your program and link it to a ``main()`` function that looks something like:

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


:\:[   ]: Open VS Code on the computer that your |developmentBoard| is connected to.

On VS Code's left-side menu, you will see an bug head icon;
this is PlatformIO's logo.

..  image:: platformIOIcon.png

:\:[   ]: Click on the PlatformIO logo.

After a few seconds, a PlatformIO side-window will appear.

:\:[   ]: In that side-window, click on the "Create New Project" button.

This takes you to the "PlatformIO Home."

.. .. :\:[   ]: In PlatformIO Home, click on the "Project Examples" button.
.. ..
.. .. :\:[   ]: In resulting pop-up window, click on the "Select an example..." drop-down menu.
.. ..
.. .. :\:[   ]: In the drop-down menu, click on "arduino blink" (it should be the first option). Click on the "Import" button.
.. ..
.. .. You will need to wait a few seconds, and then a new project will be created whose name is derived from the current date and time, such as "230718-112959-arduino-blink."
.. .. This will create an example project with the same "blink" code that is typically loaded onto an Arduino Nano before leaving the factory.

:\:[   ]: In PlatformIO Home, under "Quick Access," click on the "+ New Project" button.