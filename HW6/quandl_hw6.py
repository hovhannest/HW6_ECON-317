import quandl
from matplotlib import pyplot as plt
import pandas as pd

with open('../quandl_key.txt','r') as f:
    key = f.read()

###############################################################################################

# TT_PRI_MRCH_XD_WD - Net barter terms of trade index (2000 = 100)
# WWDI/ARM_NY_TTF_GNFS_KN Terms of trade adjustment (constant LCU) ???

data_arm = quandl.get('WWDI/ARM_TT_PRI_MRCH_XD_WD',authtoken=key)
data_lux = quandl.get('WWDI/LUX_TT_PRI_MRCH_XD_WD',authtoken=key)

plt.plot(data_arm, "r")
plt.plot(data_lux)

plt.show()

###############################################################################################

print('the 2nd highest value for Armenia is ' + str(data_arm.nlargest(2, "Value")['Value'][1]))

###############################################################################################

total_export = quandl.get('WWDI/ARM_TX_VAL_MRCH_CD_WT',authtoken=key)
total_import = quandl.get('WWDI/ARM_TM_VAL_MRCH_CD_WT',authtoken=key)

net_exports = total_export - total_import

plt.plot(net_exports)

plt.show()

###############################################################################################

cola = quandl.get('EOD/KO',authtoken=key)['Open']
nike = quandl.get('EOD/NKE',authtoken=key)['Open']
intel = quandl.get('EOD/INTC',authtoken=key)['Open']

df = pd.concat([cola, nike, intel], axis=1, join='inner')
df.columns = ['cola', 'nike', 'intel']
plt.matshow(df.corr())
plt.show()