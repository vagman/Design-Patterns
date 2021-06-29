# This class replicates the Client
class Phone():

    max_input_voltage = 5

    def outcome(self, input_voltage):
        if input_voltage > self.max_input_voltage:
            print("Input voltage: {}V -- BURNING!!!\n".format(input_voltage))
        else:
            print("Input voltage: {}V -- Charging...\n".format(input_voltage))

    def charge_device(self, input_voltage):
        self.outcome(input_voltage)