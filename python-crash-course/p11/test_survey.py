import pytest
from survey import AnonymousSurvey

def test_store_single_response():
    """ 测试单个答案会被妥善地存储 """
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')

    assert 'English' in language_survey.responses



def test_store_three_responses():
    """ 测试三个答案会被妥善地存储 """
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

# 使用 fixture 夹具来创建调查实例

@pytest.fixture
def language_survey():
    """ 一个存储调查问卷的实例 """
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """ 测试单个答案会被妥善地存储 """
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
    

def test_store_three_responses(language_survey):
    """ 测试三个答案会被妥善地存储 """
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses




