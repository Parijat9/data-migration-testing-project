# Migration Rules

This document explains how data from System A is converted into System B.

| Source Field | Target Field | Rule |
|---|---|---|
| cust_id | customer_id | Same value |
| full_name | customer_name | Remove extra spaces |
| country_code | country | Convert code to full country name |
| order_dt | order_date | Change date format |
| qty | quantity | Same value |
| amt | sales_amount | Round to 2 decimal places |

## Example
- IN becomes India
- US becomes United States
- 12-01-2023 becomes 2023-01-12
