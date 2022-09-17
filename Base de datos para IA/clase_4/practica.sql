--•	Cual son los 10 invoice mas grandes en la base

select
	*
from
	invoice i
order by
	i.total asc
limit 10;

--•	Quien es el empleado con más customers asociado

select
	e.first_name,
	e.last_name,
	count(concat(e.first_name, e.last_name)) customers
from
	employee e
inner join customer c on
	e.employee_id = c.support_rep_id
group by
	e.first_name,
	e.last_name
order by
	count(concat(e.first_name, e.last_name)) desc
limit 1;

Select e.employee_id, count(c.support_rep_id) as custom_count 
from 
	employee e 
	inner join customer c on e.employee_id = c.support_rep_id 
group by 
	e.employee_id
order by custom_count desc limit 1;

--•	armar una query que nos diga quienes son los 10 artistas con más canciones y cuantas canciones tiene cada uno.

with aux_table as (
	select a.artist_id, a."name" , al.album_id, t.track_id
	from 
		artist a 
		inner join album al on a.artist_id = al.artist_id
		inner join track t on t.album_id = al.album_id 
)
select 
	t."name",
	count(t.track_id) as "track_count"
from 
	aux_table t
group by
	t."name" 
order by track_count desc
limit 10;