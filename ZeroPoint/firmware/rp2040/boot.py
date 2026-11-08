import usb_cdc
import usb_hid

usb_cdc.enable(console=True, data=True)
usb_hid.enable((usb_hid.Device.KEYBOARD,))


# By: UnJaitor
# https://github.com/UnJaitor


# Distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.
# Non-Commercial: You cannot sell hardware kits or use this project for financial gain.
# ShareAlike: Any modification or derivative work must remain open-source under the same terms.
