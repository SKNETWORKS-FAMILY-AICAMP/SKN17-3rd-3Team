from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS, Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_huggingface import HuggingFacePipeline
# from langchain_chroma import Chroma
import os

HF_TOKEN = os.getenv('HF_TOKEN')

path = 'vectorstore/faiss3/tag_place_split'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device

template = '''당신은 대한민국 관광지에 대해 잘 알려주는 친절한 챗봇입니다.
주어진 Context에 있는 여러 장소 정보를 **종합하여, 질문에 가장 적합한 하나의 통일된 문단으로** 답변을 생성하세요.
Context에서 확인할 수 없는 질문이라면 "모른다"고 답변해야 합니다.
사용자가 "서울"처럼 지역을 특정한 경우, Context에서 region이 일치하는 document에서만 답변을 생성하세요.
답변은 정확히 3줄의 완결된 문장으로 반환하고 각 문장의 끝은 마침표('.')로 끝내세요.
장소이름 + 특징을

# Question:
{query}
# Context:
{context}

# Answer:
'''
def get_response(query):

    # 1. 임베딩 모델 로드
    embeddings_model = HuggingFaceEmbeddings(
        model_name = 'all-MiniLM-L6-v2',
        model_kwargs = {'device':'cpu'},
        encode_kwargs = {'normalize_embeddings':True}
    )

    # 2-1. local에서 FAISS load
    vectorstore = FAISS.load_local(
        folder_path=path,
        embeddings=embeddings_model,
        allow_dangerous_deserialization=True
    )

    # # 2-2. local에서 Chroma load
    # vectorstore = Chroma(
    #     persist_directory=path,
    #     embedding_function=embeddings_model
    # )

    # 3. retriever 설정
    # mmr: query 검색 시 중복되는 문서 피하는 방법
    retriever = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k':10})

    # 4. chain 생성
    # 4-1. prompt
    # 일단 단일 prompt로 시작
    prompt_template = PromptTemplate.from_template(template)

    # 4-2. llm
    # sllm 모델 생성
    model_name = "trillionlabs/Trillion-7B-preview"

    sllm = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype=torch.bfloat16,
    ).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    llm_pipe = pipeline(
        'text-generation',
        model=sllm,
        tokenizer=tokenizer,
        pad_token_id=tokenizer.eos_token_id,
        max_new_tokens=96,
        repetition_penalty=1.2,
        return_full_text=False,
        temperature=0.2
    )

    llm = HuggingFacePipeline(pipeline=llm_pipe)
    retrieval = retriever.invoke(query)
    chain = (
    {'context': retriever, 'query': RunnablePassthrough()}
    | prompt_template 
    | llm 
    | StrOutputParser())

    response = chain.invoke(query)
    res = response.split('.')
    tmp = ''
    for i, sen in enumerate(res):
        if i >= 3: break
        if (i >= 2) and (sen=='' or '\n' in sen): break
        sen = sen.strip('\n').strip()

        tmp += sen + '. '
        
    return tmp, retrieval

if __name__=="__main__":
    
    # print('retrieval documents')
    queries = ["아기 데리고 같이 갈 만한 관광지와 장소에 대한 설명을 같이 해줘.",
"반려동물과 함께 갈 수 있는 서울에 있는 관광지 추천해줘.",
"부모님과 함께 드라이브할 수 있는 코스 추천해줘.",
"혼자서 놀기에 적합한 부산 여행지 추천해줘.",
"애인과 함께 데이트할 만한 강원도 여행지 추천해줘.",
"아이와 함께 체험활동을 할 수 있는 관광지 추천해줘.",
"역사탐방하기에 좋은 관광지 코스 추천해줘.",
"경상남도 사진찍기 좋은 곳 추천해줘.",
"전라남도 피크닉하기 좋은 곳 추천해줘.",
"경기도 산책하기 좋은 장소 추천해줘.",]
    
    for q in queries:
        res, _ = get_response(q)

        print('query:', q)
        print('response:', res)
        print()
