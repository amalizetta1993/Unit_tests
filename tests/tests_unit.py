import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from main import *

class TestDisciplineTeacher(unittest.TestCase):
    teacher4 = DisciplineTeacher('Иван Петров', 'РГУ', 4, 'Химия', 'Учитель 1 категории')
    teacher5 = DisciplineTeacher('Глеб Орлов', 'МГУ', 10, 'География', 'Завуч')
    teacher6 = DisciplineTeacher('Юлия Савина', 'РГРТУ', 1, 'Физика', 'Учитель') 
    
    def test_1_init(self):
        self.assertEqual(len(Teacher.teachers), 3)
        
    def test_2_get_name(self):
        self.assertEqual(self.teacher4.get_name(), 'Иван Петров')
        
    def test_3_get_education(self):
        self.assertEqual(self.teacher4.get_education(), 'РГУ')
        
    def test_4_get_experience(self):
        self.assertEqual(self.teacher4.get_experience(), 4)
        
    def test_5_set_experience(self):
        self.teacher4.set_experience(5)
        self.assertEqual(self.teacher4.get_experience(), 5)
        
    def test_6_teacher_data(self):
        self.assertEqual(' '.join(self.teacher4.get_teacher_data()), 'Иван Петров, образование РГУ, опыт работы 5 года. Предмет Химия, должность Учитель 1 категории')
    
    def test_7_get_discipline(self):
        self.assertEqual(self.teacher4.get_discipline(), 'Химия')
        
    def test_8_get_job_title(self):
        self.assertEqual(self.teacher4.get_job_title(), 'Учитель 1 категории')
        
    def test_9_set_job_title(self):
        self.teacher4.set_job_title('Директор')
        self.assertEqual(self.teacher4.get_job_title(), 'Директор')
        
    def test_10_add_mark(self):
        self.assertEqual(' '.join(self.teacher4.add_mark('Ангелина', 5)), 'Иван Петров поставил оценку 5 студенту Ангелина. Предмет: Химия')
        
    def test_11_remove_mark(self):
        self.assertEqual(' '.join(self.teacher4.remove_mark('Вова', 3)), 'Иван Петров удалил оценку 3 студенту Вова. Предмет: Химия')       
        
    # def test_12_dismissal_teachers(self):
    #     Teacher.dismissal_teachers('Глеб Орлов')
    #     self.assertEqual(Teacher.teachers, ['Иван Петров', 'Юлия Савина']) 


        