import cocos
import pyglet


class Move(cocos.actions.Move):
    def __init__(self, *args, **kwargs):
        super(Move, self).__init__(self, *args, **kwargs)

class Layer(cocos.layer.Layer):
    def __init__(self):
        super(Layer, self).__init__()


class Sprite(cocos.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Sprite, self).__init__(*args, **kwargs)

    def do(self, action, target=None):
        """Executes an :class:`.Action`.
        When the action is finished, it will be removed from the node's actions
        container.

        To remove an action you must use the :meth:`do` return value to
        call :meth:`remove_action`.

        Arguments:
            action (Action):
                Action that will be executed.
        Returns:
            Action: A clone of ``action``

        """
        a = action

        if target is None:
            a.target = self
        else:
            a.target = target

        a.start()
        self.actions.append(a)

        if not self.scheduled:
            if self.is_running:
                self.scheduled = True
                pyglet.clock.schedule(self._step)
        return a