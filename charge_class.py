class ChargedParticle:
    def __init__(self, chrg: float, pos: list) -> None:
        self.charge = chrg
        if len(pos) != 3:
            raise ValueError("Position must have three components.")
        self.pos = pos  
    def __repr__(self) -> str:
        r = "Charge: {} C. Positon: x = {} m, y = {} m, z = {} m".format(self.charge,self.pos[0],self.pos[1],self.pos[2])
        return r