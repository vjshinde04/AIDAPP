"""
You have to save your beloved from the clutches of an evil chimpanzee.
The chimpanzee has N monkeys in his army and you need to find a way to fight your way through his army.
The monkeys are arranged in a single file (pun intended). Each monkey has a number assigned to it, which represents the amount of damage it can suffer before you defeat it in the battle. You have to then fight the monkey immediately next in line (again pun intended).

You begins with a Health = 2000 and Injuries = 1 and the maximum Injuries that you can sustain is 1000000.

Lets say you fight a monkey who can deal 'D' damage. Then your health decreases by D and your total injuries get multiplied by D.

You can initially strategically position yourself anywhere in the line. You need to find the maximum number of monkeys that you can defeat. You assume that after this feat of great skill, the evil chimp will return your beloved safe and sound.

We reiterate that you don't need to necessarily reach the evil chimpanzee to win. Nor, do you have to defeat all the monkeys. You just need to defeat the maximum possible, starting anywhere.

Oh and also, we need you to be alive after your battle!

 Hint: You are alive only if your Health > 0 AND Injuries < MAX Injuries

Assume:
Once beaten, the monkeys do not return to battle.
The monkeys cannot turn back and hence those behind you cannot fight.
You can choose to start fighting wherever and choose to stop fighting whenever.


Input File --- 'input.txt'
First line contains the total number of elements (monkeys) in the file (army) = N.
N lines follow. Each element in the subsequent Jth line is a positive number (integer) which is equal to the damage that can be dealt by the Jth monkey.

Example (MOCK BATTLE)

FILE:
5
100
50
25
5
100

There are 5 monkeys (First line of the file). Damage that can be dealt by them are 100,50,25,5,100 (in order).
Let us say that your health (ignore injuries for this example) is only 100 (it is 2000 for the real battle). You could start by attacking the 1st monkey, but in doing so you defeat him at the cost of your life.

Hence, you may choose to start from the 2nd monkey and defeat him and the next 2 in line (remember you have to fight them sequentially) and  opt out of the battle before you take on the 5th monkey.

Please make sure that you understand why starting from position 2 (2nd monkey) is the best strategy. It is because you cannot defeat more than 3 by starting elsewhere.

Please go through the file (which you have downloaded) to understand it better.

Please read the questions that follow and solve them so that you can save your beloved!

What is the maximum number of monkeys that can be defeated by you?
20 points
Is there only one such position where the previous count of defeated monkeys can be achieved? If no, what is the total number of such positions? If yes, please input 1.
20 points
"""

with open("input.txt") as f:
    line = f.readlines()

noMonkeys = line[0]
#print(noMonkeys)

monkeyPower = []
for i in range(1,int(noMonkeys)+1):
    monkeyPower.append(int(line[i]))
#print(len(monkeyPower))
#print(monkeyPower[-3],monkeyPower[-2],monkeyPower[-1])

hIcombo = {}
for i in range(0, (len(monkeyPower)-1)):
    j = i
    monkeyCount = 0
    healthDamage = 0
    injury = 1
    while 1:
        healthDamage += monkeyPower[j]
        injury = injury * monkeyPower[j]
        if healthDamage < 2000 and injury < 1000000:
            monkeyCount += 1
        j += 1
        if healthDamage > 2000 or injury > 1000000 or j == len(monkeyPower):
            hIcombo[i] = monkeyCount
            break

print(max(hIcombo.values()))

#print(hIcombo)

c = 0
for i in hIcombo.values():
    if i == 19:
        c += 1
print(c)