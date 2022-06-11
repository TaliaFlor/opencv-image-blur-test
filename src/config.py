from numpy import ndarray

from filter_strategy import FilterType


class Config:

    def __init__(self, default_config: list, default_filters: list[FilterType]) -> None:
        self.default_config = default_config
        self.default_filters = default_filters

    def load_args(self, argv: list[str]) -> list[str]:
        for i, arg in enumerate(argv):
            if i == 1:  # filter
                filter_result = self.__search_filters(arg)
                if len(filter_result) == 0:
                    raise Exception('Filter strategy does not exists!')
                else:
                    self.default_config[i] = filter_result[0]
            elif i == 2:  # delay
                self.default_config[i] = int(arg)
            else:
                self.default_config[i] = arg

        return self.default_config

    def __search_filters(self, alias: str) -> list[FilterType]:
        return list(filter(lambda f: f.get('alias') == alias, self.default_filters))

    def ask_to_display_config_questions(self) -> bool:
        while True:
            answer = input(f'Do you wish to configure the application [y/N]?: ').strip().lower()
            if not answer:
                return False

            answer_char = answer[0]
            if answer_char != 'y' and answer_char != 'n':
                print('Please, choose [Y]es or [N]o')
            else:
                return True if answer_char == 'y' else False

    def ask_config_questions(self, default_image: ndarray, default_filter: FilterType, default_blur_delay: int) \
            -> list:
        self.__show_default_values(default_image, default_filter, default_blur_delay)

        filename = self.__get_image(default_image)
        filter_type = self.__get_filter_type(default_filter)
        blur_delay = self.__get_blur_delay(default_blur_delay)

        return [filename, filter_type, blur_delay]

    def __show_default_values(self, default_image: ndarray, default_filter: FilterType,
                              default_blur_delay: int) -> None:
        print('\n------------------------------------')
        print(f'Press [ENTER] in any of the options to use the default value')
        print(f'Image: {default_image}')
        print(f"Filter strategy: {default_filter.get('alias')}")
        print(f'Blur delay: {default_blur_delay} ms')
        print('------------------------------------\n')

    def __get_image(self, default_image: ndarray) -> str:
        filename = input(f"Image: ").strip()
        if not filename:
            return default_image
        return filename

    def __get_filter_type(self, default_filter: FilterType) -> FilterType:
        options = ', '.join([f.get('alias') for f in self.default_filters])
        while True:
            strategy_name = input(f"Filter strategy ({options}): ").strip()
            if not strategy_name:
                return default_filter

            result = self.__search_filters(strategy_name)
            if (len(result)) == 0:
                print('Please, choose a valid strategy')
            else:
                return result[0]

    def __get_blur_delay(self, default_blur_delay: int) -> int:
        while True:
            try:
                answer = input(f'Blur delay in ms (or 0 to disable): ').strip()
                if not answer:
                    return default_blur_delay
                return int(answer)
            except ValueError:
                print('Please, choose a valid value')
