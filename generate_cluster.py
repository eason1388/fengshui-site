from pathlib import Path
from html import escape

root = Path(r'C:/Users/eason1288/.openclaw/workspace')
sui = root / 'suiyuantang'
gen = root / 'general'
sui.mkdir(exist_ok=True)
gen.mkdir(exist_ok=True)

base = 'https://eason1388.github.io/fengshui-site'
update_date = '2026-03-18'

cluster = [
    {
        'slug': 'eight-mansions-fengshui-guide',
        'title': '陽宅風水八宅風水完整指南',
        'keyword': '陽宅風水八宅風水',
        'desc': '隨緣堂整理陽宅風水八宅風水完整觀念，串連命卦、宅卦、吉凶方位與空間配置，作為八宅風水主頁與導覽中心。',
        'faq': [
            ('八宅風水和一般居家風水差在哪裡？', '八宅風水更強調命卦、宅卦與八方位之間的對應關係，會用系統化方式看住宅與人的匹配。'),
            ('八宅風水一定要整間房子重做嗎？', '不一定，多數情況可以先從主臥、床位、書桌、爐灶與日常使用方位開始調整。'),
            ('八宅風水適合所有人嗎？', '它是一套常見且好上手的陽宅風水系統，適合想先建立判斷框架的人。')
        ],
        'sections': [
            ('前言：為什麼很多人研究陽宅風水時會先碰到八宅風水？', '陽宅風水八宅風水，是許多人接觸居家風水時最先遇到的系統之一。原因很簡單，它把原本看起來很抽象的風水觀念，轉成比較容易操作的邏輯：先分東四命、西四命，再看住宅屬於東四宅或西四宅，接著對照八個方位的吉凶，思考大門、主臥、床位、書桌與爐灶該怎麼安排。對初學者來說，這套方法至少有架構，不會一開始就被一堆名詞打到頭昏。\n\n但八宅風水並不是背完吉方凶方就萬事大吉。真正有用的地方，在於它幫你建立一個檢查住宅使用方式的框架。例如你每天最常待的地方是否落在較適合自己的方位、休息區與工作區是否彼此衝突、住宅本身的門向與居住者的命卦是否有明顯矛盾。這些才是陽宅風水八宅風水真正落地的地方。'),
            ('八宅風水的核心邏輯：人與宅都要一起看', '八宅風水不是只看房子，也不是只看人，而是把人與宅放在同一套座標裡一起看。人的部分通常會先計算命卦，住宅部分則看宅卦，然後分出延年、生氣、天醫、伏位等相對吉方，以及絕命、五鬼、六煞、禍害等相對不利方位。這種分類的好處，在於居住者可以很快知道哪些位置適合睡眠、閱讀、工作或長時間停留。\n\n不過，陽宅風水八宅風水真正實用的方式，不是把每個方位都神化，而是按重要程度排序。像是主臥、床頭、書桌朝向與大門使用感，通常就比少量裝飾品更值得優先調整。'),
            ('八宅風水可以先從哪裡開始？', '若你剛接觸陽宅風水八宅風水，可以先做四件事：第一，確認住宅大致坐向；第二，確認居住者命卦；第三，把住宅平面圖簡單劃出八方位；第四，找出你每天停留時間最長的區域。做完這些，你就已經從空談進入實作階段。\n\n很多人以為風水一定要大裝修，其實先調整床位、書桌、玄關整潔、工作位置與照明，往往就能感受到差異。八宅風水最大的價值，不在於一次改到滿分，而在於讓你知道應該先改哪裡。'),
            ('結論：把八宅風水當成居住秩序工具，比當神奇公式更有用', '總結來說，陽宅風水八宅風水之所以流傳多年，並不是因為它神祕，而是因為它提供了一套能把空間、使用習慣與個人狀態串起來的判斷方法。若你把它當成一種整理生活秩序的工具，而不是僵硬背誦吉凶口訣，會更容易真的用得上。接下來你可以沿著這組文章，分別看命卦、方位、床位、大門與主臥配置，會更好消化。')]
    },
    {
        'slug': 'eight-mansions-fengshui-calculation', 'title': '八宅風水怎麼算', 'keyword': '八宅風水怎麼算', 'desc': '整理八宅風水怎麼算的基礎流程，包含命卦、宅卦、方位劃分與常見計算盲點。',
        'faq': [('八宅風水怎麼算最先要做什麼？', '先確認出生年份計算命卦，再確認住宅坐向，這兩步是八宅風水怎麼算的起點。'), ('沒有精準羅盤能算八宅風水嗎？', '可以先做初步判斷，但若要更細緻，仍建議用可靠工具確認坐向。'), ('八宅風水怎麼算會因男女不同嗎？', '傳統命卦計算方式確實會區分男女，因此要依正確公式處理。')],
        'sections': [('前言：八宅風水怎麼算，為什麼很多人一開始就算亂？', '八宅風水怎麼算，是很多人研究陽宅風水八宅風水時第一個卡住的地方。因為只要命卦算錯、住宅坐向看反，後面所有吉凶方位都會跟著偏掉。很多網路文章只丟出簡短口訣，卻沒有提醒你哪裡最容易出錯，結果大家算得很勤，方向卻完全反著來。\n\n實際上，八宅風水怎麼算可以拆成很清楚的流程：先用出生年份計算命卦，再確認住宅坐向得到宅卦，接著把平面圖對應八方位，最後再把常用空間放進去看。這樣一層一層做，比硬背一堆表格有效得多。'), ('第一步：命卦計算與東四命、西四命區分', '八宅風水怎麼算的第一步，通常是確認居住者的命卦。傳統算法會依出生年份與性別進行計算，再得出屬於東四命或西四命。這一步的重點不是背公式，而是確保年份使用正確、農曆與節氣交界不混淆，否則命卦一錯，後面所有配置建議都會跟著歪掉。\n\n算出命卦後，你至少知道自己較適合東四方還是西四方。這對床頭朝向、書桌位置與長時間停留區域的安排都很有幫助。'), ('第二步：住宅坐向與宅卦判定', '接著要處理的是住宅本身。八宅風水怎麼算，不可能只看人不看宅。住宅的坐向通常要以整體格局與主要納氣方向來判斷，再據此分出東四宅或西四宅。這裡最容易犯的錯，是把門面方向直接等於坐向，或只憑感覺判斷。\n\n若想做得更準，至少要確認整體大門、陽台與主要採光面哪一面才是真正的納氣重點。這會直接影響宅卦判定。'), ('第三步：把方位放進平面圖，而不是只停留在口訣', '很多人學八宅風水怎麼算，卡在知道自己命卦後就停住了。其實真正重要的是把八方位對應到實際平面圖。當你把房子的中心點抓出來，分出東、南、西、北與四個斜角後，才知道主臥、大門、廚房、書桌到底落在哪一區。\n\n這一步一做，很多問題會立刻浮現：原來床頭剛好壓在不利方、原來書桌一直放在讓人分心的位置、原來大門進來的動線沒有緩衝。這些都是八宅風水真正有價值的地方。'), ('結論：八宅風水怎麼算，重點是算完要能用', '總結來說，八宅風水怎麼算不是為了考試，而是為了讓空間調整有依據。命卦、宅卦、平面圖與生活動線要放在一起看，才有實際價值。只要流程清楚、步驟不跳，你就不容易被零碎口訣繞進去。')]
    },
    {
        'slug': 'eight-mansions-fengshui-lucky-directions', 'title': '八宅風水吉方位整理', 'keyword': '八宅風水吉方位', 'desc': '整理八宅風水吉方位的判讀邏輯，說明生氣、延年、天醫、伏位如何應用在日常空間。',
        'faq': [('八宅風水吉方位一定每個都一樣重要嗎？', '不一定，通常會依用途排序，像主臥、床位、書桌與大門會優先考慮。'), ('吉方位可以拿來放什麼？', '適合放主臥、書桌、長時間工作區或需要穩定感的區域。'), ('吉方位找到了就一定會開運嗎？', '吉方位是加分條件，但仍要搭配整潔、通風、動線與實際生活習慣。')],
        'sections': [('前言：八宅風水吉方位為什麼常被過度神化？', '很多人在研究陽宅風水八宅風水時，最先想知道的就是八宅風水吉方位。這很正常，因為大家都想知道哪裡是生氣、延年、天醫、伏位，哪裡可以睡、可以坐、可以工作。但如果只把吉方位當成神奇按鈕，很容易誤會它的用途。吉方位不是保證書，而是空間安排的優先順序。\n\n真正有用的做法，是知道這些方位各自偏向哪種能量，再配合空間功能與生活習慣來用。這樣八宅風水吉方位才不會只停留在看圖說故事。'), ('生氣、延年、天醫、伏位各代表什麼？', '八宅風水吉方位中，生氣通常被視為最有發展性與提升感的方位，適合放工作區、書房或需要推進的空間；延年多與穩定、人際、關係和諧有關；天醫常被拿來對應健康與修養；伏位則偏向穩定、安定與長時間靜心使用。\n\n這些分類可以幫你決定：若空間有限，哪個區域先留給主臥、哪裡適合書桌、哪裡比較適合安靜閱讀。'), ('八宅風水吉方位最常怎麼用在住宅裡？', '實際操作上，八宅風水吉方位通常會優先套用在主臥、床頭朝向、書桌位置、大門納氣與常坐位。原因很簡單，這些區域對日常狀態影響最大。若吉方位剛好落在雜物間或很少使用的角落，再好的方位也很難真正發揮效果。\n\n因此，與其執著每一塊角落都要完美，不如先把最常用的區域放對位置。這是八宅風水比較務實的用法。'), ('結論：吉方位是優先安排，不是迷信按鈕', '總結來說，八宅風水吉方位真正的價值，在於告訴你有限空間裡誰該優先佔好位置。先把主臥、書桌、工作區和常坐位放進較適合的區域，再處理其他細節，往往比追求表面開運物更有效。')]
    },
    {
        'slug': 'eight-mansions-fengshui-bed-placement', 'title': '八宅風水床位怎麼擺', 'keyword': '八宅風水床位怎麼擺', 'desc': '整理八宅風水床位怎麼擺的原則，說明床頭方位、主臥位置與常見錯誤配置。',
        'faq': [('八宅風水床位怎麼擺最重要的是床頭還是房間位置？', '兩者都重要，但通常會先看主臥是否落在相對合適區域，再看床頭朝向。'), ('床位不可能完全照吉方位擺怎麼辦？', '先避開門沖、樑壓與明顯壓迫，再在可行範圍內朝較佳方位調整。'), ('八宅風水床位怎麼擺能改善睡眠嗎？', '若原本床位確實讓人不安、受沖或壓迫，調整後往往會提升穩定感與休息品質。')],
        'sections': [('前言：八宅風水床位怎麼擺，為什麼總是大家最先想調？', '在陽宅風水八宅風水裡，床位永遠是熱門題目，因為人每天待在床上的時間很長。八宅風水床位怎麼擺，不只是看起來順不順眼，而是牽涉到主臥位置、床頭朝向、門窗關係與睡眠安定感。若床位長期背門、壓樑、靠窗或落在明顯不舒服的位置，人就算嘴上說沒差，身體通常還是會有感。\n\n所以八宅風水床位怎麼擺的核心，從來不是只看一個羅盤角度，而是要把睡眠品質、房間格局與方位一起看。'), ('先看主臥位置，再看床頭方向', '很多人研究八宅風水床位怎麼擺時，只盯著床頭要朝哪裡，卻忽略主臥本身如果就落在不理想區域，床再怎麼轉也有限。比較合理的順序是：先看主臥區域是否與居住者命卦相對協調，再來看床頭朝向與門窗位置。\n\n若主臥位置已固定，床頭就成為更重要的微調點。這時候要同時兼顧有靠、避門沖、避鏡照與八宅吉方，不是只拼其中一條。'), ('床位配置最容易踩的幾個雷', '八宅風水床位怎麼擺最常見的錯誤，包括：床頭無靠、床尾直對門、鏡子照床、床壓樑、雙人床一側卡死、床下堆滿雜物。這些問題就算先不談八宅，光從使用感受來看都很容易讓人睡不安穩。\n\n當你把八宅吉方加入考量時，重點不是讓床硬塞進某個角，而是找一個兼顧方位與舒適度的平衡點。'), ('結論：床位不是硬拗角度，而是讓人真正睡得穩', '總結來說，八宅風水床位怎麼擺，真正目標不是追求教條，而是讓人睡得安、醒得穩。先把明顯雷點排除，再用八宅方位做優化，通常就是最實際的作法。')]
    },
    {
        'slug': 'eight-mansions-fengshui-front-door', 'title': '八宅風水大門方位', 'keyword': '八宅風水大門方位', 'desc': '整理八宅風水大門方位的判讀方式，說明大門納氣、住宅坐向與門位調整重點。',
        'faq': [('八宅風水大門方位是不是最重要？', '大門通常是高優先級項目，因為它影響納氣與日常進出感受。'), ('大門方位不能改還有救嗎？', '可以透過玄關、動線、收納與視線設計做調整，不是只有拆門重做一條路。'), ('八宅風水大門方位只看門朝向嗎？', '不只，大門前後的明亮度、整潔與內外緩衝同樣重要。')],
        'sections': [('前言：八宅風水大門方位為什麼一堆人特別在意？', '大門在陽宅風水八宅風水裡之所以重要，是因為它被視為住宅納氣入口。八宅風水大門方位不只影響方位上的吉凶判讀，也影響實際的進出動線、光線與入口秩序。若大門本身落在比較尷尬的位置，或一進門就見亂、見壓迫、見不舒服的視線，住起來通常也會比較卡。\n\n這就是為什麼很多人在學八宅時，會先問大門能不能落吉方。因為門一開，整個家的第一口氣就從這裡開始。'), ('八宅風水大門方位怎麼看才不會看錯？', '八宅風水大門方位的判斷，不能只看門片朝哪邊，還要回到住宅坐向與主要納氣面來看。有些房子大門只是出入口，但真正採光與空氣主要來自陽台；有些住宅則大門本身就是最主要氣口。若不先分清楚，很容易在計算上產生偏差。\n\n因此，八宅風水大門方位應該放在整體宅卦判讀裡理解，而不是單獨抽出來看。'), ('大門不理想時可以怎麼調整？', '現實裡很多人的大門無法重開，所以八宅風水大門方位若不理想，通常會先從玄關動線、收納整潔、採光照明與視線遮擋著手。像是一開門直見雜物、直見廁所、直見長走道，都可以透過玄關櫃、屏風、燈光與整理來降低不舒服感。\n\n也就是說，大門方位固然重要，但入口秩序同樣是風水的一部分，不要把所有責任都推給方位本身。'), ('結論：大門方位是起點，但入口秩序才是你天天會感受到的事', '總結來說，八宅風水大門方位值得重視，因為它關係到住宅納氣與第一印象；但若想真正提升居住感受，仍要把玄關、收納、照明與動線一起整理。這樣的調整才有機會從理論變成日常。')]
    },
    {
        'slug': 'eight-mansions-fengshui-bedroom', 'title': '八宅風水主臥配置', 'keyword': '八宅風水主臥配置', 'desc': '整理八宅風水主臥配置重點，說明主臥區域、床位、衣櫃與安定感之間的關係。',
        'faq': [('八宅風水主臥配置要先看哪裡？', '先看主臥落在哪個方位，再看床頭、收納與門窗關係。'), ('主臥一定要在吉方嗎？', '理想上會優先考慮，但若格局固定，也能透過床位與空間秩序做調整。'), ('主臥配置和夫妻關係有關嗎？', '在風水邏輯裡，主臥的穩定感常被視為影響關係與睡眠的重要因素。')],
        'sections': [('前言：八宅風水主臥配置為什麼比客房重要得多？', '在陽宅風水八宅風水裡，主臥的重要性通常遠高於客房或次要房間，因為主臥是居住者每天停留最久、最需要安定感的地方。八宅風水主臥配置如果做得好，通常對睡眠、情緒與生活節奏都有幫助；反過來說，主臥若落在讓人不舒服的方位，再加上床位不穩、收納凌亂，人在裡面自然難放鬆。\n\n所以主臥配置不是只看裝潢美不美，而是看這個空間是不是能讓人真正安穩下來。'), ('主臥區域選擇：方位比面積更值得先看', '八宅風水主臥配置的第一步，通常不是挑最大的房，而是看哪個房間更適合長期休息。若主臥剛好落在對居住者較佳的方位，通常會是優先選擇。這並不是說面積不重要，而是安定感與實際使用順序，往往比多幾坪更有感。\n\n當主臥方位比較理想時，再去處理床位、照明、衣櫃與門窗，就會更容易形成穩定感。'), ('主臥裡哪些細節最容易破壞風水？', '八宅風水主臥配置最常見的問題包括：鏡子直照床、床尾對門、衣櫃壓迫、房內雜物過多、工作區硬塞進睡眠區、燈光過強或色調太躁。這些情況不只在風水上被視為干擾，實際生活裡也很容易讓人無法真正休息。\n\n因此，主臥配置應該盡量簡化，讓睡眠、收納與基本閱讀活動各有位置，不要什麼都往裡面塞。'), ('結論：主臥配置的終點，是讓人進房後能慢慢安靜下來', '總結來說，八宅風水主臥配置真正重視的是安穩感。先挑相對適合的區域，再把床位、收納與光線整理清楚，比硬追一堆裝飾與口訣更有用。')]
    },
    {
        'slug': 'eight-mansions-fengshui-study-desk', 'title': '八宅風水書桌方向', 'keyword': '八宅風水書桌方向', 'desc': '整理八宅風水書桌方向的安排原則，說明讀書、工作與專注力區域如何配合吉方位。',
        'faq': [('八宅風水書桌方向真的會影響專注力嗎？', '至少在空間秩序與視線安定上會有影響，若方位合適又不受干擾，通常更容易坐得住。'), ('書桌一定要面向吉方嗎？', '理想上可以優先考慮，但仍要兼顧採光、背後有靠與不受門沖。'), ('書桌擺在臥室會不會有問題？', '可以，但要避免工作區完全侵占睡眠區，否則容易讓休息感下降。')],
        'sections': [('前言：八宅風水書桌方向，為什麼工作越忙的人越該看？', '在遠距工作與長時間用腦成為日常後，八宅風水書桌方向這個問題變得比以前更實際。很多人不是沒有書桌，而是桌子擺得讓人坐下來就分心、背後沒安全感、光線不對、面前雜訊太多。八宅風水提供的其中一個價值，就是幫你找到比較能穩定專注的區域。\n\n八宅風水書桌方向不是迷信地找神奇角度，而是把專注、視線、坐姿穩定與方位加在一起考量。'), ('書桌方向怎麼選，才不會只剩儀式感？', '八宅風水書桌方向的安排，通常會優先考慮命卦中的較佳方位，再搭配背後有靠、前方開闊、側邊採光適中與避開門沖。若只把桌子硬轉到吉方，卻讓螢幕反光、走道一直有人經過，實際效果通常不會好。\n\n因此，方位是加分條件，但空間使用感仍是核心。'), ('讀書區與工作區可以怎麼用八宅優化？', '若家中有多個可用角落，可以把需要長時間專注的工作桌放在相對穩定的方位，把暫時處理雜事的區域放在次要位置。這樣八宅風水書桌方向就不只是理論，而是直接反映在你每天的工作節奏上。\n\n另外，桌面整潔、線材收納、椅背支撐與照明品質，也都會影響書桌風水的穩定度。'), ('結論：書桌方向的目標是讓你坐得住，不是坐得玄', '總結來說，八宅風水書桌方向的重點，是建立一個比較容易專注與久坐的區域。方位有幫助，但秩序、光線與支撐感同樣重要。')]
    },
    {
        'slug': 'eight-mansions-fengshui-east-west-group', 'title': '八宅風水東四命西四命差異', 'keyword': '八宅風水東四命西四命差異', 'desc': '說明八宅風水東四命西四命差異，幫助讀者理解命卦分組與住宅方位應用。',
        'faq': [('八宅風水東四命西四命差異最核心是什麼？', '核心在於不同命卦較適合的方位群不同，因此空間安排重點會有所差別。'), ('夫妻一個東四命一個西四命怎麼辦？', '通常會以主要居住需求、共同可接受的方位與主臥配置平衡處理，不必過度恐慌。'), ('東四命西四命差異會影響所有房間嗎？', '會影響整體判讀，但最重要的還是主臥、書桌與常待區域。')],
        'sections': [('前言：八宅風水東四命西四命差異，為什麼是整套系統的分水嶺？', '學陽宅風水八宅風水時，八宅風水東四命西四命差異是一定會碰到的核心概念。因為這個分類直接決定你後續怎麼看吉方與凶方。若連自己屬於哪一組都沒搞清楚，後面無論看床位、主臥、書桌還是大門，都很容易整個套錯。\n\n可以說，東四命與西四命的分組，就是八宅風水判讀的起跑線。'), ('東四命與西四命到底差在哪裡？', '八宅風水東四命西四命差異，最直接的表現就是適合的方位群不同。東四命通常較偏向東、東南、南、北這一組方向；西四命則較偏向西、西北、西南、東北。這種差異並不是要把人分高低，而是提供一套空間使用優先順序。\n\n也就是說，當你知道自己是哪一組後，至少能先判斷哪些區域更適合長時間停留。'), ('不同命組的人一起住，要怎麼處理？', '實務上最常見的問題，就是家人命卦不完全一致。這時候八宅風水東四命西四命差異的應用，就不能太僵。一般會先找共同生活中最重要的區域，例如主臥、書桌、常坐位，盡量做平衡安排；再來才是次要空間的微調。\n\n八宅的重點不是讓全家每個角落都完美，而是把影響最大的地方先安排妥當。'), ('結論：先懂命組差異，後面所有配置才會有基礎', '總結來說，八宅風水東四命西四命差異是理解整套系統的基礎。只要這一步清楚，你後面看吉方、凶方、床位與書桌時都會更有方向。')]
    },
    {
        'slug': 'eight-mansions-fengshui-house-selection', 'title': '八宅風水選屋重點', 'keyword': '八宅風水選屋重點', 'desc': '整理八宅風水選屋重點，說明看房時如何用八宅概念快速篩選格局與方位。',
        'faq': [('八宅風水選屋重點最先看哪裡？', '先看住宅大致坐向與主要納氣面，再看主臥與大門位置。'), ('看房時沒有平面圖也能用八宅嗎？', '可以先做初步判斷，但若要更準，最好仍搭配平面圖與方位工具。'), ('八宅風水選屋重點適合租屋族嗎？', '適合，因為它能幫你快速挑出比較容易住得穩的格局。')],
        'sections': [('前言：八宅風水選屋重點，為什麼比入住後再補救更省力？', '很多人開始研究陽宅風水八宅風水，都是房子買了、租了、裝潢做了，才發現怎麼住都卡。其實若在看房階段就先掌握八宅風水選屋重點，很多明顯不適合自己的格局一開始就能排除，省下後續大量補救成本。\n\n八宅風水選屋重點不需要你變成專業師傅，而是讓你在看房時多一套篩選邏輯。'), ('看房時先抓住宅坐向與主要納氣面', '八宅風水選屋重點的第一步，是快速判斷住宅的主要納氣方向與大致坐向。這能幫你先知道它大概屬於哪一類宅卦。若你連房子的主要採光面與進氣方向都搞不清楚，後面再怎麼看方位都容易模糊。\n\n看房時可先記錄大門位置、陽台方向與客廳主要採光面，再配合簡單羅盤工具做初步判斷。'), ('主臥、大門、工作區先過關，其他再說', '八宅風水選屋重點裡，最值得先檢查的是主臥、大門與可作為工作區的位置。因為這三個地方對日常狀態影響最大。如果這些關鍵區域全卡在不理想位置，之後就算靠軟裝調整，彈性也有限。\n\n相反地，只要關鍵區域大致順手，其他次要空間往往比較容易處理。'), ('結論：選屋先篩掉明顯不適合的，比入住後硬救實在', '總結來說，八宅風水選屋重點最大的價值，在於幫你在看房階段先做篩選。只要先抓坐向、看主臥與大門、確認工作區，很多將來會讓你住得很累的問題，其實一開始就看得出來。')]
    }
]

