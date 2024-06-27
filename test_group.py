import pytest
from group import Group
import team


@pytest.fixture
def sample_group_D_5_5_3_2():
    return Group(
        "A",
        [
            ["Denmark", "Belgium", 3, 2, True],
            ["England", "Spain", 1, 1, True],
            ["Denmark", "England", 0, 0, True],
            ["Belgium", "Spain", 1, 2, True],
            ["Denmark", "Spain", 1, 1, True],
            ["Belgium", "England", 2, 0, True],
        ],
    )


@pytest.fixture
def sample_group_4_4_4_4_DG():
    return Group(
        "A",
        [
            ["Denmark", "Belgium", 4, 0, True],
            ["England", "Spain", 0, 5, True],
            ["Denmark", "England", 0, 3, True],
            ["Belgium", "Spain", 3, 0, True],
            ["Denmark", "Spain", 1, 1, True],
            ["Belgium", "England", 1, 1, True],
        ],
    )


@pytest.fixture
def sample_group_4_4_4_4_RF():
    return Group(
        "A",
        [
            ["Denmark", "Belgium", 3, 0, True],
            ["England", "Spain", 0, 3, True],
            ["Denmark", "England", 0, 3, True],
            ["Belgium", "Spain", 3, 0, True],
            ["Denmark", "Spain", 1, 1, True],
            ["Belgium", "England", 1, 1, True],
        ],
    )


@pytest.fixture
def sample_group_6_6_6_0():
    return Group(
        "A",
        [
            ["Denmark", "Belgium", 0, 1, True],
            ["England", "Spain", 0, 1, True],
            ["Denmark", "England", 1, 0, True],
            ["Belgium", "Spain", 0, 1, True],
            ["Denmark", "Spain", 1, 0, True],
            ["Belgium", "England", 1, 0, True],
        ],
    )


@pytest.fixture
def sample_group_9_3_3_3():
    return Group(
        "A",
        [
            ["Denmark", "Belgium", 1, 0, True],
            ["England", "Spain", 0, 1, True],
            ["Denmark", "England", 0, 1, True],
            ["Belgium", "Spain", 0, 1, True],
            ["Denmark", "Spain", 0, 1, True],
            ["Belgium", "England", 1, 0, True],
        ],
    )


def test_calculate_standings_D_5_5_3_2(sample_group_D_5_5_3_2):
    # Expected standings based on the sample group
    expected_standings = [
        {
            "Team.Name": "Spain",
            "Team.PG": 3,
            "Team.GD": 1,
            "Team.GS": 4,
            "Team.GA": 3,
            "Team.W": 1,
            "Team.Points": 5,
            "Team.EQR": team.euro_qualifier_ranking["Spain"],
            "Team.HHR": 0,
            "Rank": 1,
        },
        {
            "Team.Name": "Denmark",
            "Team.PG": 3,
            "Team.GD": 1,
            "Team.GS": 4,
            "Team.GA": 3,
            "Team.W": 1,
            "Team.Points": 5,
            "Team.EQR": team.euro_qualifier_ranking["Denmark"],
            "Team.HHR": 0,
            "Rank": 2,
        },
        {
            "Team.Name": "Belgium",
            "Team.PG": 3,
            "Team.GD": 0,
            "Team.GS": 5,
            "Team.GA": 5,
            "Team.W": 1,
            "Team.Points": 3,
            "Team.EQR": team.euro_qualifier_ranking["Belgium"],
            "Team.HHR": 0,
            "Rank": 3,
        },
        {
            "Team.Name": "England",
            "Team.PG": 3,
            "Team.GD": -2,
            "Team.GS": 1,
            "Team.GA": 3,
            "Team.W": 0,
            "Team.Points": 2,
            "Team.EQR": team.euro_qualifier_ranking["England"],
            "Team.HHR": 0,
            "Rank": 4,
        },
    ]

    # Calculate standings
    standings = sample_group_D_5_5_3_2.calculate_standings()

    # Assert that the calculated standings match the expected standings
    assert standings.to_dict(orient="records") == expected_standings


def test_calculate_standings_4_4_4_4_GD(sample_group_4_4_4_4_DG):
    # Expected standings based on the sample group
    expected_standings = [
        {
            "Team.Name": "Spain",
            "Team.PG": 3,
            "Team.GD": 2,
            "Team.GS": 6,
            "Team.GA": 4,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["Spain"],
            "Team.HHR": 1,
            "Rank": 1,
        },
        {
            "Team.Name": "Denmark",
            "Team.PG": 3,
            "Team.GD": 1,
            "Team.GS": 5,
            "Team.GA": 4,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["Denmark"],
            "Team.HHR": 1,
            "Rank": 2,
        },
        {
            "Team.Name": "Belgium",
            "Team.PG": 3,
            "Team.GD": -1,
            "Team.GS": 4,
            "Team.GA": 5,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["Belgium"],
            "Team.HHR": 1,
            "Rank": 3,
        },
        {
            "Team.Name": "England",
            "Team.PG": 3,
            "Team.GD": -2,
            "Team.GS": 4,
            "Team.GA": 6,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["England"],
            "Team.HHR": 1,
            "Rank": 4,
        },
    ]

    # Calculate standings
    standings = sample_group_4_4_4_4_DG.calculate_standings()

    # Assert that the calculated standings match the expected standings
    assert standings.to_dict(orient="records") == expected_standings


