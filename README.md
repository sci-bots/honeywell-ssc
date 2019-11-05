# Honeywell SSC Series pressure sensors driver #

MicroPython driver for [Honeywell TruStability(R) SSC Series][honeywell-ssc]
I2C pressure sensors.

# Usage

```python
>>> from honeywell_ssc import HoneywellSSC
>>>
>>> sensor = HoneywellSSC(i2c, addr=0x28)
>>> sensor.read()  # Ambient pressure (PSI)
0.4467772
```

-------------------------------------------------------------------------------

Install
-------

The latest [`honeywell-ssc` release][1] is available as a
[Conda][2] package from the [`sci-bots`][2] channel.

To install `honeywell-ssc` in an **activated Conda environment**, run:

    conda install -c sci-bots -c conda-forge honeywell-ssc

This installs the MicroPython source files into the following path:

    $env:CONDA_PREFIX/share/platformio/micropython-lib/honeywell_ssc

-------------------------------------------------------------------------------

License
-------

This project is licensed under the terms of the [BSD license](/LICENSE.md)

-------------------------------------------------------------------------------

Contributors
------------

 - Christian Fobel ([@sci-bots](https://github.com/sci-bots))


[1]: https://github.com/sci-bots/honeywell-ssc
[2]: https://anaconda.org/sci-bots/honeywell-ssc
[honeywell-ssc]: https://sensing.honeywell.com/honeywell-sensing-trustability-ssc-series-standard-accuracy-board-mount-pressure-sensors-50099533-a-en.pdf