all_entries = [
    ('general/current-stock-market-analysis.html', '現今股市的分析｜市場趨勢、風險與投資人關注重點', '網站編輯部'),
    ('general/folk-customs.html', '民間習俗整理｜常見傳統觀念、節慶禁忌與生活文化解析', '網站編輯部'),
    ('suiyuantang/kitchen-fengshui.html', '廚房風水完整指南｜爐灶、動線、收納與常見禁忌解析', '隨緣堂'),
    ('suiyuantang/toilet-fengshui.html', '廁所風水完整解析｜穢氣、通風、清潔與常見禁忌整理', '隨緣堂'),
    ('suiyuantang/front-door-fengshui.html', '大門風水完整解析｜納氣、門向、玄關與常見禁忌整理', '隨緣堂'),
]
for item in cluster:
    all_entries.append((f"suiyuantang/{item['slug']}.html", item['title'], '隨緣堂'))

slugs = [item['slug'] for item in cluster]
slug_to_title = {item['slug']: item['title'] for item in cluster}

def faq_json(faqs):
    return ','.join(
        '{{"@type":"Question","name":"{}","acceptedAnswer":{{"@type":"Answer","text":"{}"}}}}'.format(
            q.replace('"', '\\"'), a.replace('"', '\\"')
        ) for q, a in faqs
    )

