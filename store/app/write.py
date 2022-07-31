from app.models import *
from store.app.models import Userorm
import datetime
def write_instructor():
    #Add instructors
    #Create a User
    user_john = Userorm(first_name='John', last_name='Doe', dob=datetime(1962, 7, 16))
    user_john.save()
    instructor_John = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor _john to be user_john
    instructor_John.user = user_john
    instructor_John.save()
    
    instructor_yan = Instructor(first_name='Yan', last_name='Luo', dob=datetime(1962, 7, 16), full_time=True, total_learners=30050)
    instructor_yan.save()

    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=datetime(1992, 1, 2), full_time=False, total_learners=10040)
    instructor_joy.save()
    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=datetime(1982, 5, 2), full_time=True, total_learners=2002)
    instructor_peter.save()
    print("Instructor objects all saved... ")
    