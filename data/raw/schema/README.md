# Raw data schemas

Store version-controlled schemas and data dictionaries for original input datasets in this directory. This metadata lets code and notebooks be developed without access to the underlying research data.

For each input dataset, document as applicable:

- file or table name
- column names and descriptions
- data types and formats
- units and allowed values
- nullability and uniqueness
- primary and foreign keys
- validation rules and important assumptions

Do not include real records, personal or confidential identifiers, secrets, access details, or sensitive sample values. Use clearly synthetic examples only when a format cannot be explained without one.

Use an appropriate text-based format such as Markdown, YAML, JSON Schema, SQL DDL, or a tool-specific schema format.
