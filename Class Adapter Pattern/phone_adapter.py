from phone import Phone
from power_plug import PowerPlug
from cannot_transform_voltage import CannotTransformVoltage

class PhoneAdapter(Phone, PowerPlug):

    def transform_voltage(self, input_voltage):
        if input_voltage == self.output_voltage:
            return self.max_input_voltage
        else:
            raise CannotTransformVoltage("Can\'t transform {0}-{1}V. This adapter transforms {2}-{1}V.\n".format(input_voltage, self.max_input_voltage, self.output_voltage))

    def charge(self, input_voltage):
        try:
            voltage = self.transform_voltage(input_voltage)
            self.outcome(voltage)
        except CannotTransformVoltage as e:
            print(e)