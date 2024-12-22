class SpecialSumSet:

    @staticmethod
    def make_set(targetsize, maximumsum):
        return SpecialSumSet._make_set(SpecialSumSet([], [True], [0], [0]), targetsize, maximumsum, 1)

    @staticmethod
    def _make_set(set, sizeremain, sumremain, startval):
        if sizeremain == 0:
            return set

        if sizeremain >= 2 and startval * sizeremain >= sumremain:
            return None

        endval = sumremain
        if len(set.values) >= 2:
            endval = min(set.values[0] + set.values[1] - 1, endval)

        for val in range(startval, endval + 1):
            temp = set.add(val)
            if temp is None:
                continue

            temp = SpecialSumSet._make_set(temp, sizeremain - 1, sumremain - val, val + 1)
            if temp is not None:
                return temp
        return None

    def __init__(self, vals, sumposb, minsum, maxsum):
        self.values = vals
        self.sumpossible = sumposb
        self.minimumsum = minsum
        self.maximumsum = maxsum

    def add(self, val):
        if val <= 0:
            raise ValueError("Value must be positive")
        size = len(self.values)
        if size >= 1 and val <= self.values[-1]:
            raise ValueError("Must add values in ascending order")

        posb = self.sumpossible
        if any((posb[i] and posb[i - val]) for i in range(val, len(posb))):
            return None

        newsize = size + 1
        minsum = self.minimumsum
        maxsum = self.maximumsum
        newmin = [0] + [min(minsum[i], minsum[i - 1] + val) for i in range(1, newsize)] + [minsum[size] + val]
        newmax = [0] + [max(maxsum[i], maxsum[i - 1] + val) for i in range(1, newsize)] + [maxsum[size] + val]

        if any((newmax[i] >= newmin[i + 1]) for i in range(newsize)):
            return None

        newposb = posb + [False] * val
        for i in reversed(range(val, len(newposb))):
            newposb[i] |= newposb[i - val]

        return SpecialSumSet(self.values + [val], newposb, newmin, newmax)

TARGET_SIZE = 7

maxsum = 1
while SpecialSumSet.make_set(TARGET_SIZE, maxsum) is None:
    maxsum *= 2

i = maxsum // 4
while i > 0:
    maxsum -= i
    if SpecialSumSet.make_set(TARGET_SIZE, maxsum) is None:
        maxsum += i
    i //= 2

set = SpecialSumSet.make_set(TARGET_SIZE, maxsum)
print("".join(map(str, set.values)))