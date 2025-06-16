WITH ranked AS (
    SELECT 
        player_id, 
        event_date,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
    FROM activity
),
first_second_login AS (
    SELECT 
        r1.player_id,
        r1.event_date AS first_login,
        r2.event_date AS second_login
    FROM ranked r1
    JOIN ranked r2 
      ON r1.player_id = r2.player_id 
     AND r1.rn = 1 
     AND r2.rn = 2
)
SELECT 
    ROUND(
        COUNT(IF(DATEDIFF(f.second_login, f.first_login) = 1, 1, NULL)) / 
        (SELECT COUNT(DISTINCT player_id) FROM activity),
    2
    ) AS fraction
FROM first_second_login f;
