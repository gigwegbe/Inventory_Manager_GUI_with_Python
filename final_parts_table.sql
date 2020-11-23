BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "final_parts_table" (
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
INSERT INTO "final_parts_table" VALUES (1,'W482','Washer',29021,29300,1,204.7,207.4,3);
INSERT INTO "final_parts_table" VALUES (2,'M154','Mount',26600,26800,4,230,232,2);
INSERT INTO "final_parts_table" VALUES (3,'B785','Bolt',3900,4100,1,90.5,92,4);
INSERT INTO "final_parts_table" VALUES (4,'W895','Washer',35000,35100,1,55.2,61.5,7);
INSERT INTO "final_parts_table" VALUES (5,'M184','Mount',17800,18000,6,127,128.5,5);
INSERT INTO "final_parts_table" VALUES (6,'B864','Bolt',4150,5210,1,177.5,178.5,3);
INSERT INTO "final_parts_table" VALUES (7,'W785','Washer',28900,29100,1,195.5,196,8);
INSERT INTO "final_parts_table" VALUES (8,'M785','Mount',27210,27310,5,210,212,15);
INSERT INTO "final_parts_table" VALUES (9,'B777','Bolt',7750,7822,1,95.5,97,11);
INSERT INTO "final_parts_table" VALUES (10,'W425','Washer',34700,35050,1,78,78.8,5);
INSERT INTO "final_parts_table" VALUES (11,'M864','Mount',9800,9900,4,110,110.5,8);
INSERT INTO "final_parts_table" VALUES (12,'B988','Bolt',19500,20200,1,69.7,70.3,20);
COMMIT;
