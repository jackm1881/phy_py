class ChargedParticle:
    def __init__(self,chrg: float,pos: list) -> None:
        self.charge = chrg
        while len(pos) != 3:
            pos.append(0.0)
        self.pos = pos
        

    def __repr__(self) -> str:
        r = "charge: {} C, x = {}, y = {}, z = {}".format(self.charge,self.pos[0],self.pos[1],self.pos[2])