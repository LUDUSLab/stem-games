import config

wkey_aux = 0
hs_aux = 1

class ScoreMenu:
    record_scores = []

    def __init__(self, hud, footer1, footer2, start_txt):
        self.hud = hud
        self.has_entered_nick = False
        self.start_txt = start_txt
        self.footer1 = footer1
        self.footer2 = footer2
        self.header = config.Text("HIGH  SCORES", 32)
        self.header.pos = ((config.window.size[0] - self.header.text.get_size()[0])/2, 150)
        self.pvp_mode = False
        self.nick_box_text = ""
        self.nick_box = config.Text(f'{self.nick_box_text}', 32)
        self.nick_box.pos = ((config.window.size[0] - self.nick_box.text.get_size()[0])/2, 400)
        self.name_save_header = [config.Text(x, 32) for x in [
            "YOUR SCORE IS ONE OF THE TEN BEST", "PLEASE ENTER YOUR INITIALS", "PUSH ROTATE TO SELECT LETTER",
            "PUSH HYPERSPACE WHEN LETTER IS CORRECT"
        ]]
        aux = 0
        for t in self.name_save_header:
            t.pos = ((config.window.size[0] - self.name_save_header[0].text.get_size()[0])/2 - 100, 120+aux)
            aux += 40

    def write_nick(self, key_name):
        global wkey_aux, hs_aux
        self.nick_box_text += key_name
        if wkey_aux > 2:
            if hs_aux == 1:
                self.nick_box_text = self.nick_box_text[:3]
            aux_str = "".join([" " for _ in range(7-len(self.hud.score_p1.message))])
            self.record_scores.append(
                config.Text(f'{hs_aux}{aux_str}{self.hud.score_p1.message} {self.nick_box_text}', 32, pos=(
                    self.header.pos[0], self.header.pos[1] + 75+hs_aux*40)))
            hs_aux += 1
            wkey_aux = 0
            self.has_entered_nick = True

        self.nick_box = config.Text(f'{self.nick_box_text}', 32)
        self.nick_box.pos = ((config.window.size[0] - self.nick_box.text.get_size()[0])/2, 600)
        wkey_aux += 1

    def display(self):
        if not self.has_entered_nick:
            for t in self.name_save_header:
                t.display()
            self.nick_box.display()
        else:
            self.start_txt.display()
            self.header.display()
            self.footer1.display()
            for rs in self.record_scores:
                rs.display()

        self.footer2.display()
        self.hud.menu_display()
