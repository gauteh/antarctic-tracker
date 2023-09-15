# GPS and barometric tracker based on the OpenLogArtemis for accurate determiniation of height and position

Configured for the OpenLogArtemis with the [LPS28DFW pressure sensor](https://github.com/sparkfun/OpenLog_Artemis/pull/179).

## Hardware

* [OpenLog Artemis](https://www.sparkfun.com/products/19426)
* [MAX-M10S](https://www.sparkfun.com/products/18037) (GPS receiver)
* [LPS28DFW](https://www.sparkfun.com/products/21221) (Pressure sensor)
* micro SD card

## Power and charging

The charging circuit is designed for Lithium-Ion batteries and provides _450
mA_ at _3.7 V_. That means that the capacity of the battery should be at least
_450 mAh_. See [OpenLog power](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/hardware-overview#power) for more information.
