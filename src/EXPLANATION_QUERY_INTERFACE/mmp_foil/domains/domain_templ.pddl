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

    {}
)

