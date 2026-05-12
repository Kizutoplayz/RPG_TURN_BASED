def p_stat():               #player stats
    hea = 10
    atk = 3
    defd = 1
    return hea, atk, defd

def e_stat():               #enemy stats
    e_hea = 15
    e_atk = 2
    return e_hea, e_atk

def game_loop():            #main loop
    e_h, e_a = e_stat()
    p_h, p_a, p_d = p_stat()
    while(p_h >= 0):
        print(f"Enemy Health: {e_h}")
        print(f"Player Health: {p_h}")
        c = input("\nPress [A] for Attack or [D] for Defend.\n")          #turns
        if c == "A" or "a":
            print("You attacked!\n")
            e_h = e_h - p_a
            print("Enemy attacked you back!")
            p_h = p_h - e_a
        else:
            print("You Defended.")
            p_h = p_h - (e_a - p_d)


if __name__ == "__main__":
    game_loop()