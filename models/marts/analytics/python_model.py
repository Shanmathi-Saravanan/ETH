import holidays
from snowflake.snowpark.functions import udf, col
from snowflake.snowpark.types import BooleanType


def model(dbt, session):

    dbt.config(
        materialized="table",
        packages=["holidays"],
        python_version="3.10"
    )

    fr_holidays = holidays.France()

    @udf(
        return_type=BooleanType(),
        input_types=[],
        packages=["holidays"],
        session=session,
    )
    def is_holiday(date_col):
        if date_col is None:
            return False
        return date_col in fr_holidays

    df = dbt.ref("stablecoin_activity_per_day")

    df = df.with_column(
        "IS_HOLIDAY",
        is_holiday(col("DATE"))
    )

    return df