# Test results

Run `python -m pytest -v` from the repository folder to check the included sample files.

There are six automated checks: row counts, blank customer IDs, repeated order IDs, country names, positive sales amounts and a basic date-format check.

The screenshot in the README records the result of the latest documentation review. It is not a guarantee that another dataset will pass.

## Checks to add

- Match each source order to the corresponding target order.
- Compare quantities and rounded amounts.
- Check trimmed names and country conversions against the source.
- Parse dates rather than only checking for a dash.
- Confirm the complete set of expected columns.
