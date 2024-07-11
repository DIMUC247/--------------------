def add_review(reviews: list) -> list:
    review = input("Залиште свій відгук:\n")
    reviews.append(review)


def find_repeated_chars(reviews: list) -> None:
    reviews = " ".join(reviews)

    repeated_groups = set()
    for i in range(len(reviews)):
        for j in range(i+1, len(reviews)):
            slice = reviews[i:j]
            if reviews.count(slice) >= 2:
                repeated_groups.add(slice)

    print(f"Список груп символів, які повторюються не менше 2 разів:\n{repeated_groups}")
