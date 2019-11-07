{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 15, 27, 33, 44, 83]\n"
     ]
    }
   ],
   "source": [
    "Arr=[33,4,27,83,44,15]\n",
    "class solution(object):\n",
    "    def divide(self,Arr):\n",
    "        if len(Arr)==1:\n",
    "            return Arr ##如果Arr裡面只有一個數字，就可以先return\n",
    "        else:\n",
    "            x=len(Arr)//2\n",
    "            right=Arr[x:]#切一半\n",
    "            left=Arr[:x]\n",
    "         \n",
    "            left = self.divide(left)#每個left都要被divide\n",
    "            right = self.divide(right)\n",
    "            merge = self.merge(left,right)\n",
    "        return merge\n",
    "    \n",
    "    def merge(self,left,right):         \n",
    "        i=[]                 #建立一個空間i 拿來放等下left跟right兩組比較下比較小的那個數字\n",
    "        while left and right:  \n",
    "    \n",
    "            if left[0]> right[0]:      #建立條件 左邊的第一個數字大於右邊的話 就把右邊的第一個數字放入i，相反就把左邊第一個數放入\n",
    "    \n",
    "                i.append(right.pop(0)) #在i加入right的第一個數的時候同時把right的第一個數刪掉\n",
    "            else:\n",
    "                i.append(left.pop(0))\n",
    "        \n",
    "        if left:   #如果i裡面有left+i 代表都丟完了\n",
    "            i += left\n",
    "       \n",
    "        if right:\n",
    "            i += right    \n",
    "        return i\n",
    "    \n",
    "          \n",
    "    def merge_sort(self, Arr):\n",
    "        key= self.divide(Arr)\n",
    "        print(key)\n",
    "        \n",
    "d=solution()\n",
    "d.merge_sort(Arr)        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
