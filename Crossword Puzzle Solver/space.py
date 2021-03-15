class Space:
    def __init__(self,direction_init,length_init,point_init):
        self.direction = direction_init
        self.length = length_init
        self.starting_point = point_init

    def __repr__(self):
        return "".join(["Space(", str(self.direction), ",", str(self.length),",", str(self.starting_point), ")"])
