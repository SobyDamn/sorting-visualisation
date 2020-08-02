from tkinter import Canvas,Label
import tkinter as tk
import time
window = tk.Tk()
window.title("Sorting Algorithm Visualisation")
bar_containerH = 768
bar_containerW = 1366
bar_width = 20
bar_startX = 100
bar_bottom = 525 #bottom y coordinate of bar,less than this will increase height
bar_minY = 300 #y cordinates when value is minimum
bar_min_maxH = 175 #diff between max and min height a bar can have
anim_sleep = 0.005
bar_min_movement = 0.5
graph_canvas = Canvas(window, width=bar_containerW, height=bar_containerH)
lineX_axis = graph_canvas.create_line(60,527,1300,527,width=2,fill="#4a4a4a")
lineY_axis = graph_canvas.create_line(60,527,60,27,width=2,fill="#4a4a4a")
graph_canvas.configure(bg="white")
graph_canvas.pack(fill=tk.X)
class Bar:
    def __init__(self,index,val,max_val):
        self.val = val
        self.index = index
        self.xPos = bar_startX + bar_width*index
        self.yPos = bar_minY - bar_min_maxH*(val/max_val)
        self.bar = graph_canvas.create_rectangle(self.xPos,self.yPos,self.xPos+bar_width,bar_bottom,outline="black", fill="blue")
        self.label = graph_canvas.create_text(self.xPos+10,self.yPos-20,text=self.val,angle=90,fill="#4a4a4a",font=("Helvetica", 8, "bold"))
        self.indexLabel = graph_canvas.create_text(self.xPos+10,bar_bottom+15,text=index+1,fill="#4a4a4a",font=("Helvetica", 8, "bold"))
    def moveBar(self,new_index):
        new_index = round(new_index,1)
        self.distance = new_index - self.index
        try:
            graph_canvas.move(self.bar,self.distance*bar_width,0)
            graph_canvas.move(self.label,self.distance*bar_width,0)
            window.update()
            self.index = new_index
        except:
            exit()
            pass
def smoothMove(obj,newPos):
    if newPos > obj.index:
        while True:
            i = bar_min_movement
            obj.moveBar(obj.index+i)
            time.sleep(anim_sleep)
            if obj.index >= newPos:
                break
    else:
        while True:
            i =-bar_min_movement
            obj.moveBar(obj.index+i)
            time.sleep(anim_sleep)
            if obj.index <= newPos:
                break
def insertionSort(objectList,size):
    for i in range(0,len(objectList)):
        j=i
        while j>0:
            if(objectList[j-1].val>objectList[j].val):
                print("Swapping for",j-1,j)
                smoothMove(objectList[j-1],j)
                smoothMove(objectList[j],j-1)
                objectList[j-1],objectList[j] = objectList[j],objectList[j-1]
            else:
                break
            j = j-1
                
def selectionSort(objectList,size):
    for i in range(0,size):
        min_idx = i
        for j in range(i+1,size):
            if objectList[min_idx].val>objectList[j].val:
                min_idx = j
        smoothMove(objectList[i],min_idx)
        smoothMove(objectList[min_idx],i)
        objectList[i],objectList[min_idx] = objectList[min_idx],objectList[i]

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
    while i < n1 and j < n2 : 
        if L[i].val <= R[j].val:
            arr[k] = L[i]
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
 
def main():
    array = [26,50,71,80,80,77,60,90,24,38,72,60,100,80,62,3,98,97,14,56,1,7,36,39,24,67,99,16,41,51,51,11,7,79,9,43,67,85,23,12]
    maxVal = max(array)
    size = len(array)
    objList = []
    for i in range(0,size):
        objList.append(Bar(i,array[i],maxVal))
    ##
    #insertionSort(objList,size)
    selectionSort(objList,size)
if __name__=="__main__":
    main()
window.mainloop()