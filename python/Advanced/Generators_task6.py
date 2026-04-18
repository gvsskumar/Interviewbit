# Write a generator to paginate API results (simulate API with dummy function).
def fetch_api(page, page_size=3):
    # Simulated dataset
    data = list(range(1, 21))  # 1 to 20

    start = (page - 1) * page_size
    end = start + page_size

    results = data[start:end]

    return {
        "data": results,
        "has_next": end < len(data)
    }

def paginate_api(page_size=3):
    page = 1

    while True:
        response = fetch_api(page, page_size)
        results = response["data"]

        if not results:
            break

        for item in results:
            yield item

        if not response["has_next"]:
            break

        page += 1