class Colors:

    @staticmethod
    def hex_to_rgb(hex_code):
        long_hex_code = list(hex_code)[1] * 2 + list(hex_code)[2] * 2 + list(hex_code)[3] * 2
        lv = len(long_hex_code)
        return tuple(int(long_hex_code[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
