(define (domain endemic)

    (:requirements
        :durative-actions
        :equality
        :negative-preconditions
        :numeric-fluents
        :object-fluents
        :typing
        :preferences
    )

    (:types
        city player disease - objects
    )

    (:constants

    )

    (:predicates
    (has_Role_Cards)
    (has_Pawns)
    (has_Player_cards)
    (has_Reference_Cards)
    (has_Infection_cards)
    (has_disease_cubes)
    (has_cure_markers)
    (has_outbreak_marker)
    (has_research_station_cards)
    (has_board)
    (integrity_check)
    
    (in_city ?p - player ?c - city)
    (has_city_card ?p - player ?c - city)
    (has_research_station ?c - city)
    (connected ?c1 - city ?c2 - city)
    (is_cured ?d - disease)
    (cured_disease_began ?c - city ?d - disease)
    (game_finished)
    (dummy)
    )

    (:functions
      (research_station_count)
      (city_disease_count ?c - city ?d - disease)
      (total_per_city_count ?c - city)
      (total_disease_count)
    )

    (:action validate_pieces
        :parameters ()
        :precondition (and (has_board))
        :effect (and (integrity_check))
    )
;new_act    
    (:action game_over_check
        :parameters ()
        :precondition (and (=  (total_disease_count) 0)) 
        :effect (and (game_finished))
    )
;new_act        
    (:action drive
        :parameters (?p - player ?c1 - city ?c2 - city)
        :precondition (and (in_city ?p ?c1) (connected ?c1 ?c2)) 
        :effect (and (not (in_city ?p ?c1)) (in_city ?p ?c2))
    )
;new_act    
    (:action fly_directly
        :parameters (?p - player ?c1 - city ?c2 - city)
        :precondition (and (in_city ?p ?c1) (has_city_card ?p ?c2)) 
        :effect (and (not (in_city ?p ?c1)) (not (has_city_card ?p ?c2)) (in_city ?p ?c2))
    )   
;new_act    
   (:action fly_by_charter
       :parameters (?p - player ?c1 - city ?c2 - city)
       :precondition (and (in_city ?p ?c1) (has_city_card ?p ?c1)) 
       :effect (and (not (in_city ?p ?c1)) (not (has_city_card ?p ?c1)) (in_city ?p ?c2))
   )   
;new_act    

    (:action fly_by_shuttle
        :parameters (?p - player ?c1 - city ?c2 - city)
        :precondition (and (in_city ?p ?c1) (has_research_station ?c1) (has_research_station ?c2)) 
        :effect (and (not (in_city ?p ?c1))  (in_city ?p ?c2))
    )   
;new_act    
   
    (:action build_research_station_new
        :parameters (?p - player ?c1 - city)
        :precondition (and (in_city ?p ?c1) (< (research_station_count) 6) ) 
        :effect (and (has_research_station ?c1) (increase (research_station_count) 1))
    )   
;new_act    
    (:action move_research_station
        :parameters (?p - player ?c1 - city ?c2 - city)
        :precondition (and (in_city ?p ?c1) (has_research_station ?c2) ) 
        :effect (and (has_research_station ?c1) (not (has_research_station ?c2)))
    )
;new_act    
    
    (:action treat_disease
        :parameters (?p - player ?c - city ?d - disease)
        :precondition (and (in_city ?p ?c) (> (city_disease_count ?c ?d) 0) ) 
        :effect (and (decrease (total_per_city_count ?c) 1) (decrease (total_disease_count) 1) (decrease (total_per_city_count ?c) 1))
    )
;new_act    


    (:action treat_cured_disease
        :parameters (?p - player ?c - city ?d - disease)
        :precondition (and (in_city ?p ?c) (cured_disease_began ?c ?d)) 
        :effect (and (not (cured_disease_began ?c ?d)) (assign (city_disease_count ?c ?d) 0))
    )
;new_act    

    (:action share_knowledge
        :parameters (?p1 - player ?p2 - player ?c1 - city)
        :precondition (and (in_city ?p1 ?c1) (in_city ?p2 ?c1) (has_city_card ?p1 ?c1)) 
        :effect (and (not (has_city_card ?p1 ?c1)) (has_city_card ?p2 ?c1))
    )
;new_act    

    (:action cure_disease
        :parameters (?p1 - player ?c1 - city ?c2 - city ?c3 - city ?c4 - city ?d - disease)
        :precondition (and (in_city ?p1 ?c1) (has_research_station ?c1) (has_city_card ?p1 ?c2) (has_city_card ?p1 ?c3) (has_city_card ?p1 ?c4) (not (= ?c2 ?c3)) (not (= ?c3 ?c4)) (not (= ?c3 ?c4))) 
        :effect (and (not (has_city_card ?p1 ?c2)) (not (has_city_card ?p1 ?c3)) (not (has_city_card ?p1 ?c4)) (is_cured ?d))
    )
;new_act

)

