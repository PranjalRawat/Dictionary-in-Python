dic = {1: " mohit_negi (3★)",
       2: "IDK! I have to sit in a cave for 30 years to actually know who i am! xP",
       3: "IN  India",
       4: "Uttarakhand",
       5: "Pauri",
       6: "sit down, be humble!",
       7: "Student",
       8: "IHMS Kotdwar",
       9: "None",
       10: "1611(+21) [Highest]",
       11: "1483.17",
       12: "unranked"}

vocabulary = {"USERNAME": 1,
              "ABOUT ME": 2,
              "COUNTRY": 3,
              "STATE": 4,
              "CITY": 5,
              "MOTTO": 6,
              "PROFESSION": 7,
              "INSTITUTION": 8,
              "TEAM LIST": 9,
              "CODECHEF CURRENT RATING": 10,
              "HACKERRANK CURRENT RATING": 11,
              "CODEFORCES CURRENT RATING": 12}


print("="*5, "-"*5, " You can search for ", "-"*5, "="*5)
index = 1
for element in vocabulary:
    print(index, ".", element)
    index += 1

while True:
    print("="*10, "#"*15, "="*10)
    search = input("Enter your choice = ").upper()
    if len(search) > 2:

        for word in vocabulary:
            if word in search:
                search = vocabulary[word]
                key = word
                break

        else:
            print("Wrong Input!!!")
            print("Re-run the program !!!")
            exit()
    else:
        for id in vocabulary:
            if vocabulary[id] == int(search):
                key = id

    if search == "EXIT":
        break
    else:
        search = int(search)
        if search > 12:
            print("Wrong Input!!!")
            print("Re-run the program !!!")
            exit()
        else:
            print(key, "=", dic[search])
