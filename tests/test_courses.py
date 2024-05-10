import os
from dotenv import load_dotenv

from gradescopeapi._classes._connection import GSConnection

# load .env file
load_dotenv()
GRADESCOPE_CI_STUDENT_EMAIL = os.getenv("GRADESCOPE_CI_STUDENT_EMAIL")
GRADESCOPE_CI_STUDENT_PASSWORD = os.getenv("GRADESCOPE_CI_STUDENT_PASSWORD")
GRADESCOPE_CI_INSTRUCTOR_EMAIL = os.getenv("GRADESCOPE_CI_INSTRUCTOR_EMAIL")
GRADESCOPE_CI_INSTRUCTOR_PASSWORD = os.getenv("GRADESCOPE_CI_INSTRUCTOR_PASSWORD")
GRADESCOPE_CI_TA_EMAIL = os.getenv("GRADESCOPE_CI_TA_EMAIL")
GRADESCOPE_CI_TA_PASSWORD = os.getenv("GRADESCOPE_CI_TA_PASSWORD")


def get_account(account_type="student"):
    """Creates a connection and returns the account for testing"""
    connection = GSConnection()

    match account_type.lower():
        case "student":
            connection.login(
                GRADESCOPE_CI_STUDENT_EMAIL, GRADESCOPE_CI_STUDENT_PASSWORD
            )
        case "instructor":
            connection.login(
                GRADESCOPE_CI_INSTRUCTOR_EMAIL, GRADESCOPE_CI_INSTRUCTOR_PASSWORD
            )
        case "ta":
            connection.login(GRADESCOPE_CI_TA_EMAIL, GRADESCOPE_CI_TA_PASSWORD)
        case _:
            raise ValueError(
                "Invalid account type: must be 'student' or 'instructor' or 'ta'"
            )

    return connection.account


def test_get_courses_student():
    # fetch student account
    account = get_account("student")

    # get student courses
    courses = account.get_courses()

    assert courses["instructor"] == {} and courses["student"] != {}


def test_get_courses_instructor():
    # fetch instructor account
    account = get_account("instructor")

    # get instructor courses
    courses = account.get_courses()

    assert courses["instructor"] != {} and courses["student"] == {}


def test_get_courses_ta():
    # fetch ta account
    account = get_account("ta")

    # get ta courses
    courses = account.get_courses()

    assert courses["instructor"] != {} and courses["student"] != {}
