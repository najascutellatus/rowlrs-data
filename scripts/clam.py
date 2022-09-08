# %%
import pandas as pd
from pathlib import Path

ddir = Path(__file__).parent.with_name("data")
cfile = ddir / "ExampleClamData.xlsx"

# %%
trip_dtype = {
    "Start_Lat": float,
    "Start_Lon": float,
    "Stop_Lat": float,
    "Stop_Lon": float,
    "ByCatch?": bool,
}

# with open(cfile) as f:
data_trip = pd.read_excel(cfile, sheet_name="TripLevelData", parse_dates={"time": [0, 1, 2, 3]}, index_col=[0])
data_tow = pd.read_excel(cfile, sheet_name="TowLevelData")



# %%
