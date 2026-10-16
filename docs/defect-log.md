# Issues to check

These are examples to investigate when testing a transfer, not a record of confirmed production defects.

| Possible issue | Check |
|---|---|
| Wrong country name | Compare the source country code with the target name |
| Wrong amount | Compare the source amount rounded to two decimal places |
| Repeated order | Check for duplicate order IDs |

The current tests cover duplicate order IDs. Full source-to-target checks for the other two cases still need to be added.
