(define (problem endemic_1)
(:domain endemic)
(:objects
    delhi - city
    mumbai - city
    london - city
    arizona - city
    johannesburg - city
    atlanta - city
    player1 - player
    player2 - player
    player3 - player
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
    (preference p1 {} ) 
)
)
(:metric minimize (+ (* 1.6 (is-violated p1)) 0))
)
