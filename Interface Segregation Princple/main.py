"""
Interface Segregation Principle

Make fine grained interfaces that are client specific
Clients should not be forced to depend upon interfaces that they do not use.
This principle deals with the disadvantages of implementing big interfaces.

Depending on something that carries baggage that you don't need can cause you troubles that you didn't expect 
~ Robert Martin

Documentation I found useful: https://www.brainstobytes.com/interface-segregation-principle/

"""

from developer import Developer

dev = Developer("John", 25, 18000)
new_dev_salary = dev.calculate_salary(4 * 1000)
print("------ Developers Note ------\nSalary was decreased from {}$ to {}$ due to lower working hours.".format(dev.get_salary(), new_dev_salary))
print("Break time has been increased from {}' to {}\'.\n".format(dev.break_time(), dev.break_time() * 4))