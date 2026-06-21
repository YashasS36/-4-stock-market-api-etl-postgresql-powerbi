-- Total Records
SELECT COUNT(*)
FROM stock_prices;

-- Latest Date
SELECT MAX(trade_date)
FROM stock_prices;

-- Records Per Stock
SELECT
    stock_symbol,
    COUNT(*) AS total_records
FROM stock_prices
GROUP BY stock_symbol
ORDER BY total_records DESC;

-- Highest Closing Price
SELECT
    stock_symbol,
    MAX(close_price) AS highest_close
FROM stock_prices
GROUP BY stock_symbol;

-- Lowest Closing Price
SELECT
    stock_symbol,
    MIN(close_price) AS lowest_close
FROM stock_prices
GROUP BY stock_symbol;

-- Total Volume
SELECT
    stock_symbol,
    SUM(volume) AS total_volume
FROM stock_prices
GROUP BY stock_symbol;