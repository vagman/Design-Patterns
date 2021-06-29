"""
Target: defines the domain-specific interface used by the client code.

Adaptee: contains some useful behavior, but its interface is incompatible with 
the existing client code. The Adaptee needs some adaptation before the client can use it.

Adapter: makes the Adaptee's Abstract class compatible with the Target's interface via multiple inheritance.    

"""

from eu_power_plug_adapter import EUPowerPlugAdapter
from us_power_plug_adapter import USPowerPlugAdapter
from eu_power_plug import EUPowerPlug
from us_power_plug import USPowerPlug

eu_phone = EUPowerPlugAdapter()
us_phone = USPowerPlugAdapter()

# Compatibility
eu_phone.charge(EUPowerPlug.output_voltage)
us_phone.charge(USPowerPlug.output_voltage)

# Incompatibility of the Adapter
eu_phone.charge(USPowerPlug.output_voltage)
us_phone.charge(EUPowerPlug.output_voltage)