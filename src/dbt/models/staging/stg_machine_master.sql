WITH source_data AS (

    SELECT
        machine_id,
        machine_name,
        location,
        machine_type,
        install_date,
        installation_engineer_name,
        machine_owner_name,
        ingestion_timestamp

    FROM {{ source('bronze', 'bronze_machine_master') }}

)

SELECT
    TRIM(machine_id) AS machine_id,
    TRIM(machine_name) AS machine_name,
    TRIM(location) AS location,
    TRIM(machine_type) AS machine_type,
    install_date,
    TRIM(installation_engineer_name) AS installation_engineer_name,
    TRIM(machine_owner_name) AS machine_owner_name,
    ingestion_timestamp

FROM source_data