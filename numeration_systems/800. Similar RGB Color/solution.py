class Solution:
    def similarRGB(self, color: str) -> str:
        res = "#"

        def findTar(curHex):
            highSim = float("inf")
            tarOneHex = -1

            cur = int(curHex, 16)

            for i in range(16):
                tar = 17 * i
                targetSim = (cur - tar) ** 2
                if targetSim < highSim:
                    highSim = targetSim
                    tarOneHex = i
            return format(tarOneHex, 'x') * 2

        for j in range(1, len(color), 2):
            tarTwoHex = findTar(color[j:j+2])
            res += tarTwoHex

        return res
