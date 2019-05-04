###############################################
# File name   : test.py                       #
# Description : Unit testing for the solution #
# Author      : Pratik Kulkarni               #
# Date        : 03/30/2019                    #
# E-mail      : pratikkulkarni228@gmail.com   #
###############################################


import unittest
import cluster
obj = cluster.clusterCircle()
class ClusterRemoval(unittest.TestCase):
    def test_op(self):
        """
        Tests the working of the solution for various test cases
        """

        #TEST CASE 1 - Provided in the assignment
        input_1 =[(0.5,0.5,0.5),(1.5,1.5,1.1),(0.7,0.7,0.4),(4,4,0.7)]
        expected_output_1= [(1.5, 1.5, 1.1), (4, 4, 0.7)]

        #TEST CASE 2 - Provided in the assignment
        input_2 =[(1.5,1.5,1.3),(4,4,0.7)]
        expected_output_2= [(1.5, 1.5, 1.3), (4, 4, 0.7)]

        #TEST CASE 3 - Provided in the assignment
        input_3 =[(1,3,0.7),(2,3,0.4),(3,3,0.9)]
        expected_output_3= [(3, 3, 0.9)]

        #TEST CASE 4 - This test case includes two different clusters
        input_4 =[(0.5,0.5,0.5),(1.5,1.5,1.1),(0.7,0.7,0.4),(4,4,0.7),(1,5,0.7),(2,5,0.4),(3,5,0.9)]
        expected_output_4= [(3, 5, 0.9), (1.5, 1.5, 1.1)]	

        #TEST CASE 5 - This test case includes two different clusters along with 2 non-overlapping circles
        input_5 =[(0.5,0.5,0.5),(1.5,1.5,1.1),(0.7,0.7,0.4),(4,4,0.7),(1,5,0.7),(2,5,0.4),(3,5,0.9),(7,5,1),(6,7,0.9)]
        expected_output_5= [(3, 5, 0.9), (1.5, 1.5, 1.1), (6, 7, 0.9), (7, 5, 1)]


        result = obj.removeCircle(input_3)
        print('INPUT:',input_3)
        print('OUTPUT',result)
        return self.assertEqual(result, expected_output_3)

if __name__ == '__main__':
    unittest.main()