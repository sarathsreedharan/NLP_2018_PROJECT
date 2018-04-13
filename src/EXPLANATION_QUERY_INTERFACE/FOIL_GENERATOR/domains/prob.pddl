(define (problem endemic_1)
(:domain endemic)
(:objects
    delhi - city
    bombay - city
    london - city
    phoenix - city
    p1 - player
    p2 - player
    ebola - disease
)
(:init
  (has_board)
  (= (research_station_count) 0)
  (= (city_disease_count delhi  ebola) 1)
  (= (total_per_city_count delhi) 1)
  (= (total_disease_count) 1)
  (in_city p1 london)
  (has_city_card p1 delhi)
  (in_city p2  delhi)
)
(:goal
    (and
        (integrity_check)
    )
)
(:constraints
(and 
    (preference p1 (at end (has_city_card p1 delhi)) )
)
)
(:metric minimize (+ (* 1.6 (is-violated p1)) 0))
)
