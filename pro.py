import ba

# ba_meta require api 6
# ba_meta export plugin

class Unlock(ba.Plugin):
    ba.app.accounts.have_pro = lambda: True
