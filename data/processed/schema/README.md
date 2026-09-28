# Processed data schemas

Store version-controlled schemas and data dictionaries for derived, analysis-ready datasets in this directory. Keep each schema synchronized with the processing code that produces the dataset.

For each derived dataset, document as applicable:

- file or table name
- source dataset or transformation
- row grain
- column names and descriptions
- data types, formats, and units
- nullability, uniqueness, and keys
- validation rules and important assumptions

Do not include real records, personal or confidential identifiers, secrets, access details, or sensitive sample values. Use clearly synthetic examples only when a format cannot be explained without one.

Use an appropriate text-based format such as Markdown, YAML, JSON Schema, SQL DDL, or a tool-specific schema format.
