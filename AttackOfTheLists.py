from heapq import merge

class AttackOfTheLists(object):

    def swapTwoLists(self, a, b):
        """
        Args:  a: List a
               b: List b
        Return: List a, List b with contents swapped
        """
        if a[0] > b[0]:
            print("Alert: Detected Index Position 0 of list a greater than b")
            for each in range(len(a)):
                a[each], b[each] = b[each], a[each]
            print("Swapped List Structures: \nList A : {}\nList B : {}".format(a, b))
        else:
            print(a, b)

    def sortLists(self, a, b):
        """
        Args:  a: List a
               b: List b
        Return: List a, List b with contents sorted
        """
        print("Pre-Sort List Structures: \nList A : {}\nList B : {}".format(a,b))
        a = self.quicksorter(a)
        b = self.quicksorter(b)
        print("Post-Sort List Structures: \nList A : {}\nList B : {}".format(a,b))
        return a,b

    def quicksorter(self, arr):
        """
        Args:
            arr: List array
        Return:
            quickSorter: sorted list array via quicksort algorithm
        """
        # Initialize Lists
        pivoter = []
        highVal = []
        lowVal = []
        # Check size of list, if 1 or less, no need to sort, just return
        if len(arr) <= 1:
            return arr
        # Else, array contains items that must be sorted
        else:
            # Set pivot = first index
            pivot = arr[0]
            # For each element in arr, compare and append to higher/lower list or pivoter
            for i in arr:
                if i < pivot:
                    lowVal.append(i)
                elif i > pivot:
                    highVal.append(i)
                else:
                    pivoter.append(i)
            low = self.quicksorter(lowVal)
            high = self.quicksorter(highVal)
            quickSorter = (low + pivoter + high)
        return quickSorter

    def mergeLists(self, a,b):
        """
        Args:
            a: List array
            b: List array
        Return:
            combinedList: merged list via heapq merge
        """
        combinedLists = list(merge(a,b))
        return combinedLists

    def checkIfSorted(self, a,b):
        """
        Args:
            a: List array
            b: List array
        Return:
            iterList: merged, potentially sorted list
        """
        iterList = [a,b]
        indexCounter = 0
        for each in iterList:
            for element in each:
                if all(each[element] <= each[element + 1] for element in range(len(each) - 1)):
                    pass
                else:
                    print("Unsorted Array Detected, passing lists to sorting protocol")
                    iterList[indexCounter] = self.quicksorter(iterList[indexCounter])
                    break
            indexCounter+=1
        return iterList
