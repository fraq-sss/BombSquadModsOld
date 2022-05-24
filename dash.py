import ba
from bastd.actor.spaz import Spaz

dash = True

def new_pickup_release(self) -> None:
    old_pickup_release(self)
    time_ms = ba.time(timeformat=ba.TimeFormat.MILLISECONDS)
    def impulse() -> None:
        self.node.handlemessage("impulse",
        self.node.position[0],
        self.node.position[1],
        self.node.position[2],
        self.node.move_left_right * 30,
        self.node.position[1] + 5,
        self.node.move_up_down * -30, 5, 5, 0, 0,
        self.node.move_left_right * 30,
        self.node.position[1] + 5,
        self.node.move_up_down * -30)

    if not dash \
    or not self.node.exists() \
    or self.node.knockout > 0.0 \
    or self.node.frozen > 0.0 \
    or time_ms - self.last_pickup_time_ms < 800:
        return
    ba.emitfx(
        position=self.node.position,
        velocity=self.node.velocity,
        count=50,
        scale=0.5,
        spread=1.0,
        chunk_type='spark')

    for i in range(5):
        ba.timer(i * 0.01, impulse)
        ba.playsound(ba.getsound("shieldHit"))

old_pickup_release = Spaz.on_pickup_release
Spaz.on_pickup_release = new_pickup_release

# ba_meta require api 6
# ba_meta export plugin

class Dash(ba.Plugin):
    pass