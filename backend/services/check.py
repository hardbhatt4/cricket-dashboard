from data_loader import get_data
from kpi_service import get_kpi

df = get_data()

print(df.shape)
print(df.dtypes)
print(df["season"].unique())
print(df.isnull().sum())

print(get_kpi(None, None))
print(get_kpi("2007/08", None))
print(get_kpi(None, "Mumbai Indians"))
