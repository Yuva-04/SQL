# Write your MySQL query statement below
select query_name,round(avg(rating/position),2) as quality, round(avg(if(rating < 3 , 1 ,0)*100),2) as poor_query_percentage
from Queries
where query_name is not null #incase null value is given
group by query_name