# %%
import pandas as pd
from pathlib import Path

ddir = Path(__file__).parent.with_name("data")
cfile = ddir / "castaway_processed_example_CC1606011_20200811_122016.csv"
# %%

df = pd.read_csv(cfile, skiprows=28, index_col=1)
# %%
