import ba

from bastd.actor.spaz import Spaz


Spaz.dash = True


def new_dash(self) -> None:
    old_dash(self)
    time = ba.time(timeformat=ba.TimeFormat.MILLISECONDS) - self.last_punch_time_ms
    spaz = self.node

    def impulse() -> None:
        spaz.handlemessage("impulse",
        spaz.position[0],
        spaz.position[1],
        spaz.position[2],
        spaz.move_left_right * 30,
        spaz.position[1] + 5,
        spaz.move_up_down * -30,
        5, 5, 0, 0,
        spaz.move_left_right * 30,
        spaz.position[1] + 5,
        spaz.move_up_down * -30)

    if self.dash == False \
    or spaz.exists() == False \
    or spaz.knockout > 0.0 \
    or spaz.frozen > 0.0 \
    or self.last_punch_time_ms == -9999 \
    or time < 1000:
        return

    ba.emitfx(
        position=spaz.position,
        velocity=spaz.velocity,
        count=50,
        scale=0.5,
        spread=1.0,
        chunk_type='spark')

    ba.playsound(
        ba.getsound("shieldHit"),
        volume=time / 1000,
        position=spaz.position)

    for i in range(5):
        ba.timer(i * 0.01, impulse)


old_dash = Spaz.on_punch_release
Spaz.on_punch_release = new_dash


# ba_meta require api 7
# ba_meta export plugin

class Dash(ba.Plugin):
    pass