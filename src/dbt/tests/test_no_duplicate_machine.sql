SELECT
    machine_id,
    COUNT(*) AS record_count

FROM {{ ref('dim_machine') }}

GROUP BY machine_id

HAVING COUNT(*) > 1