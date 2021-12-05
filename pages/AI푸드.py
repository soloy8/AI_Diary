"""This page is for searching and viewing the list of awesome resources"""
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
from webpage.web_food_predict import *

def write():
    #위 구문 안쓰면 오류임

    input_data = st.text_area("식사 전의 기분을 입력하세요!")

    # 여기서 input_data를 감정분석 프로그램에 넘겨주고 그 인수를 받아와야 한다. - 해결!

    Push_listen_button = st.button("AI 음식 추천")
    if Push_listen_button:
        result,link = predict(input_data)
        st.success(result)
        from PIL import Image
        st.image(src=link, width=700)  # 400잡으면 전체 400축소됨.

    st.write(
    """
    
    <AI FOOD의 이론적 배경>

    광운대 산업심리학과 이상희 교수팀 연구논문 '대학생들의 정서에 따른 컴포트 푸드의 차이:성차를 중심으로(2014)'
    
    행복할 때 찾는 음식은?
    남학생 1위 고기, 2위 술
    여학생 1위 치킨, 2위 피자, 스파게티
    
    즐거울 때 찾는 음식은?
    남학생 1위 술, 2위 치킨
    여학생 1위 치킨, 2위 아이스크림
    
    슬플 때 찾는 음식은? 
    남학생 1위 술, 2위 초콜릿
    여학생 1위 초콜릿, 2위 술 
    
    화날 때 찾는 음식은?
    남학생 1위 술, 2위 매운음식
    여학생 1위 매운음식, 2위 초콜릿
    
    c.f. 국민건강증진법 시행령 및 시행규칙 개정안 6월 30에 의거 청소년 대상 주류광고 불가입니다.
    만19세 이상의 제한적 배포가 어렵기에 주류광고는 제거하겠습니다.
    
    마음 불안할 때 먹으면 좋은 ‘음식’ 4
    이해나 헬스조선 기자 | 김명주 헬스조선 인턴기자
    
    바나나
    바나나에 들어있는 트립토판 성분은 '행복호르몬' 세로토닌 생성을 돕는다. 트립토판은 필수 아미노산의 일종으로 음식을 통해 섭취해야 하는데, 행복감을 느끼게 하는 세로토닌 생성에 이용된다. 이외에도 바나나에 함유된 마그네슘, 칼슘은 근육의 긴장을 이완해 마음을 차분히 가라앉힌다. 또한 비타민B군이 풍부해 피로 해소, 스트레스 완화에 좋다.
    
    호두
    뇌 건강을 향상시키는 호두는 불안할 때 먹어도 도움이 된다. 호두에는 식물성 오메가3 지방산인 '리놀렌산'이 다른 견과류보다 많이 들어있다. 리놀렌산은 혈압을 낮추고, 스트레스와 불안감을 해소하는 효과가 있다. 마그네슘이 풍부해 긴장을 이완하고, 칼륨과 비타민B1이 있어 피로를 해소해주기도 한다. 호두 섭취가 우울증 유병률을 낮추는 데 도움이 된다는 연구 결과도 있다. 미국 캘리포니아대 연구팀이 약 2만6000명을 대상으로 조사한 결과, 평소 호두를 자주 섭취한 그룹은 견과류를 아예 섭취하지 않은 그룹보다 우울증 점수가 26% 낮았다.
    
    연어
    연어에는 피로 해소를 돕는 비타민B군과 오메가3 지방산이 풍부하다. 오메가3 지방산은 스트레스를 완화하고, 세로토닌의 분비량을 늘려준다. 실제 미국 존스홉킨스대·일본 도쿄대 공동 연구팀은 오메가3 지방산이 함유된 어유(魚油) 보충제가 외상후스트레스장애 예방과 만성 스트레스 완화에 도움된다는 연구 결과를 발표하기도 했다. 오메가3 지방산은 연어 외에도 고등어, 꽁치와 같은 등푸른생선에 많이 함유돼 있다.
    
    허브티
    허브티를 마시는 것도 불안감 완화에 도움이 된다. 라벤더는 심신 안정 효과가 있어 대체의학에서 불면증, 우울증 증상 완화에 사용하는 것으로 알려졌다. 라벤더의 향을 내는 '리날룰' 성분이 불안 증세를 완화하는 데 효과가 있다는 일본 대학 연구팀의 동물 실험 결과가 있다. 라벤더를 따뜻한 티로 우려 마시면 좋다. 캐모마일 차를 마셔도 도움이 된다. 캐모마일은 신경안정 효과가 있어 수면 보조제로 널리 활용된다. 대만 푸잉대 연구팀에 따르면 산모들을 대상으로 실험한 결과, 캐모마일 차를 매일 2주간 마신 그룹은 그렇지 않은 그룹보다 우울 증상이 적었고 수면의 질이 높았다.


    """



    )


if __name__ == "__main__":
    write()