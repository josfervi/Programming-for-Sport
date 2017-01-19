# https://www.interviewbit.com/problems/allocate-books/

# practically the same as painters parition problem

from math import ceil

# P - list containing the number of pages in each book
# n - len(P) - the number of books
# S - sum(P)
# m - number of students

# O( n * lgS )

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    # given len(P) books where book i has P[i] pages,
    # allocate all the books to m students
    # s.t.
    #     each student receives at least one book
    #     a student is aloted contiguous books
    #     the max number of pages that a student is aloted is minimized
    def books(self, P, m):
        
        num_books= len(P)
        num_students= m
        
        if num_students > num_books or num_students == 0:
            # there are not enough books to go around
            # s.t. each student gets at least one book
            return -1
        
        if num_students == num_books:
            return max(P)
        
        sum_= sum(P)
        max_= max(P)
        avg=  int( ceil( float(sum_) / num_students ) )
        
        best_conceivable_result=  max( max_, avg )
        worst_conceivable_result= sum_
        
        c_min, c_max = best_conceivable_result, worst_conceivable_result
        
        best_result_so_far= -1
        
        while c_min <= c_max:
            
            candidate= (c_min+c_max)/2
            
            if self.is_possible_to_allocate(P, m, candidate):
                best_result_so_far= candidate
                
                c_max= candidate - 1
            else:
                c_min= candidate + 1
        
        return best_result_so_far
    
    # returns true if it is possible to allocate len(P) books
    # (book i has P[i] pages) to m students
    # such that every student is assigned <= max_allocation number of pages
    def is_possible_to_allocate(self, P, number_of_students_available, max_allocation):
        
        number_of_students_used_so_far= 1
        current_allocation= 0
        
        for num_of_pages in P:
            
            if current_allocation + num_of_pages <= max_allocation:
                # assign current book which has num_of_pages pages
                # to the current student
                current_allocation+= num_of_pages
                continue
            
            # assign current book to the next student
            number_of_students_used_so_far+= 1
            current_allocation= num_of_pages
            
            if number_of_students_used_so_far > number_of_students_available:
                return False
        
        return True