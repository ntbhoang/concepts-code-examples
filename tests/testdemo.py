import os
import time
from enum import Enum

from dotenv import load_dotenv
from playwright.sync_api import Page, expect


class EnvironmentVars(str, Enum):
    TARGET_ENV = 'target_env'

    def __str__(self):
        return str(self.value)


target_env = os.getenv(EnvironmentVars.TARGET_ENV)
file_path = os.path.abspath('/Users/hoangntb/PycharmProjects/concepts-code-examples/env_files/.env.')

load_dotenv(f'{file_path}{target_env}')
time.sleep(2)


def test_abc(page: Page):
    print(os.getenv('REGISTER_URL'))
    page.goto(os.getenv('REGISTER_URL'))
    expect(page).to_have_title('ABC')





