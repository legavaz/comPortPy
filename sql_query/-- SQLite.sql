-- SQLite
select 
     julianday('now'),    
     julianday(DateTime),
     (julianday(DateTime) - julianday('now')),
     DateTime
     


 from staffWork;