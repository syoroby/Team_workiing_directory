##y=x그래프 그리기##

import matplotlib.pyplot as plt
x=[a for a in range(11)]
y=[b for b in range(11)]
plt.plot(x,y)
plt.show()

##이차함수 그래프 y=x**2->주피터에서 구현 가능##

import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


##사인함수 구현-> 주피터에서 구현가능##
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)
y=np.sin(x)
plt.pㅣot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
