from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

if 'id="cognitionPage"' in text or 'const cognitionThemes=' in text:
    raise SystemExit('Cognition archive already exists; refusing duplicate insertion')

css = r'''
    .cognition-main{max-width:1040px;padding:48px 0 88px}.cognition-hero{max-width:850px;padding:26px 0 50px}.cognition-hero .detail-title{margin-bottom:20px}.cognition-manifesto{margin:0;max-width:820px;color:var(--text);font-family:var(--serif);font-size:clamp(25px,3vw,38px);font-weight:600;line-height:1.36;letter-spacing:-.012em}.cognition-manifesto-zh{max-width:800px;margin:10px 0 0;color:var(--muted);font-size:13px;line-height:1.85}.cognition-index-section{margin-top:8px;border-top:1px solid var(--line);padding-top:34px}.cognition-index-heading{display:flex;align-items:baseline;justify-content:space-between;gap:24px;margin-bottom:18px}.cognition-index-heading h2{margin:0;color:var(--rose);font-family:var(--mono);font-size:11px;font-weight:550;letter-spacing:.12em}.cognition-index-summary{color:var(--muted-dark);font-family:var(--mono);font-size:10px;letter-spacing:.07em}.cognition-theme-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.cognition-theme-card{position:relative;min-height:205px;display:flex;flex-direction:column;padding:26px 28px;border:1px solid var(--line);border-radius:var(--radius-card);background:rgba(26,20,32,.58);cursor:pointer;text-align:left;transition:transform .24s var(--ease),border-color .2s ease,background .2s ease}.cognition-theme-card:hover,.cognition-theme-card:focus-visible{transform:translateY(-2px);border-color:var(--rose-soft);background:var(--card-hover);outline:none}.cognition-theme-card.developing{grid-column:1/-1;min-height:190px;border-color:var(--line-strong);background:var(--card)}.cognition-card-top{display:flex;align-items:center;justify-content:space-between;gap:18px}.cognition-card-type,.cognition-card-count{color:var(--muted-dark);font-family:var(--mono);font-size:10px;letter-spacing:.08em}.cognition-theme-card.developing .cognition-card-type{color:var(--rose)}.cognition-card-title{margin:24px 0 0;color:var(--text);font-family:var(--serif);font-size:clamp(26px,2.8vw,34px);font-weight:700;line-height:1.14;letter-spacing:-.012em}.cognition-card-subtitle{display:block;margin-top:6px;color:var(--muted);font-size:12px;font-weight:450;line-height:1.5}.cognition-card-summary{max-width:650px;margin:14px 36px 0 0;color:var(--muted);font-size:14px;line-height:1.72}.cognition-card-arrow{position:absolute;right:26px;bottom:24px;color:var(--rose);font-family:var(--mono);font-size:17px;transition:transform .2s ease}.cognition-theme-card:hover .cognition-card-arrow,.cognition-theme-card:focus-visible .cognition-card-arrow{transform:translateX(4px)}
    .cognition-detail{max-width:1040px;padding:36px 0 94px}.cognition-detail-meta{display:flex;align-items:center;justify-content:space-between;gap:24px;padding-bottom:19px;border-bottom:1px solid var(--line);color:var(--muted);font-family:var(--mono);font-size:10px;letter-spacing:.08em}.cognition-detail-status{color:var(--rose)}.cognition-detail-heading{padding:42px 0 34px}.cognition-detail-heading h1{max-width:900px;margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(42px,6vw,70px);font-weight:700;line-height:1.06;letter-spacing:-.022em}.cognition-detail-heading p{margin:11px 0 0;color:var(--muted);font-family:var(--mono);font-size:13px;letter-spacing:.04em;line-height:1.65}.cognition-reference-note{max-width:880px;margin:0 0 30px;padding:14px 16px;border-left:2px solid var(--rose-soft);background:rgba(141,123,178,.045);color:var(--muted);font-size:12px;line-height:1.8}.cognition-reflection-list{border-top:1px solid var(--line)}.cognition-reflection{display:grid;grid-template-columns:44px minmax(0,1fr);gap:24px;padding:34px 0;border-bottom:1px solid var(--line)}.cognition-reflection-index{padding-top:4px;color:var(--rose);font-family:var(--mono);font-size:11px;letter-spacing:.08em}.cognition-reflection-title{margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(25px,2.8vw,32px);font-weight:700;line-height:1.2}.cognition-thought{max-width:870px;margin:18px 0 0;color:var(--text);font-size:15px;line-height:1.95;white-space:pre-line}.cognition-related{display:flex;align-items:flex-start;flex-wrap:wrap;gap:8px 10px;margin-top:20px}.cognition-related-label{margin-right:4px;padding-top:4px;color:var(--muted-dark);font-family:var(--mono);font-size:10px;letter-spacing:.08em}.cognition-tag{display:inline-flex;padding:5px 8px;border:1px solid var(--line);border-radius:999px;color:var(--muted);font-family:var(--mono);font-size:10px;line-height:1.3;letter-spacing:.025em}.cognition-theory{display:grid;gap:24px}.cognition-theory-intro{padding:28px;border:1px solid var(--line-strong);border-radius:var(--radius-card);background:rgba(26,20,32,.72)}.cognition-theory-kicker{margin:0;color:var(--rose);font-family:var(--mono);font-size:10px;letter-spacing:.1em}.cognition-theory-thesis{max-width:820px;margin:13px 0 0;color:var(--text);font-family:var(--serif);font-size:clamp(25px,3.1vw,38px);font-weight:650;line-height:1.42;letter-spacing:-.012em}.cognition-theory-copy{max-width:850px;margin:16px 0 0;color:var(--muted);font-size:14px;line-height:1.9}.cognition-chain{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px}.cognition-chain-step{position:relative;min-height:102px;display:flex;align-items:center;justify-content:center;padding:16px 12px;border:1px solid var(--line);border-radius:10px;background:rgba(26,20,32,.45);color:var(--text);font-family:var(--mono);font-size:11px;line-height:1.55;text-align:center}.cognition-chain-step:not(:last-child)::after{content:"→";position:absolute;right:-9px;z-index:2;color:var(--rose);background:var(--bg);padding:0 2px}.cognition-theory-steps{border-top:1px solid var(--line)}.cognition-theory-step{display:grid;grid-template-columns:42px minmax(0,1fr);gap:18px;padding:21px 0;border-bottom:1px solid var(--line)}.cognition-theory-step-num{color:var(--rose);font-family:var(--mono);font-size:10px;letter-spacing:.08em}.cognition-theory-step p{margin:0;color:var(--text);font-size:15px;line-height:1.8}.cognition-theory-change{padding:22px 24px;border-left:2px solid var(--rose);background:rgba(141,123,178,.05)}.cognition-theory-change strong{display:block;color:var(--text);font-family:var(--serif);font-size:20px}.cognition-theory-change p{margin:8px 0 0;color:var(--muted);font-size:14px;line-height:1.85}
'''
marker = '    footer{padding:28px 0 34px;'
if marker not in text:
    raise SystemExit('CSS footer marker not found')
