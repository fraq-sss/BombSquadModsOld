# ba_meta require api 7

import ba
from bastd.actor.spaz import Spaz


def new_hook(spaz: Spaz) -> None:
    spaz.old_hook()
    time = ba.time(timeformat=ba.TimeFormat.MILLISECONDS) - spaz.last_punch_time_ms
    node = spaz.node

    if spaz.dash is False \
    or node.exists() is False \
    or node.knockout > 0.0 \
    or node.frozen > 0.0 \
    or spaz.last_punch_time_ms == -9999 \
    or time < 1000:
        return

    def impulse() -> None:
        node.handlemessage(
            'impulse',
            node.position[0],
            node.position[1],
            node.position[2],
            node.move_left_right * 30,
            node.position[1] + 5,
            node.move_up_down * -30,
            5,
            5,
            0,
            0,
            node.move_left_right * 30,
            node.position[1] + 5,
            node.move_up_down * -30
        )

    ba.emitfx(
        position=node.position,
        velocity=node.velocity,
        count=50,
        scale=0.5,
        spread=1.0,
        chunk_type='spark'
    )

    ba.playsound(
        ba.getsound('shieldHit'),
        volume=time / 1000,
        position=node.position
    )

    for i in range(5):
        ba.timer(i * 0.01, impulse)


class Dash(ba.Plugin):
    def on_app_running(self) -> None:
        Spaz.dash_enabled = True
        Spaz.old_hook = Spaz.on_punch_release

        # Monkey-patching: https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/
        Spaz.on_punch_release = new_hook
