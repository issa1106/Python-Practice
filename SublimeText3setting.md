這一切的起源自於我跟朋友說我電腦裝好最夯的程式語言[Python](https://www.python.org/)了，
於是身為學統計的工程師朋友就貼給我[手寫辨識](https://ithelp.ithome.com.tw/articles/10187912)讓我玩玩看，然後我就從零開始跟著code，
所以這篇很適合剛接觸的新手看。

首先，要安裝可以編輯打字的介面，也就是IDE，
所以我看了[推薦10款最好用的Python IDE](https://read01.com/zh-tw/Dx5BKQ.html)，
一開始選中了Pycharm，
安裝玩的結果光是開個檔案就慢到想睡覺了。

後來看到[Sublime Text](https://www.sublimetext.com/)看起最簡潔，就選擇改安裝它了，
殊不知最簡潔也代表很多套件都要自己安裝，
這也是網路上很多人推薦Sublime的原因，
因為它可以隨個人喜好改變，隨各種程式語言或檔案格式改變，
而且我用一週就愛上它了，你能不用嗎?

再來，跟著[懶人包安裝教學](http://killer0001.blogspot.tw/2017/01/python-sublime-text-3.html)

1. 安裝套件控制器，於上列選單中Tools中的，install Package Control

   (也有另外一種方法，為View中的，Show Console顯示主控台並貼上[PackageControl](https://packagecontrol.io/installation)中的文字)

2. 叫出套件控制器開始安裝套件，並選擇Install Package

   ConvertToUTF8 為可在編輯區正常顯示中文的套件

   Anaconda 為輔助coding Python語言的套件，包括顯示、編碼等等

好了，到這邊應該可以簡單的執行測試一下是否運作正常。
然後若套件有什麼問題，可至Preferences中的Package settings中做設定

像我就發生一個問題，我無法import numpy，也就是上述教學文章中資料科學要用到的，
於是我爬了一下文，發現必須要使用Python with Anaconda

然後真的很感謝[Stack Overflow](https://stackoverflow.com/)有好多問題上面都有討論，雖然是英文，有點硬就是了

於是我去下載[Anaconda](https://www.anaconda.com/download/)，然後要裝32-bit版本的 (忘記在哪看到64-bit的python run什麼有問題了)

安裝完發現它是完整環境包，裡面有配備Python跟IDE，

就像買了份日本定食，只買壽司，發現送主餐肉排、味增湯和小菜

當然主餐肉排就是我們的Python，

然後味增湯是名為Spyder的IDE(朋友後來說他工作是用這個開發環境)，

還有小菜Jupyter Notebook(教學文章中所使用)，

也就是說，若你不想用Sublime Text當編譯器，只想跟著教學文章練習，

請直接安裝Anaconda就可以了。

問題就來了，那我用Sublime Text 3 編譯時，到底是用哪個版本Python

於是我把最一開始從Python下載的那個版本刪除了

接著用Sublime開起.py檔就會跳出有關Anaconda的錯誤訊息

檢查了一下，真的是python_interpreter的問題

嘗試了解決方法如下：

1. 懶人包教學文章中的電腦系統環境變數Path改為Anaconda的Python路徑

   (查詢方法開啟Anaconda環境包中的Prompt，輸入where python查詢)

2. 打開Sublime的Package settings將Anaconda的python_interpreter的路徑也更改

   (Sublime中可用查詢，點選左下角的小框框Switch Panel點選Find)

3. 選單中Tools，Build System建立的新的編碼系統New Build System，寫上如下面的程式碼

   (cmd中的路徑設定為Python with Anaconda電腦中的位置，請依個別狀況調整)

   (經測試encoding中的cp950可以印出中文，如設定UTF-8不會有錯誤訊息但無法print輸出中文)

   (Shell設定為true可顯示出圖片，統計圖表show時用的)

         {

           "cmd": ["C:\\ProgramData\\Anaconda3\\python.exe", "-u", "$file"],
   
           "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
   
            "selector": "source.python",
   
           "encoding": "cp950"

           "shell": "true"
   
          }
   
最後，如果開啟.py檔還有Anaconda的錯誤訊息，但程式可以順利Build，無錯誤訊息，
可以依照它顯示的訊息內容，在Package settings中的此顯示設定忽略，
就可以開始你的Python coding，祝玩得愉快。

有設定上的問題，可以參考影片: [環境變數設定](https://www.youtube.com/watch?v=fd4shj64xVU)、[New Build System](https://youtu.be/rIl0mmYSPIc)
