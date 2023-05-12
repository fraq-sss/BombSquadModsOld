import ba
from bastd.actor.spaz import Spaz

Spaz.dash = True


def new_hook(spaz: Spaz) -> None:
    old_hook(spaz)
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
            "impulse",
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
        ba.getsound("shieldHit"),
        volume=time / 1000,
        position=node.position
    )

    for i in range(5):
        ba.timer(i * 0.01, impulse)


old_hook = Spaz.on_punch_release
Spaz.on_punch_release = new_hook
