class Shortner:
    def __init__(self, items):
        self.original_items = items

    def print_original(self):
        print(self.original_items)


class ListAndCharShortner(Shortner):
    def print_shortened(self):
        print(self.original_items[0:3])


class DictionaryShortner(Shortner):
    def print_shortened(self):
        # original_items = {1: 'mike', 2: 'tom', 3: 'rebecca', 4: 'john', 5: 'paul'}
        dict = self.original_items
        counter = 0
        result_dict = {}
        for (k, v) in dict.items():
            if counter < 3:
                result_dict.update({k: v})
                counter += 1
        print(result_dict)


my_shortner = ListAndCharShortner("This is a sentence")
my_shortner2 = ListAndCharShortner([1, 2, 3, 4, 5, 6, 7])
my_shortner.print_shortened()
my_shortner2.print_shortened()

my_shortner3 = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebecca', 4: 'john', 5: 'paul'})
my_shortner3.print_original()
my_shortner3.print_shortened()
