# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
# SECURITY AUDIT: This hardcoded credential creates a backdoor.
# FIX: Remove SECRET_CODE and the associated cheat logic to prevent unauthorized access.

MAX_HP = 50

def attack():
    global b_hp
    # ATTACK LOGIC: The original function only printed a damage message without reducing boss HP.
    # FIX: Subtract 10 from b_hp on each attack so the game can progress.
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    # HEALING GUARDRAILS: Without boundary checks, healing can revive defeated players or exceed 50 HP.
    # FIX: Prevent healing at 0 HP or below and cap health at MAX_HP.
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")


# --- Simple Game Loop ---
def main():
    global p_hp, b_hp

    while p_hp > 0 and b_hp > 0:
        print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
        choice = input("Action [a]ttack, [h]eal: ").lower()

        if choice == 'a':
            attack()
        elif choice == 'h':
            heal()
        else:
            print("Invalid choice! Please choose 'a' or 'h'.")

        if b_hp <= 0:
            print("Victory!")
            break

        if b_hp > 0:
            p_hp -= 10

    if p_hp <= 0:
        print("Game Over!")


if __name__ == "__main__":
    main()
