BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "parts_table" (
	"ID"	INTEGER,
	"Reference"	TEXT,
	"PartName"	TEXT,
	"MinArea"	NUMERIC,
	"MaxArea"	NUMERIC,
	"NumberOfHoles"	INTEGER,
	"MinDiameter"	NUMERIC,
	"MaxDiameter"	NUMERIC,
	"Count"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
COMMIT;
