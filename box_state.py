class BoxState():
    def __init__(self, numbers: list[int]) -> None:
        self.id = self.get_id(numbers)
        self.numbers = numbers
        self.expectation = None

    @staticmethod
    def get_id(numbers: list[int]) -> str:
        if len(numbers) == 0:
            return ""

        if len(numbers) == 1:
            return str(numbers[0])

        sorted_numbers = sorted(numbers)
        return ",".join(map(str, sorted_numbers))
