########################################
#  SQL Queries for the report
########################################

RIDER_SHIFT_QUERY = """ SELECT shift.id AS ID ,DATE_FORMAT(shift.start_at , '%Y-%m-%d') ,
                    DATE_FORMAT(shift.start_at ,'%H:%i:%s') , DATE_FORMAT(shift.close_at , '%Y-%m-%d') ,
                    DATE_FORMAT(shift.close_at ,'%H:%i:%s') ,h.area_name AS HOT_SPOT,c.name AS city ,shift.riders_required AS RIDER_REQUIRED FROM
                    (shift
                     INNER JOIN  hotspot h
                     ON shift.hotspot_id = h.id)
                     LEFT JOIN city c ON h.city_id = c.id where shift.start_at< '{}' and shift.close_at>'{}'"""