STYLE = '''
  <style>
    :root {
      --bg: #f7f1ea;
      --paper: rgba(255,255,255,0.9);
      --card: #ffffff;
      --text: #2f261f;
      --muted: #6f6258;
      --primary: #8a6038;
      --primary-dark: #654326;
      --line: #eadccf;
      --soft: #fff8ef;
      --shadow: 0 16px 40px rgba(80,56,29,0.08);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body { margin: 0; font-family: "Noto Sans TC", "Microsoft JhengHei", sans-serif; line-height: 1.85; color: var(--text); background: linear-gradient(180deg, #fdfaf6 0%, var(--bg) 100%); }
    a { color: inherit; text-decoration: none; }
    .container { width: min(1120px, calc(100% - 32px)); margin: 0 auto; }
    .hero { background: linear-gradient(135deg, #fff9f1 0%, #f3e7d8 100%); border-bottom: 1px solid rgba(138,96,56,0.14); }
    .hero-inner { display: grid; grid-template-columns: 1.08fr 0.92fr; gap: 28px; align-items: center; padding: 76px 0 56px; }
    .badge { display: inline-block; padding: 8px 14px; border-radius: 999px; background: rgba(138,96,56,0.1); color: var(--primary-dark); font-size: 14px; font-weight: 800; letter-spacing: .04em; margin-bottom: 18px; }
    h1 { margin: 0 0 16px; font-size: clamp(34px, 5vw, 60px); line-height: 1.15; }
    .lead { margin: 0; color: var(--muted); font-size: 18px; }
    .hero-card, .card, .faq-item, .toc { background: var(--paper); border: 1px solid var(--line); border-radius: 24px; box-shadow: var(--shadow); }
    .hero-card { padding: 24px; }
    .hero-card h3, .card h3, .faq-item h3 { margin-top: 0; }
    .hero-card ul, .card ul { margin: 0; padding-left: 20px; }
    .hero-card li, .card p, .card li, .faq-item p, .meta { color: var(--muted); }
    section { padding: 72px 0; }
    .layout { display: grid; grid-template-columns: 280px minmax(0,1fr); gap: 28px; align-items: start; }
    .toc { position: sticky; top: 18px; padding: 20px; }
    .toc a { display: block; padding: 8px 0; color: var(--primary-dark); font-weight: 700; }
    .card { padding: 28px; margin-bottom: 24px; }
    h2 { margin-top: 0; margin-bottom: 14px; font-size: clamp(28px, 4vw, 40px); }
    h3 { margin-bottom: 10px; font-size: 22px; }
    .mini-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 24px; }
    .mini-card { background: var(--soft); border: 1px solid var(--line); border-radius: 20px; padding: 22px; box-shadow: var(--shadow); }
    .mini-card h3 { color: var(--primary-dark); }
    .faq-wrap { background: linear-gradient(180deg, var(--soft) 0%, #fff 100%); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
    .faq-list { display: grid; gap: 18px; }
    .faq-item { padding: 22px; }
    .footer-links { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 14px; }
    .footer-links a { display: inline-flex; align-items: center; justify-content: center; padding: 10px 16px; border-radius: 12px; background: var(--soft); color: var(--primary-dark); font-weight: 800; }
    footer { padding: 30px 0 48px; text-align: center; color: var(--muted); font-size: 14px; }
    .card a { color: var(--primary-dark); font-weight: 800; }
    @media (max-width: 920px) { .hero-inner, .layout, .mini-grid { grid-template-columns: 1fr; } .toc { position: static; } }
  </style>
'''

