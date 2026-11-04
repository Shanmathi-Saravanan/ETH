import holidays
from snowflake.snowpark.functions import udf, col
from snowflake.snowpark.types import BooleanType

def model(dbt, session):

    dbt.config(
        materialized="table",
        packages=["holidays"]
        python_version="3.10"
    )

    @udf(
        packages=["holidays"],
        return_type=BooleanType(),
        session=session
    )
    def is_holiday(date_col):
        return date_col in holidays.France()

    df = dbt.ref("stablecoin_activity_per_day")

    df = df.with_column(
        "IS_HOLIDAY",
        is_holiday(col("DATE"))
    )

    return df