text = text.replace(marker, css + '\n' + marker, 1)

html = r'''
  <div id="cognitionPage" class="view subpage"><div class="shell"><nav class="topbar" aria-label="Cognition navigation"><button class="brand" type="button" onclick="showPortal()">KeeCharlotte</button><button class="back-link" type="button" onclick="backToAbility()">← Ability</button></nav><main class="cognition-main"><header class="cognition-hero"><p class="eyebrow">Ability · Cognition</p><h1 class="detail-title">Cognition</h1><p class="cognition-manifesto">A record of how I reason about the world, emotion, meaning, human nature, and the patterns behind choice.</p><p class="cognition-manifesto-zh">這裡紀錄我對世界、情緒、意義、人性與選擇模式的思考。保留推理過程，而不是只留下結論。</p></header><section class="cognition-index-section" aria-labelledby="cognitionIndexTitle"><div class="cognition-index-heading"><h2 id="cognitionIndexTitle">Reflection archive</h2><span id="cognitionIndexSummary" class="cognition-index-summary"></span></div><div id="cognitionThemeGrid" class="cognition-theme-grid"></div></section></main><footer>© 2026 KeeCharlotte</footer></div></div>

  <div id="cognitionDetailPage" class="view subpage"><div class="shell"><nav class="topbar" aria-label="Cognition detail navigation"><button class="brand" type="button" onclick="showPortal()">KeeCharlotte</button><button class="back-link" type="button" onclick="backToCognition()">← Cognition</button></nav><main class="cognition-detail"><div class="cognition-detail-meta"><span>Personal reasoning archive</span><span id="cognitionDetailMeta"></span></div><header class="cognition-detail-heading"><p id="cognitionDetailEyebrow" class="eyebrow">Ability · Cognition</p><h1 id="cognitionDetailTitle"></h1><p id="cognitionDetailSubtitle"></p></header><p class="cognition-reference-note">以下為個人思考紀錄；「關聯概念」僅作延伸參照，不代表我的想法與該理論完全等同。</p><div id="cognitionDetailContent"></div></main><footer>© 2026 KeeCharlotte</footer></div></div>

'''
html_marker = '  <div id="categoryPage"'
if html_marker not in text:
    raise SystemExit('categoryPage HTML marker not found')
