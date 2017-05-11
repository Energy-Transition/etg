"""
All the classes and methods having to do with the political parties in the game.
"""
from .entity import Entity

class Party(Entity):
    """
    A class to represent the parties in the simulation. It contains
    information about the state of the party (funds, policies, voters,
    etc) and methods for updating the party and validating user input. The
    parties are created when a player joins, and should not be created
    manually.
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, simulation, options, name):
        super(Party, self).__init__(simulation)
        self.set_values(options)
        self.name = name

    def set_values(self, config):
        """
        Set all the values on this party by coping them from the config dict
        from the simulation.
        """
        self.money = config['parties']['starting_money']
        self.taxes = {}
        for energy_type in self.simulation.energy_types:
            self.taxes[energy_type.name] = 0
        self.campaign_budget = 0

    @property
    def voters(self):
        """
        All the voters for this party, as an :class:`~etg.util.agentset.AgentSet`.
        """
        return self.simulation.agents.filter(lambda a: a.party == self)

    @property
    def campaign(self):
        """
        How much is spend on campaigning in this tick.
        """
        pass

    @property
    def income(self):
        """
        How much money the company earned this tick.
        """
        pass
