import pandas as pd
food_data = pd.read_excel('data/음식 라벨링 감정 7개.xlsx')

food_data_list = []
for w, foodlabel in zip(food_data['음식'], food_data['성분'])  :
    fooddata = []
    fooddata.append(w)
    fooddata.append(str(foodlabel))

    food_data_list.append(fooddata)

food_line1 = food_data['감정'].str.contains('공포')
food_line2 = food_data['감정'].str.contains('당황')
food_line3 = food_data['감정'].str.contains('분노')
food_line4 = food_data['감정'].str.contains('슬픔')
food_line5 = food_data['감정'].str.contains('기쁨')
food_line6 = food_data['감정'].str.contains('차분')
food_line7 = food_data['감정'].str.contains('불안')

save_food_line1 = food_data[food_line1]
save_food_line2 = food_data[food_line2]
save_food_line3 = food_data[food_line3]
save_food_line4 = food_data[food_line4]
save_food_line5 = food_data[food_line5]
save_food_line6 = food_data[food_line6]
save_food_line7 = food_data[food_line7]

# 제목-가수 출력
# final_food1 = save_food_line1[['제목','가수']]
# final_food2 = save_food_line2[['제목','가수']]
# final_food3 = save_food_line3[['제목','가수']]
# final_food4 = save_food_line4[['제목','가수']]
# final_food5 = save_food_line5[['제목','가수']]
# final_food6 = save_food_line6[['제목','가수']]
# final_food7 = save_food_line7[['제목','가수']]

# 제목-가수-youtube 링크 출력
final_food1 = save_food_line1[['음식','성분','Photo_link']]
final_food2 = save_food_line2[['음식','성분','Photo_link']]
final_food3 = save_food_line3[['음식','성분','Photo_link']]
final_food4 = save_food_line4[['음식','성분','Photo_link']]
final_food5 = save_food_line5[['음식','성분','Photo_link']]
final_food6 = save_food_line6[['음식','성분','Photo_link']]
final_food7 = save_food_line7[['음식','성분','Photo_link']]