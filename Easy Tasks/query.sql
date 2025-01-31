with daily_users as (
    select date(timestamp) as day, user_id
    from default.churn_submits
    group by date(timestamp), user_id
)
select
    day,
    count(distinct user_id) over (order by day rows between 6 preceding and current row) as wau
from daily_users
order by day;