def test_calculate_standings_4_4_4_4_RF(sample_group_4_4_4_4_RF):
    # Expected standings based on the sample group
    expected_standings = [
        {
            "Team.Name": "Belgium",
            "Team.PG": 3,
            "Team.GD": 0,
            "Team.GS": 4,
            "Team.GA": 4,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["Belgium"],
            "Team.HHR": 1,
            "Rank": 1,
        },
        {
            "Team.Name": "England",
            "Team.PG": 3,
            "Team.GD": 0,
            "Team.GS": 4,
            "Team.GA": 4,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["England"],
            "Team.HHR": 1,
            "Rank": 2,
        },
        {
            "Team.Name": "Spain",
            "Team.PG": 3,
            "Team.GD": 0,
            "Team.GS": 4,
            "Team.GA": 4,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["Spain"],
            "Team.HHR": 1,
            "Rank": 3,
        },
        {
            "Team.Name": "Denmark",
            "Team.PG": 3,
            "Team.GD": 0,
            "Team.GS": 4,
            "Team.GA": 4,
            "Team.W": 1,
            "Team.Points": 4,
            "Team.EQR": team.euro_qualifier_ranking["Denmark"],
            "Team.HHR": 1,
            "Rank": 4,
        },
    ]

    # Calculate standings
    standings = sample_group_4_4_4_4_RF.calculate_standings()

    # Assert that the calculated standings match the expected standings
    assert standings.to_dict(orient="records") == expected_standings


def test_calculate_standings_6_6_6_0(sample_group_6_6_6_0):
    # Expected standings based on the sample group
    expected_standings = [
        {
            "Team.Name": "Belgium",
            "Team.PG": 3,
            "Team.GD": 1,
            "Team.GS": 2,
            "Team.GA": 1,
            "Team.W": 2,
            "Team.Points": 6,
            "Team.EQR": team.euro_qualifier_ranking["Belgium"],
            "Team.HHR": 1,
            "Rank": 1,
        },
        {
            "Team.Name": "Spain",
            "Team.PG": 3,
            "Team.GD": 1,
            "Team.GS": 2,
            "Team.GA": 1,
            "Team.W": 2,
            "Team.Points": 6,
            "Team.EQR": team.euro_qualifier_ranking["Spain"],
            "Team.HHR": 1,
            "Rank": 2,
        },
        {
            "Team.Name": "Denmark",
            "Team.PG": 3,
            "Team.GD": 1,
            "Team.GS": 2,
            "Team.GA": 1,
            "Team.W": 2,
            "Team.Points": 6,
            "Team.EQR": team.euro_qualifier_ranking["Denmark"],
            "Team.HHR": 1,
            "Rank": 3,
        },
        {
            "Team.Name": "England",
            "Team.PG": 3,
            "Team.GD": -3,
            "Team.GS": 0,
            "Team.GA": 3,
            "Team.W": 0,
            "Team.Points": 0,
            "Team.EQR": team.euro_qualifier_ranking["England"],
            "Team.HHR": 0,
            "Rank": 4,
        },
    ]

    # Calculate standings
    standings = sample_group_6_6_6_0.calculate_standings()

    # Assert that the calculated standings match the expected standings
    assert standings.to_dict(orient="records") == expected_standings


def test_calculate_standings_9_3_3_3(sample_group_9_3_3_3):
    # Expected standings based on the sample group
    expected_standings = [
        {
            "Team.Name": "Spain",
            "Team.PG": 3,
            "Team.GD": 3,
            "Team.GS": 3,
            "Team.GA": 0,
            "Team.W": 3,
            "Team.Points": 9,
            "Team.EQR": team.euro_qualifier_ranking["Spain"],
            "Team.HHR": 0,
            "Rank": 1,
        },
        {
            "Team.Name": "Belgium",
            "Team.PG": 3,
            "Team.GD": -1,
            "Team.GS": 1,
            "Team.GA": 2,
            "Team.W": 1,
            "Team.Points": 3,
            "Team.EQR": team.euro_qualifier_ranking["Belgium"],
            "Team.HHR": 1,
            "Rank": 2,
        },
        {
            "Team.Name": "England",
            "Team.PG": 3,
            "Team.GD": -1,
            "Team.GS": 1,
            "Team.GA": 2,
            "Team.W": 1,
            "Team.Points": 3,
            "Team.EQR": team.euro_qualifier_ranking["England"],
            "Team.HHR": 1,
            "Rank": 3,
        },
        {
            "Team.Name": "Denmark",
            "Team.PG": 3,
            "Team.GD": -1,
            "Team.GS": 1,
            "Team.GA": 2,
            "Team.W": 1,
            "Team.Points": 3,
            "Team.EQR": team.euro_qualifier_ranking["Denmark"],
            "Team.HHR": 1,
            "Rank": 4,
        },
    ]

    # Calculate standings
    standings = sample_group_9_3_3_3.calculate_standings()

    # Assert that the calculated standings match the expected standings
    assert standings.to_dict(orient="records") == expected_standings