text = text.replace(html_marker, html + html_marker, 1)

data = r'''
    const cognitionThemeOrder=["personality-destiny","worldview","emotion-reason","meaning-freedom","self-integration","human-ethics"];
    const cognitionThemes={
      "personality-destiny":{
        title:"個性即命運",subtitle:"Personality as Destiny",type:"theory",status:"Developing theory",
        summary:"從個性、偏好、選擇與結果之間的連鎖關係，推導命運為何可被預測，也為何仍能被改變。",
        tags:["Heraclitus","Temperament","CAPS","人格改變"],
        theory:{
          thesis:"個性即命運。命運不是固定不變的外力，而是穩定思考模式長期推動偏好與選擇後，形成的高機率人生軌跡。",
          copy:"這是我自己從「命運是什麼」開始，一個步驟一個步驟推導出的模型。核心不是把命運理解成神祕的預定結果，而是把它拆成可以追蹤的因果鏈。",
          chain:["個性\n（思考模式）","情境中的\n偏好作法","反覆出現的\n選擇與行為","長期累積的\n結果","命運"],
          steps:[
            "人出生時就帶有某些個性傾向。",
            "個性會影響一個人在遇到事情時偏好的處理方式。",
            "當相似的偏好在不同情境中反覆出現，選擇與結果就會形成可辨識的模式。",
            "多個長期模式累積後，一個人的人生走向便能在一定程度上被合理推斷；我把這個高機率軌跡稱為命運。",
            "命運不是不可改變。若能改變個性，偏好與選擇也會改變，人生軌跡便會跟著改變。",
            "真正困難的地方在於：個性不是單一行為，而是更底層的思考模式。行為可以暫時壓住，思考模式卻很難重寫，所以改變命運需要非常大的努力。"
          ],
          changeTitle:"命運可以改變，但成本很高。",
          change:"改變表面的行為，未必等於改變個性；只有當底層思考模式真的改變，偏好與長期選擇才會跟著穩定改變。"
        }
      },
      worldview:{
        title:"世界觀與形上學",subtitle:"Worldview & Metaphysics",type:"reflection",
        summary:"從世界是否可被規則、數學與物理還原，到把視角拉離自身後重新觀看人類。",
        reflections:[
          {title:"世界作為規則實驗場",thought:`我曾經想過，這個世界的本質可能是一個由精密規則打造的實驗場。只要規定每一個原子的行為，就等於規定了整個底層世界的運作，其他事物理論上都可以透過足夠精密的計算被推導。\n\n我當時把「生物」想成整個系統裡唯一真正的變數：高等生物或許設下這個場域，就是想觀察在固定規則之下，生物是否會產生連設計者自己都沒有預想過的新結論、新技術或新的可能性。`,tags:["決定論","模擬假說","自由意志"]},
          {title:"數學與物理作為世界底層",thought:`我常覺得這個世界本質上就是由數學和物理組成的。看到風吹樹葉，腦中會自動去想風作用在葉面的力、面積與做功，為什麼最後會形成眼前的晃動；看到下雨，也會想像水滴落在葉面上的過程。\n\n這種習慣讓我進一步想到：如果變數與規則都足夠完整，世界是不是能被精密的數學計算模擬出來？`,tags:["機械論","數學宇宙假說","數位物理學"]},
          {title:"衛星／神明視角",thought:`遇到壓力或煩心事時，我會刻意把視角從自己身上抽離，想像自己站在地球外太空，用衛星或神明視角看整個人類社會、國與國之間的連結與繁榮。\n\n在那個尺度下，我會覺得大家終究都只是地球上的人類與生物，國界、人種與眼前的衝突都突然變得很小。再從這個視角回頭看自己正在承受的壓力，就會覺得事情其實沒有原本感受到的那麼巨大。`,tags:["Overview Effect","斯多葛宇宙視角","去人類中心化"]}
        ]
      },
      "emotion-reason":{
        title:"情緒與理性的運作",subtitle:"Emotion & Reason",type:"reflection",
        summary:"情緒可以真實發生，理性也能同時分析；重點不是消除情緒，而是理解自己能控制什麼。",
        reflections:[
          {title:"情緒與理性雙軌並行",thought:`遇到會引發情緒的事情時，我會先感受到情緒本身，例如難過、流眼淚，接著腦袋會開始反思：為什麼我有這個情緒？我真正的感受是什麼？這件事真的造成了這麼大的傷害，還是情緒把它放大了？\n\n被罵的時候這件事尤其明顯。就算我知道問題點在哪裡、正在分析自己哪裡做錯、為什麼會這樣做、之後要怎麼改，我還是可能難過甚至掉眼淚。我沒有辦法只靠理性關掉生理上的情緒反應，但理性分析可以同時存在，兩條軌道並不衝突。`,tags:["後設認知","CBT：事實與想法分離"]},
          {title:"只處理自己能控制的部分",thought:`我認為自己不能改變別人，抱怨也不能改變已經發生的事實，所以遇到狀況時，我通常會很快接受現況，然後開始想能怎麼處理。\n\n我真正能控制的是自己的應對、判斷與改進；別人的反應、已發生的事情、別人的情緒則不是我能直接控制的。這也是為什麼我不太容易長時間停留在生氣或抱怨裡。`,tags:["控制二分法","Dichotomy of Control"]},
          {title:"興趣本身就足夠成為動機",thought:`我常常會一直問自己「我到底要做什麼？為什麼要做？」但想到最後，我發現答案其實沒有那麼複雜：因為我有興趣、因為我想做，這樣就夠了。\n\n我不需要靠它證明自己，也不需要先替結果焦慮，不需要把喜歡做的事變成一個一定要交付成果的責任。我就只是在做自己喜歡做的事。`,tags:["內在動機","Self-Determination Theory"]}
        ]
      },
      "meaning-freedom":{
        title:"存在意義與自由",subtitle:"Meaning & Freedom",type:"reflection",
        summary:"把社會規則拆回最底層，重新問：誰規定人一定要厲害、進步，或活成某一種標準答案？",
        reflections:[
          {title:"經驗不構成支配他人的資格",thought:`我從以前就會想：為什麼大人常覺得自己一定比小孩厲害？後來我覺得，很多時候只是因為大人經歷過比較多事情，知道某些狀況發生時該怎麼辦。但小孩也可以自己去踩那些坑、自己經歷，經驗上的差距不代表小孩本質上比較差。\n\n這又延伸成另一個問題：為什麼不夠厲害、不夠專業、不夠有知識、甚至不夠努力，就理所當然應該被罵？這些標準是人類社會建立的規則，不是宇宙本身的真理。\n\n如果把現代社會拆回最原始的生存狀態，人類至少要做到的是生存與繁衍；在那之外，我不認為每個人都必須向別人證明自己的價值。只要能靠自己活下去、知道自己喜歡什麼，並且活得開心，對我來說就已經成立。`,tags:["知識與權力","社會建構論","存在先於本質"]},
          {title:"生命沒有預設意義",thought:`我也思考過意識的本質與生命的意義，最後得到的結論是：生命沒有一個預先替所有人設定好的意義。\n\n每個人來到這個世界上，都有自己想達成的目標、想過的生活方式。既然沒有統一答案，那意義就是做自己真正想做的事，就是這麼簡單。`,tags:["積極虛無主義","存在主義"]}
        ]
      },
      "self-integration":{
        title:"自我整合與幸福",subtitle:"Self-Integration & Contentment",type:"reflection",
        summary:"低物慾、對當下生活的滿足，以及同時容納平淡、探索與持續思考的生活方式。",
        reflections:[
          {title:"如果重來一次，我仍會選現在的人生",thought:`我的物質慾望很低。看到很有錢、生活非常奢侈的人，我不太會產生羨慕或比較的感覺，因為我覺得自己現在已經很幸福。花錢大多集中在出去玩、吃好吃的、看醫生，以及像電腦這種會高頻使用、能拿來做很多事情和打遊戲的核心工具。\n\n我也很坦然承認自己有強烈的本能渴望，但在行動上會極度克制並尊重他人的邊界。我的人生目標很單純：活得開心、做自己想做的事。\n\n我很享受現在的生活，回頭看以前的事情也常覺得很好笑、很懷念。若能讓完全一樣的人生從頭再來一次，我會非常願意。我對其他人的生活也會有興趣，但最後還是覺得自己的生活最舒服。`,tags:["斯多葛式知足","Amor Fati","課題分離"]},
          {title:"平淡與遠方可以同時成立",thought:`我常覺得自己的喜好看起來很矛盾：我很喜歡跟自己愛的人悠閒、平淡地過生活，但同時也會想自己一個人去環遊世界、跑進深山，看不同的風景。\n\n後來我比較不把這理解成真正的矛盾。穩定的關係與日常可以是心理上的錨點，而獨自探索未知則是另一種驅力；我可以同時需要連結，也同時需要自由與探索。`,tags:["Secure Base","多重自我"]},
          {title:"日常中的逆向工程與心智模擬",thought:`我從以前就很習慣在洗澡、做家事、走路的時候讓腦袋自己開始運轉。看到旁邊的電線桿，就會開始想它是怎麼做的、上面的線各自是做什麼；遇到事情，又可能跳去想人生的意義、為什麼一定要進步或變強。\n\n想到遊戲或系統時，我也會開始模擬它應該怎麼設計、可能遇到哪些問題，聯想到玩過的遊戲或看過的動畫裡有什麼可以參考，然後在腦海裡一步一步把整個流程走完。`,tags:["逆向工程式思維","心智模擬","跨域聯想"]},
          {title:"小幸福本身就是生活",thought:`我的日常其實很單純：喜歡打遊戲、看動漫，也喜歡生活裡很小的幸福——吃吃喝喝、悠閒地散步、看看沿途的風景。\n\n我不需要每一段時間都在追求更大的成就；這些很普通的體驗本身，就是我真正喜歡的生活。`,tags:["微觀幸福","體驗導向"]}
        ]
      },
      "human-ethics":{
        title:"人性、倫理與人際邊界",subtitle:"Human Nature, Ethics & Boundaries",type:"reflection",
        summary:"承認人的存在平等，同時保留清楚的喜惡、真誠問題、求助方式與人際距離。",
        reflections:[
          {title:"人的本質平等與行為界線",thought:`我認為所有人類在本質上都是平等的。馬斯克、愛因斯坦、牛頓或任何普通人，一樣要吃飯、喝水，都有喜歡的事情，被罵也會不開心、會有情緒。\n\n以前我很難理解黑道、動不動就罵人或容易生氣的人，後來我會試著把他們也看成和我一樣呼吸、吃飯、活著的人。理解這件事，不代表我必須喜歡所有人的行為。對很頑固不聽勸、會陷害人、虐待人、完全不顧別人死活的行為，我仍然會有非常明確的厭惡。\n\n所以對我來說，「所有人作為人是平等的」和「我可以討厭某些行為或某些人」完全可以同時成立。`,tags:["存在平等","寬容悖論"]},
          {title:"表現出的善意與內心真實",thought:`我思考過，一個人表現出來的行為和他心裡真正的想法，到底哪一個更重要。\n\n假設一個人一輩子都對我非常好，直到去世，即使他內心其實極度討厭我，我的一生仍然可能因為他的行為而感到幸福。相反，如果一個人心裡極度喜歡我，卻因為某些原因一直無法表達，表現甚至讓我誤以為他討厭我，那我可能到他去世都不會知道真相。\n\n如果一個人不在乎別人心裡怎麼想，第一種或許更好；如果一個人真正想理解、同理對方，第二種內在真實又可能更重要。但最後我發現，整個問題有一個更底層的限制：人可能說謊，我們本質上不可能完全確認另一個人的內心。`,tags:["結果論","動機論","他者心靈問題"]},
          {title:"信任、求助、認可與距離",thought:`遇到困難時，我會向自己信任的人或專業人士求助，也會把事情完整告訴伴侶；如果信任的人給出的反應不好，我之後就會收斂。對專業人士，我通常只講問題本身，不太講情緒。\n\n雖然我常說不需要向別人證明自己，但內心仍然會有想被自己崇拜的人認可的渴望，例如想像和馬斯克聊天、被 OpenAI 邀請，或看到身邊的人露出驚訝的表情。不過我知道那是想像，也會把自己拉回現實。\n\n對討厭的人，我通常不會正面表現厭惡或立刻斷絕關係，而是表面順著對方，私下盡量拉開距離、減少牽扯。`,tags:["情感邊界","外部認可","被動迴避策略"]}
        ]
      }
    };
'''
data_marker = '    const fictionWorks={'
if data_marker not in text:
    raise SystemExit('fictionWorks data marker not found')
