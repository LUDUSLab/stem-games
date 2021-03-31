from enum import Enum


class GameLogic:

    class State(Enum):
        """ Possible states for the GameLogicHandler. """
        DEAD, NO_FOOD, FOOD_EATEN = 0, 1, 2

    def update(self):  #add as condicoes
        if (por aqui condicoes de quando ela bate em si mesma e quando bate no wall ou nos obstaculos ou quandoela bate na cobra bot):
            return self.State.DEAD  # game over

        '''food = (self._board[i][j] == config.FOOD)
        self._move_snake((i, j))'''

        if food:
            '''condicoes ede quando a cobra come'''
            return self.State.FOOD_EATEN

        return self.State.NO_FOOD


class Action:
    """ Actions that can be taken by the snake. """
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

    @staticmethod
    def opposite(action):
        """ Returns the action related to a movement in the opposite direction. """
        if action == action.UP: return action.DOWN
        if action == action.DOWN: return action.UP
        if action == action.LEFT: return action.RIGHT
        return action.LEFT