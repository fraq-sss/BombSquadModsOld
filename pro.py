import ba

# ba_meta require api 7
# ba_meta export plugin

class Unlock(ba.Plugin):
    ba.app.accounts_v1.have_pro = lambda: True