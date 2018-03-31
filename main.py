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
              "STUDENT/PROFESSIONAL": 7,
              "INSTITUTION": 8,
              "TEAM LIST": 9,
              "CODECHEF CURRENT RATING": 10,
              "HACKERRANK CURRENT RATING": 11,
              "CODEFORCES CURRENT RATING": 12}

loc = 1
print("="*5, "-"*5, " You can search for ", "-"*5, "="*5)
a = 1
for i in vocabulary:
    print(a, ".", i)
    a += 1

while True:
    print("="*10, "#"*15, "="*10)
    n = input("Enter your choice = ").upper()
    if len(n)>1:
        for word in vocabulary:
            if word in n:
                n = vocabulary[word]
                break

    if n == "EXIT":
        break
    else:
        n = int(n)
        print(dic[n])
