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
    {}
)
(:goal
    (and
        (integrity_check)
    )
)
(:constraints
(and 
    (preference p1 {})            
    (preference p2 {}) 
)
)
(:metric minimize  (+ (* 1.6 (is-violated p1)) 0)
                   (+ (* 1.6 (is-violated p2)) 0)
)
)
