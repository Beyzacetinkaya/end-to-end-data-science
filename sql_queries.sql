-- Retention by country
SELECT country, COUNT(*) FROM user_data GROUP BY country;