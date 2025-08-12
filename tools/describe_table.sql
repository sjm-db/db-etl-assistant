CREATE OR REPLACE FUNCTION etl_assist_test.tools.describe_table(
  cat STRING COMMENT 'Catalog name',
  sch STRING COMMENT 'Schema name',
  tbl STRING COMMENT 'Table name'
)
RETURNS TABLE (
  column_name STRING COMMENT 'Column name',
  data_type STRING COMMENT 'Data type',
  is_nullable STRING COMMENT 'YES or NO',
  comment STRING COMMENT 'Column comment',
  ordinal_position INT COMMENT '1-based position in table'
)
COMMENT 'Returns column metadata like DESCRIBE for a given <catalog>.<schema>.<table>.'
RETURN
SELECT
  c.column_name,
  c.data_type,
  c.is_nullable,
  c.comment,
  c.ordinal_position
FROM system.information_schema.columns AS c
WHERE c.table_catalog = cat
  AND c.table_schema  = sch
  AND c.table_name    = tbl
ORDER BY c.ordinal_position;

