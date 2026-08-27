from dataclasses import dataclass

from Options import PerGameCommonOptions, Choice, OptionGroup, Range, Toggle


class Goal(Choice):
    """
    Defines wich goal is used
    Nolok: The goal is, like in usual STK, to beat nolok in the final race at fort magma
    Grad Pix: Beat all four Grand Prix to goal
    """

    display_name = "Goal"

    option_nolok = 0
    option_gp = 1

    default = option_nolok

class GoalDifficulty(Choice):
    """
    Sets the minimum difficulty required to goal.
    For example: selecting hard mode will trigger the goal (when you selected nolok goal)
    only when you win fort magma in at least hard mode
    """

    display_name = "Goal Difficulty"

    option_easy = 0
    option_normal = 1
    option_hard = 2
    option_supertux = 3

    default = option_easy

class RequiredKeys(Range):
    """
    Controls how many keys are required to open the door to noloks fort magma
    Keys are items placed in the multiworld
    """

    display_name = "Required Keys"

    range_start = 0
    range_end = 20
    default = 3

class GeneratedKeys(Range):
    """
    Defines how many keys are placed in the multiworld.
    Has to be at least the required ones
    """

    display_name = "Generated Keys"

    range_start = 0
    range_end = 20
    default = 5

class RequiredPoints(Range):
    """
    Changes the points required points to unlock fort magma
    """

    display_name = "Required Points"

    range_start = 0
    range_end = 300
    default = 190

class Nitro(Toggle):
    """
    Adds Nitro Ability to the itempool
    """

    display_name = "Nitro"
    default = True

class Skid(Toggle):
    """
    Adds Skid Ability to the itempool
    """

    display_name = "Skid"
    default = True

class LookBack(Toggle):
    """
    Adds Look Back Ability to the itempool
    """

    display_name = "Look Back"
    default = True

class DeathLink(Toggle):
    """
    Enables Death Link
    """

    display_name = "Death Link"
    default = False

class DeathLinkSendMode(Choice):
    """
    When do you send Death Link
    Challenge Lost: Death Link is triggered when you fail a challenge
    Knockout: Death Link is triggered every time you get knocked out by something (e.g. a bowling ball)
    Both: Death Link is triggered when you loose a challenge and get knocked out
    """

    display_name = "Death Link Send Mode"

    option_knockout = 0
    option_challenge_lost = 1
    option_both = 2

    default = 1


class DeathLinkReceiveMode(Choice):
    """
    What happens when you receive a Death Link
    Knockout: On receive you simply get knocked out
    Loose Challenge: On Death Link give up will be triggered when you are in a challenge
    """

    display_name = "Death Link Receive Mode"

    option_knockout = 0
    option_loose_challenge = 1

    default = 0

@dataclass
class STKOptions(PerGameCommonOptions):
    goal: Goal
    goal_difficulty: GoalDifficulty
    required_keys: RequiredKeys
    generated_keys: GeneratedKeys
    required_points: RequiredPoints
    nitro: Nitro
    skid: Skid
    look_back: LookBack
    death_link: DeathLink
    death_link_send_mode: DeathLinkSendMode
    death_link_receive_mode: DeathLinkReceiveMode

option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal, GoalDifficulty]
    ),
    OptionGroup(
        "Abilities",
        [Nitro, Skid, LookBack]
    ),
    OptionGroup(
        "Death Link",
        [DeathLink, DeathLinkSendMode, DeathLinkReceiveMode]
    )
]