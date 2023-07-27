Example Code
============

The CowPi library has two code examples.

..  contents::

|

..  _io_test:

io_test
-------

The *io_test* example demonstrates the use of the library's :doc:`inputs` and :doc:`outputs`, including :ref:`debouncing`\ .
Its primary purpose, however, is to validate the correct placement of a Cow Pi board's components when following the :doc:`../construction`\ .

..  NOTE::
    The compile-time conditionals (``#ifdef __AVR__``) are there to move the print statement's format strings into flash memory on AVR platforms,\ [#]_
    while also working correctly on ARM platforms that do not support this feature.
    That this example must work for all microcontrollers that could be used on a Cow Pi board requires that either we leave those constants in SRAM or that we use compile-time conditionals to optimize for AVR platforms when we can.

    In practice, you should simply write your code for your target unless you need to be both portable and also optimal for all targets.


..  code:: cpp

    #include <CowPi.h>

    void setup(void) {
        cowpi_setup(9600,
                    (cowpi_display_module_t) {.display_module = NO_MODULE},
                    (cowpi_display_module_protocol_t) {.protocol = NO_PROTOCOL}
        );

    #ifdef __AVR__
        printf_P(PSTR("CowPi library version %s\n"), COWPI_VERSION);

        printf_P(PSTR("The simple I/O test will print the status of the keypad and of each\n"));
        printf_P(PSTR("\tbutton, switch, and LED every time there is a change.\n\n"));
    #else
        printf("CowPi library version %s\n", COWPI_VERSION);

        printf("The simple I/O test will print the status of the keypad and of each\n");
        printf("\tbutton, switch, and LED every time there is a change.\n\n");
    #endif //__AVR__
    }

    void loop(void) {
        static bool left_button_was_pressed = false;
        static bool right_button_was_pressed = false;
        static bool left_switch_was_in_left_position = false;
        static bool right_switch_was_in_left_position = false;
        static char previous_key = 'z';     // this is impossible and will trigger the initial status "update"
        bool left_button_is_pressed = cowpi_debounce_byte(cowpi_left_button_is_pressed(), LEFT_BUTTON_DOWN);
        bool right_button_is_pressed = cowpi_debounce_byte(cowpi_right_button_is_pressed(), RIGHT_BUTTON_DOWN);
        bool left_switch_is_in_left_position = cowpi_debounce_byte(cowpi_left_switch_is_in_left_position(),
                                                                   LEFT_SWITCH_LEFT);
        bool right_switch_is_in_left_position = cowpi_debounce_byte(cowpi_right_switch_is_in_left_position(),
                                                                    RIGHT_SWITCH_LEFT);
        char current_key = (char) cowpi_debounce_byte(cowpi_get_keypress(), KEYPAD);
        bool update_is_needed = ((left_button_is_pressed != left_button_was_pressed)
                                 || (right_button_is_pressed != right_button_was_pressed)
                                 || (left_switch_is_in_left_position != left_switch_was_in_left_position)
                                 || (right_switch_is_in_left_position != right_switch_was_in_left_position)
                                 || (current_key != previous_key));
        if (update_is_needed) {
            left_button_was_pressed = left_button_is_pressed;
            right_button_was_pressed = right_button_is_pressed;
            left_switch_was_in_left_position = left_switch_is_in_left_position;
            right_switch_was_in_left_position = right_switch_is_in_left_position;
            previous_key = current_key;
            bool illuminate_left_led = left_button_is_pressed && !left_switch_is_in_left_position;
            bool illuminate_right_led = right_button_is_pressed && !right_switch_is_in_left_position;
            char c;
    #ifdef __AVR__
            printf_P(PSTR("Keypad:      %-5c    Column pins:  %d%d%d%d\n"),
                     (c = current_key) ? c : '-', digitalRead(A0), digitalRead(A1), digitalRead(A2), digitalRead(A3));
            printf_P(PSTR("Left switch: %-5s    Right switch: %s\n"),
                     left_switch_is_in_left_position ? "LEFT" : "RIGHT",
                     right_switch_is_in_left_position ? "LEFT" : "RIGHT");
            printf_P(PSTR("Left button: %-5s    Right button: %s\n"),
                     left_button_is_pressed ? "DOWN" : "UP",
                     right_button_is_pressed ? "DOWN" : "UP");
            printf_P(PSTR("Left LED:    %-5s    Right LED:    %s\n\n"),
                     illuminate_left_led ? "ON" : "OFF",
                     illuminate_right_led ? "ON " : "OFF");
    #else
            printf("Keypad:      %-5c    Column pins:  %d%d%d%d\n",
                   (c = current_key) ? c : '-', digitalRead(A0), digitalRead(A1), digitalRead(A2), digitalRead(A3));
            printf("Left switch: %-5s    Right switch: %s\n",
                   left_switch_is_in_left_position ? "LEFT" : "RIGHT",
                   right_switch_is_in_left_position ? "LEFT" : "RIGHT");
            printf("Left button: %-5s    Right button: %s\n",
                   left_button_is_pressed ? "DOWN" : "UP",
                   right_button_is_pressed ? "DOWN" : "UP");
            printf("Left LED:    %-5s    Right LED:    %s\n\n",
                   illuminate_left_led ? "ON" : "OFF",
                   illuminate_right_led ? "ON " : "OFF");
    #endif //__AVR__
            if (illuminate_left_led) {
                cowpi_illuminate_left_led();
            } else {
                cowpi_deluminate_left_led();
            }
            if (illuminate_right_led) {
                cowpi_illuminate_right_led();
            } else {
                cowpi_deluminate_right_led();
            }
        }
    }

|

----

..  _pin_interrupts:

pin_interrupts
--------------

This example demonstrates the use of :func:`cowpi_register_pin_ISR`.
It shows that more than one pin can be handled by the same ISR,
and it shows that different pins on the same I/O bank can be assigned to different ISRs.\ [#]_

This example also demonstrates a macro that can be used to debounce mechanical inputs that trigger interrupts.
Note also the busy-wait code in the ISRs.
As shown in ``handle_right_button()``, if the input's value can be inferred then the input's value does not need to be explicitly read, and there is no race condition.
However, as shown in ``handle_keypad()``, if the input's value *must* be read, then there is a race condition:
it is possible that in the time between the input changing (triggering the interrupt) and the ISR reading the input's value, the mechanical device bounced back to its original position, causing the wrong value to be read.
The race condition is resolved by busy-waiting until the input is different than what it previously had been (see the highlighted line in ``handle_keypad()``).
If we must explicitly read the input then clearly we don't know what the value *should* be;
however, just as clearly, we know that the new value is *not* the previous value
(otherwise, the interrupt would not have been fired).


..  code-block:: cpp
    :emphasize-lines: 54

    #include <CowPi.h>

    void handle_keypad(void);
    void handle_left_button(void);
    void handle_right_button(void);

    #define DEBOUNCE_THRESHOLD 20

    // using triggers for human-scale events, such as pressing buttons, is probably
    // better handled with polling, but for this demonstration, the only certain
    // inputs are from the keypad, pushbuttons, and slide switches. Because those
    // mechanical devices will bounce, let's make sure there's only one interrupt
    // fired per press/release/toggle.
    #define debounce_interrupt(action)                            \
      do {                                                        \
        static unsigned long last_trigger = 0L;                   \
        unsigned long now = millis();                             \
        if (now - last_trigger > DEBOUNCE_THRESHOLD) { action; }  \
        last_trigger = now;                                       \
      } while(0)

    static volatile char last_key;
    static volatile uint8_t last_left_button;
    static volatile uint8_t last_right_button;

    void setup() {
        cowpi_setup(9600,
                    (cowpi_display_module_t) {.display_module = NO_MODULE},
                    (cowpi_display_module_protocol_t) {.protocol = NO_PROTOCOL}
        );
        // make sure we know what the initial conditions are, so we handle the race conditions properly (see below)
        last_key = cowpi_get_keypress();
        last_left_button = cowpi_left_button_is_pressed();
        last_right_button = cowpi_right_button_is_pressed();
        // demonstrates multiple pins using the same handler
        cowpi_register_pin_ISR((1L << 14) | (1L << 15) | (1L << 16) | (1L << 17), handle_keypad);
        // demonstrates different pins on the same I/O bank (for ATmega328P) using different handlers
        cowpi_register_pin_ISR(1L << 8, handle_left_button);
        cowpi_register_pin_ISR(1L << 9, handle_right_button);
    }

    void loop() {
        ;
    }

    void handle_keypad(void) {
        debounce_interrupt({
            char key;
            // When scanning the keypad to figure out which key was pressed, it's possible that the key bounced, and we
            // see the key in its previous (unpressed) position. Similarly, on a key release, a bounce would make us see
            // the key as pressed. So we'll just keep scanning the keypad until we see something different from what we
            // saw before (something *must* be different, or there wouldn't have been an interrupt).
            // busy-wait through the race condition
            while ((key = cowpi_get_keypress()) == last_key) {}

            // you *really* shouldn't print in an ISR! but this is for demonstration purposes
            printf("keypad: %#4x\n", cowpi_get_keypress());

            last_key = key;
        });
    }

    void handle_left_button(void) {
        debounce_interrupt({
            uint8_t this_position;
            // busy-wait through the race condition
            while ((this_position = cowpi_left_button_is_pressed()) == last_left_button) {}

            printf("left button is %s\n", this_position? "pressed" : "released");

            last_left_button = this_position;
        });
    }

    void handle_right_button(void) {
        debounce_interrupt({
            // since the new position MUST be the opposite of the old position, we could simply invert `last_right_button`
            // instead of reading the button's position
            uint8_t this_position = !last_right_button;

            printf("right button is %s\n", this_position? "down" : "up");

            last_right_button = this_position;
        });
    }


..  [#] The 315 bytes' worth of string constants would otherwise consume over 15% of the ATmega328P's SRAM.
..  [#] On the AVR platforms, pin change interrupts require that a single ISR be assigned to all pins on the same I/O bank.
        (This is probably why Arduino's ``attach_interrupt()`` code is limited: on *some* pins, a different type of interrupt can be registered, with a separate ISR for each pin.)
        The CowPi library's :func:`cowpi_register_pin_ISR` function does not suffer this limitation.