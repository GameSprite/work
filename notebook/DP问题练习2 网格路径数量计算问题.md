### DP问题练习2:网格路径数量计算问题

#### 问题描述

有一个机器人的位于一个 m × n 个网格左上角。
机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。
问有多少条不同的路径？

#### 样例:

给出 m = 3 和 n = 3, 返回 6.
给出 m = 4 和 n = 5, 返回 35.

#### 思路

```javascript
用坐标i,j标识格子的位置，左上角为(0,0),右下角为(m-1,n-1)
状态转移方程:
f(i,j) = i>0?f(i-1,j):0 + j>0?f(i,j-1):0  //f(i,j)表示(i,j)位置的路径数量,i-1和j-1都要在允许的范围里，否则直接取值0
```

#### 代码:

```javascript
var M = 3;
var N = 3;
var LOG = console.log;
(()=>{
	main()
})();
function countPaths(m,n){
	return (m==n && m==0) ? 1 : ((m > 0 ? countPaths(m-1,n) : 0) + (n > 0 ? countPaths(m,n-1) : 0));
}
function main(){
	console.log(countPaths(M-1,N-1));
}
```

其实三年前我学数据结构这门课的时候做过一道类似的题，不过是求所有可能的路径。当时编码量不到800行，所以屁都不懂，就去网上找了一个解答，使用DFS。由于是第一次写比较复杂的程序，所以有很深的印象。就用dfs写一个解答缅怀一下吧:

```javasc
/**
 * 从左上角到右下角可能的路径数量  使用DFS算法
 * @param {[type]} m [description]
 * @param {[type]} n [description]
 */
function DFS_Pro(m,n){
	var count = 0;
	function dfs(x,y){
		if(x == m && y == n){
		  count ++;
		}else{
          if(x < m)
          	dfs(x+1,y)
          if(y < n)
          	dfs(x,y+1)
		}
	}

	dfs(0,0);
	return count;
}
```

