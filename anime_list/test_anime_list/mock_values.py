mock_season = {
    1: {
        "season": 1,
        "airing": False,
        "time_of_year": "WIN",
        "year": 2020,
        "name_of_season": "mock_season",
        "episode_count": 23,
    },
    2: {
        "season": 2,
        "airing": True,
        "time_of_year": "WIN",
        "year": 2021,
        "name_of_season": "mock_season",
        "episode_count": 23,
    },
}


def get_mock_season(no: int, anime):
    """Return anime season with anime set"""
    mock_s = mock_season[no].copy()
    mock_s["anime"] = anime
    return mock_s
