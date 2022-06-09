import ba
from bastd.actor.spaz import Spaz

Spaz.dash = True

def new_punch_release(self) -> None:
    old_punch_release(self)
    time = ba.time(timeformat=ba.TimeFormat.MILLISECONDS)
    spaz = self.node
    def impulse() -> None:
        spaz.handlemessage("impulse",
        spaz.position[0],
        spaz.position[1],
        spaz.position[2],
        spaz.move_left_right * 30,
        spaz.position[1] + 5,
        spaz.move_up_down * -30, 5, 5, 0, 0,
        spaz.move_left_right * 30,
        spaz.position[1] + 5,
        spaz.move_up_down * -30)

    if not self.dash \
    or not spaz.exists() \
    or spaz.knockout > 0.0 \
    or spaz.frozen > 0.0 \
    or time - self.last_punch_time_ms < 800:
        return
    ba.emitfx(
        position=spaz.position,
        velocity=spaz.velocity,
        count=50,
        scale=0.5,
        spread=1.0,
        chunk_type='spark')

    for i in range(5):
        ba.timer(i * 0.01, impulse)
        ba.playsound(ba.getsound("shieldHit"))

old_punch_release = Spaz.on_punch_release
Spaz.on_punch_release = new_punch_release

# ba_meta require api 6
# ba_meta export plugin

class Dash(ba.Plugin):
    pass
