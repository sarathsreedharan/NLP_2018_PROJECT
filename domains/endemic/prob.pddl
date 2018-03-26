(define (problem endemic_1)
(:domain endemic)
(:objects
    delhi - city
    p1 - player
    ebola - disease
)
(:init
  (has_board)
  (= (research_station_count) 0)
  (= (city_disease_count delhi  ebola) 1)
  (= (total_per_city_count delhi) 1)
  (= (total_disease_count) 1)
)
(:goal
    (integrity_check)
)
)
