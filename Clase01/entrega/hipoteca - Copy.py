# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:03:34 2021

@author: Gustavo
"""
import time
inicio = time.time()
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

adelanto = 1000
mes = 0

pago_extra_mes_comienzo = 60
pago_extra_mes_fin = 107
pago_extra = 1000
print('Mes', '    ', 'Pagado', '        ', 'Saldo')
while saldo > 0:
    # while mes < 12 :
        # saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        # total_pagado = total_pagado + pago_mensual + adelanto
        # mes += 1
    saldo = saldo*(1+(tasa/12))
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else: 
        if saldo > pago_mensual:
            saldo = saldo - pago_mensual
            total_pagado = total_pagado + pago_mensual
        else:
            pago_mensual = saldo 
            saldo = saldo - pago_mensual
            total_pagado = total_pagado + pago_mensual

    mes += 1
    print(mes,'    ', round(total_pagado, 2), '        ', round(saldo, 2))
print('Total Pagado: ', round(total_pagado, 2))
print('Meses: ', mes)
fin = time.time()
print(inicio-fin)