for item in cluster:
    slug = item['slug']
    others = [s for s in slugs if s != slug]
    related = others[:3]
    section_html = []
    for idx, (h2, body) in enumerate(item['sections']):
        extras = ''
        if idx == 0:
            extras = '<h3>實務閱讀提醒</h3><p>看這類主題時，建議先抓核心邏輯，再對照自己家的平面圖與使用習慣，不要只記口訣。</p>'
        elif idx == 1:
            extras = '<h3>常見誤區</h3><p>最常見的錯誤是把方位神化，卻忽略空間本身的動線、通風、收納與安定感。</p>'
        section_html.append('<article class="card"><h2>{}</h2>{}{}</article>'.format(
            escape(h2), ''.join(f'<p>{escape(p)}</p>' for p in body.split('\n\n')), extras))
    related_links = ''.join(f'<li><a href="{r}.html">{escape(slug_to_title[r])}</a></li>' for r in related)
    faq_items = ''.join(f'<article class="faq-item"><h3>{escape(q)}</h3><p>{escape(a)}</p></article>' for q, a in item['faq'])
    mini_cards = ''.join(f'<div class="mini-card"><h3>{escape(slug_to_title[r])}</h3><p>延伸閱讀，幫你把八宅風水這個主題往下一層拆解。</p></div>' for r in related)
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escape(item['title'])}｜隨緣堂</title>
  <meta name="description" content="{escape(item['desc'])}" />
  <meta name="keywords" content="{escape(item['keyword'])},陽宅風水八宅風水,隨緣堂" />
  <link rel="canonical" href="{base}/suiyuantang/{slug}.html" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json(item['faq'])}]}}</script>
  {STYLE}
