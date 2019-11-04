import uasyncio as asyncio

from base_node import BaseDriver, replace


PX, PY, PZ = 2, 3, 4
DX, DY, DZ = 5, 6, 7
OE = 8


def initialize(m5_stepmotor, **kwargs):
    config = m5_stepmotor.config
    print(config)
    pin_mode_bytes = bytearray(config.pin_mode_bytes)
    pin_state_bytes = bytearray(config.pin_state_bytes)
    print('mode:', [v for v in pin_mode_bytes])
    print('state:', [v for v in pin_state_bytes])

    for pin in (PX, PY, PZ, DX, DY, DZ, OE):
        port = pin // 8
        port_pin = pin % 8
        pin_mode_bytes[port] |= 1 << port_pin
        if pin == OE:
            pin_state_bytes[port] |= 1 << port_pin
        else:
            pin_state_bytes[port] &= ~(1 << port_pin)

    print('mode:', [v for v in pin_mode_bytes])
    print('state:', [v for v in pin_state_bytes])
    new_config = replace(config, pin_mode_bytes=pin_mode_bytes,
                         pin_state_bytes=pin_state_bytes,
                         **kwargs)
    print(new_config)
    m5_stepmotor.config = new_config
    # Re-initialize according to the new configuration.
    m5_stepmotor.load_config()


class M5Stepmotor(BaseDriver):
    def __init__(self):
        pass

    def begin(self, i2c, addr):
        super().__init__(i2c, addr)
        # Disable motor output.
        self.digital_write(OE, 1)
        for pin in (PX, PY, PZ, DX, DY, DZ):
            self.pin_mode(pin, 1)
            self.digital_write(pin, 0)

    async def _move(self, pulse_pin, direction_pin, pulses, direction):
        self.digital_write(OE, 0)
        self.digital_write(direction_pin, direction)
        for i in range(pulses):
            self.digital_write(pulse_pin, 1)
            await asyncio.sleep_ms(2)
            self.digital_write(pulse_pin, 0)
            await asyncio.sleep_ms(2)
        self.digital_write(OE, 1)

    async def move_x(self, *args):
        return await self._move(PX, DX, *args)

    async def move_y(self, *args):
        return await self._move(PY, DY, *args)

    async def move_z(self, *args):
        return await self._move(PZ, DZ, *args)
