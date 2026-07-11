#aula 10 - mais sobre dados financeiros valor presente liquido e taxa minina de atratividade

#fluxo de capital
#funçoes financeiras

# É preciso instalar
# pip install numpy_financial <<

import numpy as np
import numpy_financial as npf

vi=-60000
rs=40000-10000
FC=np.array([vi,rs,rs,rs,rs,rs])

# calculo do VPL (NPV - net present value)
inv=npf.npv(0.12,FC)

print('VPL=',inv)
