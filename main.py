import json
from datetime import datetime

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_popular(orders):
    categories_count = {}
    for order in orders:
        ordered_at = datetime.strptime(order['ordered_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if ordered_at.month == 12 and ordered_at.day >= 1 and ordered_at.day <= 31:
            for item in order['items']:
                category = item['category']['name']
                categories_count[category] = categories_count.get(category, 0) + 1

    max_count = max(categories_count.values())
    popular_categories = sorted([category for category, count in categories_count.items() if count == max_count])
    return popular_categories


def generate_report(file_path):
    orders = load_json(file_path)
    popular_categories = get_popular(orders)
    report = {'categories': popular_categories}
    return (json.dumps(report, ensure_ascii=False))

print(generate_report('format.json'))
