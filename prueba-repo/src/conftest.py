import pytest
import selenium.webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', action='store',default='chrome',
                     help ='setup browser: Chrome')


@pytest.fixture
def browser(request):
  sel_browser = request.config.getoption("--browser")
  if sel_browser == 'chrome':
   #b = selenium.webdriver.Chrome()
   b = selenium.webdriver.Chrome(ChromeDriverManager().install())
  elif sel_browser == 'headless':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(options=opts)
  elif sel_browser == 'firefox':
    b = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
  else:
    raise Exception(f'Browser '+sel_browser+'  is not supported')

  b.implicitly_wait('20')
  yield b
  b.quit()



