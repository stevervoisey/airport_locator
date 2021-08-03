

PROJECT_DIRECTORY = "D:\\WORK\\Development\\Python\\Code\\L3Harris\\AirportLocatorProject"
TEST_DIRECTORY = "airport_locator\\test"
TEST_DATA_GOOD = F"{PROJECT_DIRECTORY}\\{TEST_DIRECTORY}\\test_data_good.csv"

# 'getcwd' works in pycharm, always resolves to top level project directory, but will fail from
# command line as dependent on execution directory.
# Only safe option is full path, but this will fail/need to be re-defined, for a new environment.
# PROJECT_DIRECTORY = directory_path = os.getcwd()
