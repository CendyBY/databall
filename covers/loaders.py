import re
from functools import partial

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


def get_score(score, group):
    match = re.search(r'(\d+)-(\d+)', score)
    return match.group(group)


class GameLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    home_in = MapCompose(lambda x: '@' not in x)
    opponent_in = MapCompose(lambda x: x.replace('@', ''), str.strip)
    result_in = MapCompose(str.strip, str.split)
    score_in = MapCompose(partial(get_score, group=1), int)
    opponent_score_in = MapCompose(partial(get_score, group=2), int)
    spread_in = MapCompose(str.strip, lambda x: 0 if x == 'PK' else x, float)
    over_under_in = MapCompose(str.strip, float)


class TeamLoader(ItemLoader):
    default_output_processor = TakeFirst()
