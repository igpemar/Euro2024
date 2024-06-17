class Counter:
    def __init__(self, name: str):
        self.name = name
        self.count = {}
        self.total = 0
        self.country_count = {}

    def add(self, match):
        self.count[match] = self.count.get(match, 0) + 1
        self.total += 1

    def add_country_count(self, match):
        home = match.split("-")[0]
        away = match.split("-")[1]
        self.country_count[home] = self.country_count.get(home, 0) + 1
        self.country_count[away] = self.country_count.get(away, 0) + 1

    def sort(self):
        self.count = dict(sorted(self.count.items(), key=lambda x: x[1], reverse=True))

    def get_sorted(self):
        return dict(sorted(self.count.items(), key=lambda x: x[1], reverse=True))

    def append(self, counter):
        for key, value in counter.count.items():
            if key in self.count:
                self.count[key] += value  # If the key exists, add the values
            else:
                self.count[key] = (
                    value  # If the key doesn't exist, add the key-value pair
                )
            self.total += value
