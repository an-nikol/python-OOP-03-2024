from project_1.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student_1 = Student("Polina", {"Criminal Law": [" n1", "n2"], "Tax Law": ["n4", "n5"]})
        self.student_2 = Student("Ari")

    def test_init_with_courses(self):
        self.assertEqual("Polina", self.student_1.name)
        self.assertEqual({"Criminal Law": ["n1", "n2"], "Tax Law": ["n4", "n5"]}, self.student_1.courses)

    def test_init_without_courses(self):
        self.assertEqual("Ari", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

    def test_enroll_existing_course(self):
        result = self.student_1.enroll("Criminal Law", ["n4", "n5"], "N")

        self.assertEqual({"Criminal Law": ["n1", "n2", "n4", "n5"], "Tax Law": ["n4", "n5"]}, self.student_1.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

        result = self.student_1.enroll("Criminal Law", ["n6", "n7"], "Y")

        self.assertEqual({"Criminal Law": ["n1", "n2", "n4", "n5", "n6", "n7"], "Tax Law": ["n4", "n5"]},
                         self.student_1.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_when_not_existing_course_with_y(self):
        result = self.student_1.enroll("Property Law", ["n1", "n2"], "Y")

        self.assertTrue("Property Law" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual(["n1", "n2"], self.student_1.courses["Property Law"])

    def test_enroll_when_not_existing_course_with_empty_string(self):
        result = self.student_1.enroll("Property Law", ["n1", "n2"])

        self.assertTrue("Property Law" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual(["n1", "n2"], self.student_1.courses["Property Law"])

    def test_enroll_add_not_existing_course_and_not_adding_notes(self):
        result = self.student_1.enroll("Contract Law", ["n1", "n2"], "N")

        self.assertTrue("Contract Law" in self.student_1.courses)

        self.assertEqual([], self.student_1.courses["Contract Law"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("Contract Law", ["n6", "n7"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_successful_to_existing_course(self):
        result = self.student_1.add_notes("Criminal Law", ["n3", "n4"])

        self.assertEqual({"Criminal Law": ["n1", "n2", ["n3", "n4"]], "Tax Law": ["n4", "n5"]}, self.student_1.courses)

        self.assertEqual("Notes have been updated", result)

    def test_leave_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Contract Law")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_successful(self):
        self.student_1.leave_course("Tax Law")

        self.assertEqual({"Criminal Law": ["n1", "n2"]}, self.student_1.courses)
        self.assertNotIn("Tax Law", self.student_1.courses)

if __name__ == "__main__":
    unittest.main()