# DecodeLabs Artificial Intelligence - Project 3
## AI Recommendation Logic

### Goal
Create a simple recommendation system based on user preferences.

### Requirements covered
- Take user input (choices or interests)
- Match preferences using simple similarity/matching logic
- Display recommended items
- Demonstrate logic building and pattern matching

### Technology
- Python 3
- No external libraries are required.

### How to run
1. Open this folder in VS Code or a terminal.
2. Make sure Python is installed.
3. Run:

```bash
python recommendation_system.py
```

4. Enter interests separated by commas, for example:

```text
python, ai, data
```

5. The program calculates a simple match score and displays the best matching recommendations.

### Example
Input:
`python, ai, data`

Possible recommendations:
- Machine Learning Basics
- Artificial Intelligence
- Data Science
- Python Programming

### Algorithm
The program compares the user's preferences with the tags and category of every item. Each matching preference increases the recommendation score. Items with the highest scores are shown first.

### Project title
**Project 3: AI Recommendation Logic**

This implementation follows the Project 3 brief provided by DecodeLabs.