text = text.replace(data_marker, data + '\n' + data_marker, 1)

old_state = 'let currentCategory="";let currentFictionWork="";const views=["portalPage","abilityPage","aboutPage","fictionPage","fictionDetailPage","disciplinePage","disciplinePeriodPage","categoryPage","projectPage"];'
new_state = 'let currentCategory="";let currentFictionWork="";let currentCognitionTheme="";const views=["portalPage","abilityPage","aboutPage","fictionPage","fictionDetailPage","disciplinePage","disciplinePeriodPage","cognitionPage","cognitionDetailPage","categoryPage","projectPage"];'
if old_state not in text:
    raise SystemExit('view state anchor not found')
text = text.replace(old_state, new_state, 1)

render = r'''
    function renderCognitionIndex(){const grid=document.getElementById("cognitionThemeGrid");grid.replaceChildren();let entries=0;cognitionThemeOrder.forEach(slug=>{const theme=cognitionThemes[slug];const isTheory=theme.type==="theory";entries+=isTheory?1:theme.reflections.length;const card=document.createElement("button");card.type="button";card.className="cognition-theme-card"+(isTheory?" developing":"");card.onclick=()=>openCognitionTheme(slug);const top=document.createElement("div");top.className="cognition-card-top";top.append(makeText("span","cognition-card-type",isTheory?"Developing theory":"Reflection theme"),makeText("span","cognition-card-count",isTheory?"Ongoing":String(theme.reflections.length).padStart(2,"0")+" reflections"));const title=makeText("h2","cognition-card-title",theme.title);const subtitle=makeText("span","cognition-card-subtitle",theme.subtitle);const summary=makeText("p","cognition-card-summary",theme.summary);const arrow=makeText("span","cognition-card-arrow","→");card.append(top,title,subtitle,summary,arrow);grid.appendChild(card)});document.getElementById("cognitionIndexSummary").textContent=cognitionThemeOrder.length+" themes · "+entries+" entries"}
    function appendCognitionTags(target,tags){const related=document.createElement("div");related.className="cognition-related";related.appendChild(makeText("span","cognition-related-label","Related concepts"));tags.forEach(tag=>related.appendChild(makeText("span","cognition-tag",tag)));target.appendChild(related)}
    function renderCognitionTheory(theme,target){const theory=theme.theory;const wrap=document.createElement("section");wrap.className="cognition-theory";const intro=document.createElement("div");intro.className="cognition-theory-intro";intro.append(makeText("p","cognition-theory-kicker","Original reasoning · ongoing"),makeText("p","cognition-theory-thesis",theory.thesis),makeText("p","cognition-theory-copy",theory.copy));appendCognitionTags(intro,theme.tags);const chain=document.createElement("div");chain.className="cognition-chain";theory.chain.forEach(item=>chain.appendChild(makeText("div","cognition-chain-step",item)));const steps=document.createElement("div");steps.className="cognition-theory-steps";theory.steps.forEach((copy,index)=>{const row=document.createElement("div");row.className="cognition-theory-step";row.append(makeText("span","cognition-theory-step-num",String(index+1).padStart(2,"0")),makeText("p","",copy));steps.appendChild(row)});const change=document.createElement("div");change.className="cognition-theory-change";change.append(makeText("strong","",theory.changeTitle),makeText("p","",theory.change));wrap.append(intro,chain,steps,change);target.appendChild(wrap)}
    function renderCognitionTheme(theme){document.getElementById("cognitionDetailTitle").textContent=theme.title;document.getElementById("cognitionDetailSubtitle").textContent=theme.subtitle;document.getElementById("cognitionDetailEyebrow").textContent="Ability · Cognition";const content=document.getElementById("cognitionDetailContent");content.replaceChildren();if(theme.type==="theory"){document.getElementById("cognitionDetailMeta").textContent=theme.status;document.getElementById("cognitionDetailMeta").className="cognition-detail-status";renderCognitionTheory(theme,content);return}document.getElementById("cognitionDetailMeta").textContent=theme.reflections.length+" reflections";document.getElementById("cognitionDetailMeta").className="";const list=document.createElement("div");list.className="cognition-reflection-list";theme.reflections.forEach((reflection,index)=>{const article=document.createElement("article");article.className="cognition-reflection";article.appendChild(makeText("span","cognition-reflection-index",String(index+1).padStart(2,"0")));const body=document.createElement("div");body.append(makeText("h2","cognition-reflection-title",reflection.title),makeText("p","cognition-thought",reflection.thought));appendCognitionTags(body,reflection.tags);article.appendChild(body);list.appendChild(article)});content.appendChild(list)}
'''
fn_marker = '    function showPortal(push=true)'
if fn_marker not in text:
    raise SystemExit('showPortal function marker not found')
