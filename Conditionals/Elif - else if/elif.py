# NOTE: 'elif' keyword checks this condition if previous conditions were found to be 'not true':

x = 509
y = 505
if y > x:
    print("Y is greater than x")
elif x > y:
    print("X is actually greater than y")
