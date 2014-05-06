#!/usr/local/bin/python2.7
    

def heapsort(inputs):
  print "Input Array"
  print inputs
  print 
  l = []
  
  for start in range((len(inputs)-2)/2,-1,-1):
 
    heapify(inputs, start)
 
  print "After Heapifying "
  print inputs
  
  for end in range((len(inputs)-1),0,-1):
    inputs[end],inputs[0] = inputs[0],inputs[end]
    l.insert(0,inputs.pop())
    heapify(inputs,0)
  
  print 
  print "Output Array"
  print  l
  

  
  
def heapify(inputs, element):
  
  left = element * 2 +1;
  right = element * 2 + 2;
 
  
  if left <= len(inputs)-1 and inputs[left] > inputs[element]:
    large = left
  else:
    large = element
    
  if right <= len(inputs)-1 and inputs[right] > inputs[large]:
    large = right
    
    
  if element != large:
    temp = inputs[large]
    inputs[large] = inputs[element]
    inputs[element] = temp
    heapify(inputs, large)

	
	

inputs = [ 10, 19, 7, 6, 4, 3, 2, 1, 20, 9]
heapsort(inputs)