</head>
<body>
  <header class="hero">
    <div class="container hero-inner">
      <div>
        <div class="badge">隨緣堂｜陽宅風水八宅風水文章群</div>
        <h1>{escape(item['title'])}</h1>
        <p class="lead">{escape(item['keyword'])}是這組文章群的重要子題。這篇會用比較好讀的方式，整理概念、誤區、實作重點與 FAQ，並連結其他相關文章，避免你只看到零碎口訣卻不知道怎麼落地。</p>
      </div>
      <aside class="hero-card">
        <h3>這篇先看 3 件事</h3>
        <ul>
          <li>先理解核心邏輯，不要只背吉凶方位。</li>
          <li>把理論放回平面圖與日常使用習慣去看。</li>
          <li>搭配其他子文章閱讀，理解會更完整。</li>
        </ul>
      </aside>
    </div>
  </header>
  <main>
    <section>
      <div class="container layout">
        <nav class="toc">
          <strong>內部導覽</strong>
          <a href="eight-mansions-fengshui-guide.html">回總指南頁</a>
          <a href="#article">文章重點</a>
          <a href="#extend">延伸閱讀</a>
          <a href="#faq">FAQ</a>
          <a href="index.html">回隨緣堂分類首頁</a>
        </nav>
        <div id="article">
          {''.join(section_html)}
          <article class="card" id="extend">
            <h2>延伸閱讀與內部連結</h2>
            <p>這組文章群是串著看的，以下是和本篇最相關的其他子題：</p>
            <ul>{related_links}</ul>
            <div class="mini-grid">{mini_cards}</div>
          </article>
        </div>
      </div>
    </section>
    <section class="faq-wrap" id="faq">
      <div class="container">
        <h2>常見問題 FAQ</h2>
        <div class="faq-list">{faq_items}</div>
      </div>
    </section>
  </main>
  <footer>
    <div class="meta">更新日期：{update_date}</div>
    <div class="footer-links">
      <a href="eight-mansions-fengshui-guide.html">總指南頁</a>
      <a href="{related[0]}.html">延伸閱讀 1</a>
      <a href="{related[1]}.html">延伸閱讀 2</a>
      <a href="{related[2]}.html">延伸閱讀 3</a>
    </div>
  </footer>
