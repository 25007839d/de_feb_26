{{ config(
    materialized='table'
) }}

WITH ranked_machine AS (

    SELECT
        machine_id,
        machine_name,
        location,
        machine_type,
        install_date,
        installation_engineer_name,
        machine_owner_name,
        ingestion_timestamp,

        ROW_NUMBER() OVER (
            PARTITION BY machine_id
            ORDER BY ingestion_timestamp DESC
        ) AS row_num

    FROM {{ ref('stg_machine_master') }}

)

SELECT
    machine_id,
    machine_name,
    location,
    machine_type,
    install_date,
    installation_engineer_name,
    machine_owner_name,
    ingestion_timestamp

FROM ranked_machine

WHERE row_num = 1