text = text.replace(fn_marker, render + '\n' + fn_marker, 1)

show_anchor = 'function showAbout(push=true){activateView("aboutPage");if(push)setHash("#about");document.title="About me — KeeCharlotte"}'
show_insert = show_anchor + 'function showCognition(push=true){currentCategory="Cognition";currentCognitionTheme="";renderCognitionIndex();activateView("cognitionPage");if(push)setHash("#ability/Cognition");document.title="Cognition — KeeCharlotte"}function openCognitionTheme(slug,push=true){const theme=cognitionThemes[slug];if(!theme){showCognition(push);return}currentCategory="Cognition";currentCognitionTheme=slug;renderCognitionTheme(theme);activateView("cognitionDetailPage");if(push)setHash("#ability/Cognition/"+slug);document.title=theme.title+" — Cognition — KeeCharlotte"}'
if show_anchor not in text:
    raise SystemExit('showAbout anchor not found')
text = text.replace(show_anchor, show_insert, 1)

open_anchor = 'if(category==="Discipline"){showDiscipline(push);return}activateView("categoryPage")'
open_new = 'if(category==="Discipline"){showDiscipline(push);return}if(category==="Cognition"){showCognition(push);return}activateView("categoryPage")'
if open_anchor not in text:
    raise SystemExit('openCategory discipline anchor not found')