</body>
</html>'''
    (sui / f'{slug}.html').write_text(html, encoding='utf-8')

hub = cluster[0]
child_links = ''.join(f'<article class="card"><h3><a href="{item["slug"]}.html">{escape(item["title"])}</a></h3><p>{escape(item["desc"])}</p></article>' for item in cluster[1:])
hub_faq_items = ''.join(f'<article class="faq-item"><h3>{escape(q)}</h3><p>{escape(a)}</p></article>' for q, a in hub['faq'])
hub_html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escape(hub['title'])}｜隨緣堂</title>
  <meta name="description" content="{escape(hub['desc'])}" />
  <meta name="keywords" content="陽宅風水八宅風水,八宅風水,隨緣堂" />
  <link rel="canonical" href="{base}/suiyuantang/{hub['slug']}.html" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json(hub['faq'])}]}}</script>
  {STYLE}
</head>
<body>
  <header class="hero">
    <div class="container hero-inner">
      <div>
        <div class="badge">隨緣堂｜主頁 Hub Page</div>
        <h1>{escape(hub['title'])}</h1>
        <p class="lead">陽宅風水八宅風水是許多人學習住宅風水時的重要起點。這頁把命卦、宅卦、吉方位、床位、大門、主臥、書桌與選屋等子題串成文章群，讓閱讀路徑更完整，也讓整體 SEO 結構更像樣。</p>
      </div>
      <aside class="hero-card">
        <h3>這組內容適合誰？</h3>
        <ul>
          <li>剛接觸八宅風水，想先建立基礎架構的人</li>
          <li>正在看房、搬家、重整主臥或書房的人</li>
          <li>想把單篇知識串成完整判斷邏輯的人</li>
        </ul>
      </aside>
    </div>
  </header>
  <main>
    <section>
      <div class="container">
        <article class="card">
          <h2>文章群總覽</h2>
          <p>以下是本次延伸建立的子文章，建議先看基礎計算與命組差異，再往床位、大門、主臥與選屋延伸：</p>
          <div class="mini-grid">{child_links}</div>
        </article>
        <article class="card">
          <h2>為什麼要用文章群方式理解八宅風水？</h2>
          <p>因為八宅風水的概念環環相扣，從命卦、吉方位到主臥與選屋，都不是單篇能完整講完。文章群最大的價值，就是讓讀者與搜尋引擎一起知道這個網站不是只做一篇，而是在完整回答同一個主題。</p>
          <h3>閱讀順序建議</h3>
          <p>建議先看「八宅風水怎麼算」與「東四命西四命差異」，再讀到吉方位、床位、大門與主臥配置。若你正在找房，可以直接補看「八宅風水選屋重點」。</p>
          <h3>SEO 與閱讀體驗一起顧</h3>
          <p>這種 Hub + Cluster 結構，既能提升內部連結，也能讓每一篇子文章都回到同一個核心主題，不會散掉。</p>
        </article>
      </div>
    </section>
    <section class="faq-wrap">
      <div class="container">
        <h2>常見問題 FAQ</h2>
        <div class="faq-list">{hub_faq_items}</div>
      </div>
    </section>
  </main>
  <footer>
    <div class="meta">更新日期：{update_date}</div>
    <div class="footer-links">
      <a href="eight-mansions-fengshui-calculation.html">八宅風水怎麼算</a>
      <a href="eight-mansions-fengshui-bed-placement.html">八宅風水床位怎麼擺</a>
      <a href="eight-mansions-fengshui-house-selection.html">八宅風水選屋重點</a>
    </div>
  </footer>
</body>
</html>'''
(sui / f"{hub['slug']}.html").write_text(hub_html, encoding='utf-8')

