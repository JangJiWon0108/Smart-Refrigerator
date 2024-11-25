from langchain_openai import ChatOpenAI              # OpenAI
from langchain_upstage import ChatUpstage            # Upstage
from langchain_core.prompts import PromptTemplate

# llm 불러오는 함수
def f_import_llm():
    # llm 모델 불러오기
    llm=ChatUpstage(api_key="up_dQAX6wpLM1ls3ctIhn8VXTjFMyuNb")
    
    return llm

# 프롬프트 불러오는 함수 - 초기 냉장고 물품으로 레시피 추천
def f_import_prompt_init():
    prompt_template="""
        질문 : {question}
        당신은 레시피를 추천해주는 최고의 전문가 입니다.
        quesion은 사용자의 냉장고에 있는 재료(물품)으로 주어집니다.

        재료(물품) 기반으로, 적절한 레시피를 하나 추천해 주세요.

        1. 이모지를 최대한 많이 사용해 주세요.
        """
    prompt=PromptTemplate(
        template=prompt_template,
        input_variable=["question"]
    )

    return prompt

# 프롬프트 불러오는 함수 - 그냥 질문에 대해 레시피 추천
def f_import_prompt_no_init():
    prompt_template="""
        질문 : {question}
        당신은 레시피를 추천해주는 최고의 전문가 입니다.
        사용자 질문에 대한 레시피를 정확하고 자세하게 알려주세요.

        만약, 레시피나 음식에 대한 질문이 아니라면, 레시피나 음식에 대해 질문하도록 유도하세요.

        1. 이모지를 최대한 많이 사용해 주세요.
        """
    prompt=PromptTemplate(
        template=prompt_template,
        input_variable=["question"]
    )

    return prompt