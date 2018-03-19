Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> basketball_term = {
    "Crossover": "A basketball move wither you go left or right from one hand to the other.",
    "Rebound": "To get the ball from a missed shot weither if it is offinsive or defencive",
    "3 Pointer": "A shot from 20 ft or farther if the shot is made",
    "Free Throw": "2-3 free shots from the freethrow line if fouled",
    "Put-Back": "A shot that was missed but was put back in to the basket for 2 points",
    "Lay-Up": "A shot that is layed up into the basket for 2 points"
    }
for k, v in basketball_term.items():
    print k, v