sui_pages = [
    ('kitchen-fengshui.html', '廚房風水完整指南｜爐灶、動線、收納與常見禁忌解析'),
    ('toilet-fengshui.html', '廁所風水完整解析｜穢氣、通風、清潔與常見禁忌整理'),
    ('front-door-fengshui.html', '大門風水完整解析｜納氣、門向、玄關與常見禁忌整理'),
] + [(f"{item['slug']}.html", item['title']) for item in cluster]
(sui / 'index.html').write_text('<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>隨緣堂｜風水主題文章索引</title></head><body><h1>隨緣堂｜風水主題文章索引</h1><ul>' + ''.join(f'<li><a href="{href}">{escape(title)}</a></li>' for href, title in sui_pages) + '</ul></body></html>', encoding='utf-8')

gen_pages = [('current-stock-market-analysis.html', '現今股市的分析｜市場趨勢、風險與投資人關注重點'), ('folk-customs.html', '民間習俗整理｜常見傳統觀念、節慶禁忌與生活文化解析')]
(gen / 'index.html').write_text('<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>一般主題文章索引｜網站編輯部</title></head><body><h1>一般主題文章索引</h1><ul>' + ''.join(f'<li><a href="{href}">{escape(title)}</a></li>' for href, title in gen_pages) + '</ul></body></html>', encoding='utf-8')

(root / 'index.html').write_text('<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>網站總覽</title></head><body><h1>網站總覽</h1><ul>' + ''.join(f'<li><a href="{path}">{escape(title)}</a></li>' for path, title, _ in all_entries) + '</ul></body></html>', encoding='utf-8')
(root / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://eason1388.github.io/fengshui-site/sitemap.xml\n', encoding='utf-8')
urls = [f'{base}/index.html', f'{base}/suiyuantang/index.html', f'{base}/general/index.html'] + [f'{base}/{path}' for path, _, _ in all_entries]
(root / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(f'  <url><loc>{u}</loc><lastmod>{update_date}</lastmod></url>' for u in urls) + '\n</urlset>', encoding='utf-8')

print('cluster pages restyled')
