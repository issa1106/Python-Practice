import numpy as np
import matplotlib.pyplot as plt
import seaborn
from bokeh.plotting import figure, output_file, show
# 因版本關係Bokeh的用法請至bokeh.pydata.org的使用指引查詢

normal_samples = np.random.normal(size=10000)
plt.hist(normal_samples)
plt.show()  # 直接顯示
plt.savefig(fname="myhist.png", format="png")  # 輸出存成圖檔

seaborn.distplot(normal_samples)
# seaborn可用plt.show()顯示

draw_bk = figure(plot_width=400, plot_height=400)
draw_bk.vbar(x=[1, 2, 3], width=0.5, bottom=0, top=[1.2, 2.5, 3.7])
show(draw_bk)
