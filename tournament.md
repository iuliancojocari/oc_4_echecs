1. Play tournament -> redirect "run_tournament"

- create players pairs

View:
Generate players pairs done

Players pairs :

1. Player 1 vs Player 2
2. Player 1 vs Player 2
3. Player 1 vs Player 2
4. Player 1 vs Player 2

5. Launch Round 1

H. Homepage
Q. Exit

---

# Option 1 -> redirect "launch round 1"

Round 1 : [
(player1, player2),
(player1, player2),
(player1, player2),
(player1, player2)
]
Round 2 : [
(player1, player2),
(player1, player2),
(player1, player2),
(player1, player2)
]

### Update score

Tournament :

- Name
- Location
- Date
- Description
- Players :
  - Player1
  - Player2
  - Player3
  - Player4
  - Player5
  - Player6
  - Player7
  - Player8
- nb_rounds = 4
- Rounds :
  - Round 1 :
    - Start date
    - End date
    - Match 1 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 2 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 3 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 4 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
  - Round 2 :
    - Start date
    - End date
    - Match 1 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 2 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 3 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 4 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
  - Round 3 :
    - Start date
    - End date
    - Match 1 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 2 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 3 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 4 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
  - Round 4 :
    - Start date
    - End date
    - Match 1 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 2 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 3 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]
    - Match 4 :
      - Players pairs -> tuple (player1, player2)
      - Score -> list [0,1]

---

Tournament :

- Name
- Location
- Date
- Description
- Players
- Nb_rounds
- Rounds

Round :

- Name
- Matchs
- Start date
- End date

Match :

- Name
- Players pairs
- Score

---

play tournament

- créer le round
- créer les matchs
- mettre à jour l'objet tournament
