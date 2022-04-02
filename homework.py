from dataclasses import asdict, dataclass
from typing import ClassVar, Dict, List, Type, Union

TIKKER_SWIM: str = 'SWM'
TIKKER_RUN: str = 'RUN'
TIKKER_WALK: str = 'WLK'
TYPES_LIST: List[str] = [TIKKER_SWIM, TIKKER_RUN, TIKKER_WALK]


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    MESSAGE_CONST: ClassVar[str] = ('Тип тренировки: {training_type}; '
                                    'Длительность: {duration:.3f} ч.; '
                                    'Дистанция: {distance:.3f} км; '
                                    'Ср. скорость: {speed:.3f} км/ч; '
                                    'Потрачено ккал: {calories:.3f}.')

    def get_message(self):
        """Метод, выводящий сообщение о тренировке."""
        temp_dict: Dict[str, Union[float, str]] = asdict(self)
        return self.MESSAGE_CONST.format(**temp_dict)


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[float] = 1000
    MIN_IN_HOUR: ClassVar[float] = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(f'Method of class {type(self).__name__} '
                                  'is not redefined.')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories(),
                           )


class Running(Training):
    """Тренировка: бег."""

    RUN_COEF_1: ClassVar[float] = 18
    RUN_COEF_2: ClassVar[float] = 20

    def get_spent_calories(self) -> float:
        return ((self.RUN_COEF_1 * self.get_mean_speed() - self.RUN_COEF_2)
                * self.weight / self.M_IN_KM * self.duration
                * self.MIN_IN_HOUR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    WALK_COEF_1: ClassVar[float] = 0.035
    WALK_COEF_2: ClassVar[float] = 0.029
    WALK_DEGREE: ClassVar[float] = 2.0

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.WALK_COEF_1 * self.weight + (self.get_mean_speed()
                ** self.WALK_DEGREE // self.height) * self.WALK_COEF_2
                * self.weight) * self.duration * self.MIN_IN_HOUR)


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    SWIM_COEF_1: ClassVar[float] = 1.1
    SWOM_COEF_2: ClassVar[float] = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int,
                 ) -> None:
        super().__init__(action, duration, weight)

        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.SWIM_COEF_1) * self.SWOM_COEF_2
                * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    package: Dict[str, Type[Training]] = {
        TIKKER_SWIM: Swimming,
        TIKKER_RUN: Running,
        TIKKER_WALK: SportsWalking,
    }
    if workout_type in TYPES_LIST:
        return package[workout_type](*data)
    else:
        raise ValueError(f'You have entered {workout_type} as workout_type, '
                         f'should be something from this list: {TYPES_LIST}')


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        (TIKKER_SWIM, [720, 1, 80, 25, 40]),
        (TIKKER_RUN, [15000, 1, 75]),
        (TIKKER_WALK, [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
