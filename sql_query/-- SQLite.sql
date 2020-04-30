-- SQLite
-- select 
--      test_id_int as id,
--      DateTime,
--      propusk_id_txt as propusk_id,     
--      CAST((julianday('now') - julianday(DateTime) ) as integer) as days_old     
--  from staffWork 
 
--  WHERE
--      CAST((julianday('now') - julianday(DateTime) ) as integer) >15
--      and export_bl<>0;


SELECT * FROM 'staffWork'
WHERE export_bl=0;