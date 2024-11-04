class  Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x : (x.profit/x.weight), reverse=True)
    finalvalue = 0.0
    for item in arr:
        if item.weight <= W:
            W = W - item.weight
            finalvalue = finalvalue + item.profit

        else:
            finalvalue = finalvalue + item.profit * W/item.weight
            break

    return finalvalue

if __name__ == "__main__":
    W = 50
    arr = [Item(120,30), Item(100,20), Item(60,10)]

    max_val = fractionalKnapsack(W, arr)
    print("Maximum value in Knapsack =", max_val)
