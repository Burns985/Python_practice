class Solution:
    def trap(self, height: [int]) -> int:
        h_list = []
        start = 0
        for i in range(len(height)):
            if height[i] >= 1:
                start = i
                break

        water = 0
        for i in range(len(height)):
            if i >= start:
                h_list.append(height[i])
                if i + 1 < len(height):
                    if h_list[len(h_list) - 1] <= height[i + 1]:
                        if h_list[len(h_list) - 1] == height[i + 1]:
                            for h in h_list:
                                water += height[i + 1] - h
                        else:
                            for h in h_list:
                                water += h_list[len(h_list) - 1] - h
                        end = h_list[len(h_list) - 1]
                        print(water)
                        h_list.clear()
                        h_list.append(end)
        print(abs(water))
        return abs(water)
        # print(h_list)


try:
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    print("All Bright")
except AssertionError:
    print("All Jeans")

try:
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9

    print("Sun for All")
except AssertionError:
    print("Love for All")
