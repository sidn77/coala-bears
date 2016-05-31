from bears.python.BanditBear import BanditBear
from tests.LocalBearTestHelper import verify_local_bear

good_file = 'print("good!")'

bad_file = 'assert True  # Never fails'

BanditBearTest = verify_local_bear(
    BanditBear,
    valid_files=(good_file,),
    invalid_files=(bad_file,),
    tempfile_kwargs={"suffix": ".py"},
)
