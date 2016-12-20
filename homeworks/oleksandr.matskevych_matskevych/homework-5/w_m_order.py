from washing_machine import washing_machine
from washing_machine_smart import washing_machine_smart


order = washing_machine('1000 rpm', 'yes', 'clean')
print(order)
print(order.order_w_m())

order2 = washing_machine_smart('bosch', '1100 rpm', 'yes', 'clean', 'control app')
print(order2)
print(order.order_w_m_s())
