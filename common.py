"""Shared setup for the samples."""
from pytrends.request import TrendReq

# tz is a time zone offset in minutes with the sign reversed, the same way as
# JavaScript's Date.getTimezoneOffset(): KST (UTC+9) is -540, US CST (UTC-6) is 360.
# The time index of the results is always in UTC. See to_local_time() below.
TZ_OFFSET = -540
LOCAL_TZ = "Asia/Seoul"


def make_client():
    return TrendReq(hl="en-US", tz=TZ_OFFSET, timeout=(10, 25))


def to_local_time(df):
    """Convert the UTC time index of interest_over_time() to local time."""
    df = df.copy()
    df.index = df.index.tz_localize("UTC").tz_convert(LOCAL_TZ)
    return df


def drop_partial(df):
    """Drop rows whose period is not over yet, and the isPartial column."""
    if "isPartial" not in df:
        return df
    return df[~df["isPartial"]].drop(columns="isPartial")
