import pandas

name = ["幸平創真", "薙切繪里奈", "田所惠", "巧·阿爾迪尼",
		"一色慧", "水戶郁魅", "新戶緋沙子", "小林龍膽"]
Birthday = ["11/6", "3/23", "12/19", "7/19",
			"5/2", "5/4","10/14", "10/12"]
Height = [171, 162, 154, 168, 180, 163, 161, 171]
# 建立第一個資料表
character_dict = {
	"name": name, 
	"Birthday": Birthday,
	"Height": Height
}
character_df = pandas.DataFrame(character_dict)

# 建立第二個資料表
name = ["幸平創真", "田所惠", "巧·阿爾迪尼",
		"一色慧", "水戶郁魅", "新戶緋沙子", "小林龍膽"]
Expertise = ["日式定食,法國料理", "蔬菜", "義大利料理",
			 "日式料理", "肉", "中醫藥膳", "稀有食材"]
char_expt_dict = {"name": name, "expertise": Expertise}
char_expt_df = pandas.DataFrame(char_expt_dict)

# merge預設為inner join, 可用參數how=指定合併方法
char_join = pandas.merge(character_df, char_expt_df, how="left")
print(char_join)

# 新增一筆資料 串聯concatenate
momo_dict = {"name": ["茜久保桃"], "expertise": ["甜點"]}
momo_pd = pandas.DataFrame(momo_dict, index=[7])  # 設定index，否則為0
char_expt_n_df = pandas.concat([char_expt_df,momo_pd])
print(char_expt_n_df)

# 新增一欄 觀測值 串聯concatenate 參數axis=1
Bloodtype = ["B", "AB", "O", "A", "AB", "B", "A", "B"]
blood_dict = {"bloodtype": Bloodtype}
blood_df = pandas.DataFrame(blood_dict)
char_data = pandas.concat([character_df, blood_df], axis=1)
print(char_data)

# 轉置Transpose
char_expt_t_df = char_expt_df.stack()
print(char_expt_t_df)

# 分箱Binning用cut()
bins = [0, 165, float("inf")]
group_name = ["矮矮", "高個"]
character_df.ix[:, "Heightcut"] = pandas.cut(
	character_df.ix[:, "Height"], bins, labels=group_name)
print(character_df)

# 輸出資料表
char_data.to_csv("character.csv", index=False)
