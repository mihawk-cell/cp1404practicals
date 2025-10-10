"""Never name a file the same as a module; e.g., random.py or it will have higher precedence when you import it."""
"""
1. What did you see on line 1? 
20
What was the smallest number you could have seen, what was the largest?
5-20

2. What did you see on line 2?
7
What was the smallest number you could have seen, what was the largest?
min = 3, max = 9
Could line 2 have produced a 4?
No

3. What did you see on line 3? 
4.641566499465415
What was the smallest number you could have seen, what was the largest?
float between 2.5 - 5.5
"""

"""
4. Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

import random
print(random.randint(1, 100))
