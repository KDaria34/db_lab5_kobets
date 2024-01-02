select * from title;
create table titlecopy as select * from title; 
delete from titlecopy;
select * from titlecopy;

DO $$
 DECLARE
     film_name   		titlecopy.name%TYPE;
     film_title_type 	titlecopy.title_type%TYPE;
	 film_release_year	titlecopy.release_year%TYPE;

 BEGIN
     film_name := 'Name';
	 film_title_type := 'type';
	 film_release_year := 'year';
     FOR counter IN 0..9
         LOOP
            INSERT INTO titlecopy (name, title_type, release_year)
             VALUES (film_name || counter, film_title_type || counter, film_release_year || counter);
         END LOOP;
 END;
 $$
