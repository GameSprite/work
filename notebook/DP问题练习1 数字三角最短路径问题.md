### DP问题练习1:数字三角最短路径问题

#### 问题描述

给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。

#### 样例:

比如，给出下列数字三角形：

```javascript
     2
    3 4
   6 5 7
  4 1 8 3 
```

从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。

#### 思路

```javascript
我们给每一个位置标上坐标
     2       (0,0)
    3 4   (1,0) (1,1)
   6 5 7      ...
  4 1 8 3     ...
  我们用f(i,j)表示从(i,j)位置一直到三角形底部的最小路径和。
  那么f(0,0) = min(f(1,0),f(1,1))+Value(0,0); Value(0,0)就是值2
  f(1,0) = min(f(2,0),f(2,1))+Value(1,0);
   ...
  1.推导出状态转移方程:
  f(i,j) = min(f(i+1,j),f(i+1,j+1)) + Value(i,j)。
  利用这个状态转移方程我们可以写出一个递归函数。
  2.递归的边界确定:
  对于f(i,j),当:
  i == 三角形高度-1 的时候，直接返回Value(i,j)
```

#### 代码:

```javascript
(function(){
    main();
})();
/**
 * [三角问题最小路径和]
 * @param  {[Array]} triangleList [trianglelist]
 * @return {[Number]} [length of minimumTotal]
 */
function minimumTotal(triangleList){
  //这个DP问题的状态转移方程
  //f(i,j) = min(f(i+1,j),f(i+1,j+1))+(i,j)  f(i,j)表示当前步骤(i,j)走到最后，所对应的最小路径和
  var triangleHeight = getTriangleHeight(triangleList);

  function calResult(i,j){
    if(i == triangleHeight-1){
        return triangleList[getIndex_i(i)+j];
    }else{
        var res1 = calResult(i+1,j);
        var res2 = calResult(i+1,j+1);
        return Math.min(res1,res2)+triangleList[getIndex_i(i)+j];
    }
  }
  return calResult(0,0);                                                                 }
/**
 * 获取三角形有多少行
 * @param  {[Array]} triangleList [description]
 * @return {[Number]}              [description]
 */
function getTriangleHeight(triangleList){
    var height = 0.5*(Math.sqrt(1+triangleList.length*8)-1);
    console.assert(parseInt(height) == height,"输入的三角形数据数量有误");
    return height;
}
/**
 * 通过行数获取该行第一个元素在数组中的下标
 * @param  {[Number]} lineNo [行标,从0开始计]
 * @return {[Number]}        [数组下标]
 */
function getIndex_i(lineNo){
    // if(lineNo == 0)
    //     return 0;
    // return getIndex_i(lineNo-1)+lineNo;
    //根据 f(n) = f(n-1)+n; f(0)=0 推到 f(n) = n(n+1)/2
    return lineNo*(lineNo+1)/2;
}

function main(){
    var TEMP = [2,3,4,6,5,7,4,1,8,9];
    console.log(minimumTotal(TEMP))
}
```

