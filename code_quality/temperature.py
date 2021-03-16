from typing import List


def daily_average(temperatures: List[float]) -> float:
    return sum(temperatures) / len(temperatures)


average_temperature = daily_average([22.8, 19.6, 25.9])
print(average_temperature)
print(daily_average.__annotations__)


# def sum_xy(x: 'an integer', y: 'another integer') -> int:
#     return x + ypydant
#
#
# print(sum_xy.__annotations__)
# {'x': 'an integer', 'y': 'another integer', 'return': <class 'int'}


# from typing import Dict, Tuple
#
#
# def generate_map(points: Tuple[float, float]) -> Dict[str, int]:
#     return map(points)


from typing import Union


def sum_ab(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b
