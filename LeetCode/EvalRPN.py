
'''
逆波兰表达式

示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    	stack = []
    	for val in tokens:
    		if val == '+':
    			stack.append(stack.pop()+stack.pop())
    			pass
    		elif val == '-':
    			first = stack.pop()
    			second = stack.pop()
    			stack.append(second - first)
    			pass
    		elif val == '*'：
    			stack.append(stack.pop()*stack.pop())
    			pass
    	    elif val == '/':
    	    	first = stack.pop()
    			second = stack.pop()
    			stack.append(second / first)
    	    	pass
    	    else:
    	    	stack.append(int(i))
    	return sum(stack)    					
    	pass
