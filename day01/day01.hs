checkIfDeeper prev nums =
  head nums > prev

replicate' n x
  | n <= 0 = []
  | otherwise = x : replicate' (n -1) x

countDepth' numDepths depthList
  | null (head depthList) = numDepths
  | otherwise = numDepths + countDepth' numDepths (tail depthList)

-- main =
--   print (countDepth' 0 [1, 2, 3])