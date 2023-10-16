import sys
import pandas as pd

df = pd.concat(
    (pd.read_csv(f, index_col=None, parse_dates=[['gps_Date', 'gps_Time']])
     for f in sys.argv[1:]),
    axis=0,
    ignore_index=True)

df = df.rename(columns={'gps_Date_gps_Time': 'time'}).set_index('time')

df['gps_Lat'] = df['gps_Lat'] * 1.e-7
df['gps_Long'] = df['gps_Long'] * 1.e-7
df['gps_Alt'] = df['gps_Alt'] * 1.e-3
df['gps_AltMSL'] = df['gps_AltMSL'] * 1.e-3
df['gps_GroundSpeed'] = df['gps_GroundSpeed'] * 1.e-3
df['gps_Heading'] = df['gps_Heading'] * 1.e-5
df['gps_pDOP'] = df['gps_pDOP'] * 1.e-2

print(df)
print(df.iloc[-1])
