"""
Exception raised by the SmartphoneAdapter.
This exception represents the fact that an adapter can not provide the
right voltage to the Smartphone if the voltage of the Socket is wrong.
"""
class CannotTransformVoltage(Exception):
    pass