import interactions


class Entity:

    def __init__(self, entity_type: str, pos_x: int, pos_y: int, tile: str, interactable: bool = False):
        self.entity_type: str = entity_type
        self.data = {
            "pos_x": pos_x,
            "pos_y": pos_y
        }
        # tile is the emoji string, ex: <a:_:499435126908780554>
        self.tile: str = tile
        self.interactable: bool = interactable
        pass


class NPC(Entity):
    from game import Game

    def __init__(self, pos_x: int, pos_y: int, tile: str, dialogue: interactions.Dialogue):
        entity_type = "npc"
        super().__init__(entity_type, pos_x, pos_y, tile, True)
        self.dialogue: interactions.Dialogue = dialogue

    def interact(self, session: Game):
        self.dialogue.interact(session)