text = text.replace(open_anchor, open_new, 1)

back_anchor = 'function backToFiction(){backOrFallback("#ability/Fiction",()=>showFiction())}function backToDiscipline()'
back_new = 'function backToFiction(){backOrFallback("#ability/Fiction",()=>showFiction())}function backToCognition(){backOrFallback("#ability/Cognition",()=>showCognition())}function backToDiscipline()'
if back_anchor not in text:
    raise SystemExit('back navigation anchor not found')
text = text.replace(back_anchor, back_new, 1)

route_anchor = 'if(category==="Discipline"){if(parts[2]==="2022-08-2022-11")openDisciplinePeriod(false);else showDiscipline(false);return}if(!Object.prototype.hasOwnProperty.call(projects,category))'
route_new = 'if(category==="Discipline"){if(parts[2]==="2022-08-2022-11")openDisciplinePeriod(false);else showDiscipline(false);return}if(category==="Cognition"){if(parts[2]&&cognitionThemes[parts[2]])openCognitionTheme(parts[2],false);else showCognition(false);return}if(!Object.prototype.hasOwnProperty.call(projects,category))'
if route_anchor not in text:
    raise SystemExit('route discipline anchor not found')
text = text.replace(route_anchor, route_new, 1)

cognition_button = '<button class="category" type="button" onclick="openCategory(\'Cognition\')"><h2>Cognition</h2>'
cognition_button_available = '<button class="category available" type="button" onclick="openCategory(\'Cognition\')"><h2>Cognition</h2>'
if cognition_button not in text:
    raise SystemExit('Cognition category button anchor not found')
