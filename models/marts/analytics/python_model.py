import holidays


def model(dbt, session):

    dbt.config(
        materialized="table",
        packages=["holidays"],
        python_version="3.10"
    )

    df = dbt.ref("stablecoin_activity_per_day")

    # Simple transformation to prove Python model works
    return df