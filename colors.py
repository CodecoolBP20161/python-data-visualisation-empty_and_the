class Colors:

    def __init__(self, hex_code):
        self.hex_code = hex_code

    def hex_to_rgb(self):
        if self.hex_code is None:
            return None
        long_hex_code = list(self.hex_code)[1] * 2 + list(self.hex_code)[2] * 2 + list(self.hex_code)[3] * 2
        lv = len(long_hex_code)
        return tuple(int(long_hex_code[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
