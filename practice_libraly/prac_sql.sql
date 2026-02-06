SELECT
    user_id, 
    COUNT(*)  -- SUM, AVG, COUNT, MAX, MIN
FROM
    access_logs
WHERE
    page_url != '/'  -- (例: 2025年のデータだけ、など)
GROUP BY
    user_id             -- (例: 商品カテゴリごとにまとめる)
HAVING
    COUNT(*) >= 5  -- (例: 合計が1万円以上、など)
ORDER BY
    COUNT(*) DESC;