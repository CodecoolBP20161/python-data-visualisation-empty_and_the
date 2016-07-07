class Colors:

    def __init__(self, hex_code):
        self.hex_code = hex_code

    def hex_to_rgb(self):
        if self.hex_code is None:
            return None
        long_hex_code = list(self.hex_code)[1] * 2 + list(self.hex_code)[2] * 2 + list(self.hex_code)[3] * 2
        lv = len(long_hex_code)
        return tuple(int(long_hex_code[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    @staticmethod
    def get_avg_color(list_colors):
        list_avg_color = [0, 0, 0]
        for element in list_colors:
            color = Colors(element)
            rgb_code = color.hex_to_rgb()
            for i in range(3):
                list_avg_color[i] += rgb_code[i]
        for i in range(3):
            list_avg_color[i] = int(list_avg_color[i]/len(list_colors))
        return list_avg_color
