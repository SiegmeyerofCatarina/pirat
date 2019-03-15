import cocos
import pyglet


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