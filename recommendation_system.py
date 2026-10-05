# DecodeLabs - Artificial Intelligence Project 3
# AI Recommendation Logic
# Simple content-based recommendation using preference matching.

ITEMS = [
    {"name": "Python Programming", "category": "Programming", "tags": ["python", "coding", "programming", "software"]},
    {"name": "Machine Learning Basics", "category": "AI", "tags": ["ai", "machine learning", "python", "data"]},
    {"name": "Artificial Intelligence", "category": "AI", "tags": ["ai", "artificial intelligence", "machine learning", "robotics"]},
    {"name": "Web Development", "category": "Web", "tags": ["html", "css", "javascript", "web", "coding"]},
    {"name": "Data Science", "category": "Data", "tags": ["data", "python", "statistics", "machine learning"]},
    {"name": "Cyber Security", "category": "Security", "tags": ["security", "cyber", "network", "privacy"]},
    {"name": "Cloud Computing", "category": "Cloud", "tags": ["cloud", "aws", "azure", "technology"]},
    {"name": "Mobile App Development", "category": "Mobile", "tags": ["android", "mobile", "java", "kotlin", "coding"]},
    {"name": "Robotics", "category": "Robotics", "tags": ["robotics", "ai", "automation", "technology"]},
    {"name": "Database Management", "category": "Database", "tags": ["database", "sql", "data", "programming"]},
]

def recommendation_score(preferences, item):
    """Count how many user preferences match the item's tags/category."""
    preferences = {p.strip().lower() for p in preferences if p.strip()}
    tags = {tag.lower() for tag in item["tags"]}
    score = len(preferences & tags)
    if item["category"].lower() in preferences:
        score += 1
    return score

def recommend(preferences, top_n=5):
    scored = []
    for item in ITEMS:
        score = recommendation_score(preferences, item)
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [(item, score) for score, item in scored if score > 0][:top_n]

def main():
    print("=" * 55)
    print("      AI RECOMMENDATION LOGIC - PROJECT 3")
    print("=" * 55)
    print("Enter your interests separated by commas.")
    print("Example: python, ai, data")
    user_input = input("\nYour interests: ")
    preferences = user_input.split(",")

    results = recommend(preferences)

    print("\nRecommended Items:")
    print("-" * 55)

    if not results:
        print("No exact matches found.")
        print("Try interests such as: python, ai, data, web, security")
        return

    for position, (item, score) in enumerate(results, start=1):
        print(f"{position}. {item['name']} | Category: {item['category']} | Match Score: {score}")

    print("\nRecommendation completed using preference matching.")

if __name__ == "__main__":
    main()
