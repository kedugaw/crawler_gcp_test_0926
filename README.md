# crawler_gcp_test_0926

## 測試練習用
* 多人協作角色分配說明
  * 組員A : 提供自己的 GCP 環境，讓參與專案的組員共同使用
    * (建立Project -> Storage -> Firestore -> Cloud Shell)，最終開一個GCE
  * 組員B : 作為程式的架構者，提供程式雛形
    * 提供給組員A，將其建立在 GCP上
    * 提供給各組員，讓大家都可以 Clone 回去且進行各局部功能的開發，並且 Push 回組員B 的 git repo
  * 組員C : 負責撰寫自己分配到的局部功能，開發完成後Push 回組員B 的 git repo
  * 其他組員 : 同組員C
* 組員A 的 GCP Cloud Shell 上的程式必須為**最新版**。
   * 每次要進行 Cloud Build 前須先 Pull 程式，再進行 Cloud Run


## 重要的設定說明
* **組員A 在 GCP上的專案設定**
  * IAM 與管理 -> 身分與存取權管理 -> +新增
    * 新增主體 (輸入組員的email)
    * 選擇角色 (編輯者，可查看、建立、更新及刪除大部分的 Google Cloud 資源。瀏覽所含權限清單)
* **組員B 在 GitHub上該repo的設定**
  * 設定該 repo 的 Collaborators 功能
    * Settings \ Collaborators \ Manage access \ [Add people]
    * 新增成員 (輸入組員的 GitHub 帳號)
    * 成員記得要去收信，點選信中的連結 You can accept or decline this invitation. ，並且回覆 [Accept invitation]
  - Collaborators 類似於 Team 模式，repo 的擁有者可以直接新增合作者到自己的倉庫中，讓合作者擁有幾乎等同擁有者的許可權。
* **每個組員的前置設定**
  
## 練習在 GCP Cloud Shell Editor 進行Git, GitHub 多人協作開發 (待改0926)  
* 前提假設: 組員本機環境為 **Win**
* 組員A
  * 把組員B 的 git repo Clone 回自己的本機
  * 建立自己的虛擬環境
  * 初始化開發環境
    * 安裝套件(pip install -r "requirements.txt")
    * **新增一支程式 crawler_ptt.py**
    * 本機執行該程式沒問題後，產出新的一份 requirements.txt(沒有使用到其它套件則不必產生)
  * 把自己的負責的程式 Push 回組員B 的 git repo
* 組員B
  * 在本機建立虛擬環境
  * 初始化開發環境
    * 安裝套件(產出 requirements.txt ， pip freeze > requirements.txt)
    * 新增檔案 .gitignore 和 README.md
  * 先把乾淨的環境 Push 上自己的 git repo
  * 把自己 repo Pull 下來後，**新增一支程式 crawler_static.py**，再 Push 回自己的 repo
* 組員C,其他組員
  * 把組員B 的 git repo Clone 回自己的本機
  * 建立自己的虛擬環境
  * 初始化開發環境
    * 安裝套件(pip install -r "requirements.txt")
    * **新增一支程式 crawler_rate.py**
    * 本機執行該程式沒問題後，產出新的一份 requirements.txt(沒有使用到其它套件則不必產生)
  * 把自己的負責的程式 Push 回組員B 的 git repo


## 練習在 VSCode 進行Git, GitHub 多人協作開發
* 組員A
  * 把組員B 的 git repo Clone 回自己的本機
  * 建立自己的虛擬環境
  * 初始化開發環境
    * 安裝套件(指令為 pip install -r "requirements.txt")
    * **新增一支程式 crawler_ptt.py**
    * 本機執行該程式沒問題後，產出新的一份 requirements.txt(新程式沒有使用到其他套件則不必產生)
  * 把自己的負責的程式 Push 回組員B 的 git repo
* 組員B
  * 在本機建立虛擬環境
  * 初始化開發環境
    * 安裝套件(產出 requirements.txt ， 指令為 pip freeze > requirements.txt)
    * 新增檔案 .gitignore 和 README.md
  * 先把乾淨的環境 Push 上自己的 git repo
  * 把自己 repo Pull 下來後，**新增一支程式 crawler_static.py**，再 Push 回自己的 repo
* 組員C,其他組員
  * 把組員B 的 git repo Clone 回自己的本機
  * 建立自己的虛擬環境
  * 初始化開發環境
    * 安裝套件(指令為 pip install -r "requirements.txt")
    * **新增一支程式 crawler_rate.py**
    * 本機執行該程式沒問題後，產出新的一份 requirements.txt(新程式沒有使用到其他套件則不必產生)
  * 把自己的負責的程式 Push 回組員B 的 git repo