text = text.replace(cognition_button, cognition_button_available, 1)

responsive_anchor = '    @media(max-width:760px){body{padding:10px}'
responsive_new = '    @media(max-width:760px){.cognition-theme-grid{grid-template-columns:1fr}.cognition-theme-card.developing{grid-column:auto}.cognition-index-heading{align-items:flex-start;flex-direction:column;gap:7px}.cognition-detail-meta{align-items:flex-start;flex-direction:column;gap:7px}.cognition-reflection{grid-template-columns:34px minmax(0,1fr);gap:14px;padding:27px 0}.cognition-chain{grid-template-columns:1fr}.cognition-chain-step{min-height:68px}.cognition-chain-step:not(:last-child)::after{content:"↓";right:auto;left:50%;bottom:-13px;top:auto;transform:translateX(-50%)}.cognition-theory-intro{padding:22px}.cognition-card-summary{margin-right:28px}body{padding:10px}'
if responsive_anchor not in text:
    raise SystemExit('mobile media anchor not found')
text = text.replace(responsive_anchor, responsive_new, 1)

required = [
    'id="cognitionPage"','id="cognitionDetailPage"','const cognitionThemes=',
    'function showCognition','function openCognitionTheme','function backToCognition',
    'category==="Cognition"','cognition-theme-card"+(isTheory?" developing":"")',
    'class="category available" type="button" onclick="openCategory(\'Cognition\')"'
]
for item in required:
    if item not in text:
        raise SystemExit(f'Missing expected Cognition implementation: {item}')
for dom_id in ['cognitionPage','cognitionDetailPage','cognitionThemeGrid','cognitionDetailContent']:
    if text.count(f'id="{dom_id}"') != 1:
        raise SystemExit(f'Unexpected count for {dom_id}')

path.write_text(text, encoding='utf-8')
