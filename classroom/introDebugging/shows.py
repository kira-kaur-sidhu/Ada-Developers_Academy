# Favorite Shows
recommendations = []

while True:
    show = input("What show should I watch? (press enter to exit) ")
    if not show:
        break
    recommendations.append(show)

print(f"Here are the shows I need to watch: {', '.join(recommendations)}")