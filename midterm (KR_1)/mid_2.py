import unittest

def process_scores(scores: list[tuple[str, int]]) -> dict[str, int]:
    if not scores:
        return {}

    for name, score in scores:
        if score < 0:
            raise ValueError(f'Negative value for {name}: {score}')

    total_score = sum(score for _, score in scores)
    average_score = total_score / len(scores)

    filtered_scores = {}

    for name, score in scores:
        if score > average_score:
            filtered_scores[name] = score

    sorted_scores = sorted(filtered_scores.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_scores)

scores = [
    ('Alice', 85),
    ('Bob', 75),
    ('Charlie', 39),
    ('David', 62),
    ('Eve', 91)
]

print(process_scores(scores))

class TestProcessScores(unittest.TestCase):
    def test_above_average(self):
        scores = [('Alice', 95), ('Carl', 85), ('Bob', 60), ('Charlie', 39), ('David', 52),]
        expected = {'Alice': 95, 'Carl': 85}
        self.assertEqual(process_scores(scores), expected)

    def test_all_average(self):
        scores = [('Alice', 40), ('Bob', 40), ('Charlie', 40)]
        expected = {}
        self.assertEqual(process_scores(scores), expected)

    def test_empty_list(self):
        scores = []
        expected = {}
        self.assertEqual(process_scores(scores), expected)

    def test_single_student(self):
        scores = [('Alice', 100)]
        expected = {}
        self.assertEqual(process_scores(scores), expected)

    def test_tie_scores(self):
        scores = [('Alice', 90), ('Bob', 90), ('Charlie', 90), ('Dave', 80)]
        expected = {'Alice': 90, 'Bob': 90, 'Charlie': 90}
        self.assertEqual(process_scores(scores), expected)

    def test_negative_score(self):
        scores = [('Alice', 85), ('Bob', -75), ('Charlie', 39)]
        with self.assertRaises(ValueError):
            process_scores(scores)

if __name__ == '__main__':
    unittest.main()