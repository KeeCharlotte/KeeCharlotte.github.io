from pathlib import Path
import re

path = Path("index.html")
text = path.read_text(encoding="utf-8")

if 'id="survivalCategoryPage"' in text:
    print("Survival Skills hierarchy already updated.")
    raise SystemExit(0)


def replace_regex(source, pattern, replacement, label):
    updated, count = re.subn(pattern, replacement, source, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 match, found {count}")
    return updated


SURVIVAL_CSS = r'''

    /* Survival Skills · three-level knowledge hierarchy */
    .survival-main,.survival-category-main,.survival-detail-main{max-width:1120px;padding:48px 0 92px}.survival-hero{max-width:850px;padding:26px 0 48px}.survival-hero .detail-title{margin-bottom:20px}.survival-lede{max-width:800px;margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(24px,3vw,36px);font-weight:600;line-height:1.38;letter-spacing:-.012em}.survival-lede-zh{max-width:760px;margin:10px 0 0;color:var(--muted);font-size:15px;line-height:1.85}
    .survival-index-section,.survival-subtree-section,.survival-references,.survival-article{border-top:1px solid var(--line);padding-top:32px}.survival-index-heading,.survival-section-heading{display:flex;align-items:baseline;justify-content:space-between;gap:24px;margin-bottom:20px}.survival-index-heading h2,.survival-section-heading h2,.survival-references h2{margin:0;color:var(--rose);font-family:var(--mono);font-size:13px;font-weight:550;letter-spacing:.11em}.survival-index-heading span,.survival-section-heading span{color:var(--muted-readable);font-family:var(--mono);font-size:12px;letter-spacing:.06em}
    .survival-major-tree{display:grid;justify-items:center;padding:18px 0 8px}.survival-major-node{position:relative;width:min(100%,620px);display:grid;grid-template-columns:64px minmax(0,1fr) auto;align-items:center;gap:20px;min-height:132px;padding:25px 28px;border:1px solid var(--line-strong);border-radius:var(--radius-card);background:var(--card);cursor:pointer;text-align:left;transition:transform .24s var(--ease),border-color .2s ease,background .2s ease}.survival-major-node:hover,.survival-major-node:focus-visible{transform:translateY(-2px);border-color:var(--rose);background:var(--card-hover);outline:none}.survival-major-index{color:var(--rose);font-family:var(--mono);font-size:14px;letter-spacing:.08em}.survival-major-title{display:block;color:var(--text);font-family:var(--serif);font-size:clamp(28px,3.2vw,40px);font-weight:700;line-height:1.1}.survival-major-zh{display:block;margin-top:6px;color:var(--muted);font-size:15px}.survival-major-arrow{color:var(--rose);font-family:var(--mono);font-size:19px;transition:transform .2s ease}.survival-major-node:hover .survival-major-arrow,.survival-major-node:focus-visible .survival-major-arrow{transform:translateX(4px)}
    .survival-category-head,.survival-detail-head{padding:28px 0 42px}.survival-category-kicker,.survival-detail-kicker{margin:0 0 10px;color:var(--rose);font-family:var(--mono);font-size:13px;letter-spacing:.1em}.survival-category-title,.survival-detail-title{max-width:900px;margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(44px,6vw,72px);font-weight:700;line-height:1.04;letter-spacing:-.022em}.survival-category-zh,.survival-detail-zh{margin:8px 0 0;color:var(--muted);font-size:18px;line-height:1.6}.survival-category-intro,.survival-detail-intro{max-width:780px;margin:17px 0 0;color:var(--muted-readable);font-family:var(--mono);font-size:14px;line-height:1.75;letter-spacing:.025em}
    .survival-subtree{display:grid;justify-items:center}.survival-subtree-root,.survival-priority-node{width:min(100%,440px);padding:20px 23px;border:1px solid var(--line-strong);border-radius:var(--radius-card);background:var(--card);text-align:center}.survival-subtree-root .survival-node-en,.survival-priority-node .survival-node-en{font-size:23px}.survival-tree-line{width:1px;height:30px;background:var(--rose-soft);opacity:.8}.survival-subbranches{position:relative;width:100%;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;padding-top:22px}.survival-subbranches::before{content:"";position:absolute;top:0;left:8.3%;right:8.3%;height:1px;background:var(--line-strong)}.survival-subnode{position:relative;min-height:144px;padding:18px 15px;border:1px solid var(--line);border-radius:10px;background:rgba(26,20,32,.5);cursor:pointer;text-align:left;transition:transform .22s var(--ease),border-color .2s ease,background .2s ease}.survival-subnode::before{content:"";position:absolute;top:-22px;left:50%;width:1px;height:22px;background:var(--line-strong)}.survival-subnode:hover,.survival-subnode:focus-visible,.survival-priority-node:hover,.survival-priority-node:focus-visible{transform:translateY(-2px);border-color:var(--rose);background:var(--card-hover);outline:none}.survival-node-num{display:block;color:var(--rose);font-family:var(--mono);font-size:11px;letter-spacing:.08em}.survival-node-en{display:block;margin-top:7px;color:var(--text);font-family:var(--serif);font-size:19px;font-weight:700;line-height:1.18}.survival-node-zh{display:block;margin-top:5px;color:var(--muted);font-size:13px;line-height:1.5}.survival-priority-node{border-color:var(--rose-soft);cursor:pointer;transition:transform .22s var(--ease),border-color .2s ease,background .2s ease}
    .survival-reference-list{display:grid;margin-top:15px;border-top:1px solid var(--line)}.survival-reference{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:16px;align-items:center;padding:18px 0;border-bottom:1px solid var(--line)}.survival-reference-id{color:var(--rose);font-family:var(--mono);font-size:12px}.survival-reference-title{color:var(--text);font-size:14px;line-height:1.6}.survival-reference-meta{display:block;margin-top:4px;color:var(--muted);font-size:13px;line-height:1.7}.survival-reference-arrow{color:var(--rose);font-family:var(--mono);font-size:15px}.survival-reference:hover .survival-reference-title{color:var(--rose)}.survival-disclaimer{max-width:840px;margin:18px 0 0;color:var(--muted-dark);font-size:12px;line-height:1.75}
    .survival-article{display:grid;gap:28px}.survival-content-section{padding-bottom:28px;border-bottom:1px solid var(--line)}.survival-content-section:last-child{border-bottom:0;padding-bottom:0}.survival-content-section h2{margin:0;color:var(--text);font-family:var(--serif);font-size:clamp(25px,3vw,34px);font-weight:700;line-height:1.2}.survival-content-section p{max-width:850px;margin:13px 0 0;color:var(--text);font-size:16px;line-height:1.95}.survival-content-section ul{max-width:850px;margin:13px 0 0;padding:0;list-style:none}.survival-content-section li{position:relative;margin-top:9px;padding-left:18px;color:var(--text);font-size:16px;line-height:1.9}.survival-content-section li::before{content:"·";position:absolute;left:3px;color:var(--rose)}.survival-key-principle{padding:20px 22px;border-left:2px solid var(--rose);background:rgba(141,123,178,.05)}.survival-key-principle h2{font-size:21px}.survival-key-principle p{color:var(--text);font-family:var(--serif);font-size:19px;line-height:1.65}
    @media(max-width:900px){.survival-subbranches{grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;padding-top:0}.survival-subbranches::before,.survival-subnode::before{display:none}}
    @media(max-width:760px){.survival-index-heading,.survival-section-heading{align-items:flex-start;flex-direction:column;gap:7px}.survival-major-node{grid-template-columns:42px minmax(0,1fr) auto;padding:22px 20px;gap:13px}.survival-subbranches{grid-template-columns:1fr}.survival-subnode{min-height:0}.survival-reference{grid-template-columns:36px minmax(0,1fr) auto}.survival-category-head,.survival-detail-head{padding-top:20px}}
'''

SURVIVAL_HTML = r'''

  <div id="survivalPage" class="view subpage"><div class="shell"><nav class="topbar" aria-label="Survival Skills navigation"><button class="brand" type="button" onclick="showPortal()">KeeCharlotte</button><button class="back-link" type="button" onclick="backToAbility()">← Ability</button></nav><main class="survival-main"><header class="survival-hero"><p class="eyebrow">Ability · Survival Skills</p><h1 class="detail-title">Survival Skills</h1><p class="survival-lede">A record of the wilderness survival knowledge I am currently learning.</p><p class="survival-lede-zh">這裡介紹我目前學到的荒野求生知識。</p></header><section class="survival-index-section" aria-labelledby="survivalMajorTitle"><div class="survival-index-heading"><h2 id="survivalMajorTitle">Knowledge Tree</h2><span>Major categories</span></div><div class="survival-major-tree"><button class="survival-major-node" type="button" onclick="openSurvivalCategory('situation-assessment')"><span class="survival-major-index">01</span><span><span class="survival-major-title">Situation Assessment</span><span class="survival-major-zh">情境評估</span></span><span class="survival-major-arrow" aria-hidden="true">→</span></button></div></section></main><footer>© 2026 KeeCharlotte</footer></div></div>

  <div id="survivalCategoryPage" class="view subpage"><div class="shell"><nav class="topbar" aria-label="Situation Assessment navigation"><button class="brand" type="button" onclick="showPortal()">KeeCharlotte</button><button class="back-link" type="button" onclick="backToSurvival()">← Survival Skills</button></nav><main class="survival-category-main"><header class="survival-category-head"><p class="survival-category-kicker">Survival Skills · 01</p><h1 class="survival-category-title">Situation Assessment</h1><p class="survival-category-zh">情境評估</p><p class="survival-category-intro">Assess the situation before deciding what to do next.</p></header><section class="survival-subtree-section" aria-labelledby="survivalSubtreeTitle"><div class="survival-section-heading"><h2 id="survivalSubtreeTitle">Subtopic Tree</h2><span>Select a topic to study</span></div><div class="survival-subtree"><div class="survival-subtree-root"><span class="survival-node-num">01</span><span class="survival-node-en">Situation Assessment</span><span class="survival-node-zh">情境評估</span></div><div class="survival-tree-line" aria-hidden="true"></div><div class="survival-subbranches">
    <button class="survival-subnode" type="button" onclick="openSurvivalDetail('threats')"><span class="survival-node-num">01.1</span><span class="survival-node-en">Immediate Threats</span><span class="survival-node-zh">立即危險</span></button>
    <button class="survival-subnode" type="button" onclick="openSurvivalDetail('body')"><span class="survival-node-num">01.2</span><span class="survival-node-en">Physical Condition</span><span class="survival-node-zh">身體狀況</span></button>
    <button class="survival-subnode" type="button" onclick="openSurvivalDetail('environment')"><span class="survival-node-num">01.3</span><span class="survival-node-en">Environment</span><span class="survival-node-zh">環境條件</span></button>
    <button class="survival-subnode" type="button" onclick="openSurvivalDetail('location')"><span class="survival-node-num">01.4</span><span class="survival-node-en">Location &amp; Time</span><span class="survival-node-zh">位置與時間</span></button>
    <button class="survival-subnode" type="button" onclick="openSurvivalDetail('resources')"><span class="survival-node-num">01.5</span><span class="survival-node-en">Available Resources</span><span class="survival-node-zh">可用資源</span></button>
    <button class="survival-subnode" type="button" onclick="openSurvivalDetail('rescue')"><span class="survival-node-num">01.6</span><span class="survival-node-en">Rescue Situation</span><span class="survival-node-zh">獲救可能</span></button>
  </div><div class="survival-tree-line" aria-hidden="true"></div><button class="survival-priority-node" type="button" onclick="openSurvivalDetail('priority')"><span class="survival-node-num">01.7</span><span class="survival-node-en">Priority Assessment</span><span class="survival-node-zh">判斷目前最大威脅</span></button></div></section><section class="survival-references" aria-labelledby="survivalReferencesTitle"><h2 id="survivalReferencesTitle">References</h2><div class="survival-reference-list"><a class="survival-reference" href="https://www.redcross.org/take-a-class/first-aid/performing-first-aid/first-aid-steps" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R1</span><span class="survival-reference-title">American Red Cross · First Aid Steps<span class="survival-reference-meta">現場安全、反應狀態、呼吸與危及生命的出血評估。</span></span><span class="survival-reference-arrow">↗</span></a><a class="survival-reference" href="https://www.nps.gov/articles/gtgemergencyplan.htm" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R2</span><span class="survival-reference-title">U.S. National Park Service · Outdoor Emergency Plan<span class="survival-reference-meta">停止盲目行動、確認位置、立即危險例外、資源盤點與求救原則。</span></span><span class="survival-reference-arrow">↗</span></a><a class="survival-reference" href="https://www.nps.gov/articles/10essentials.htm" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R3</span><span class="survival-reference-title">U.S. National Park Service · Ten Essentials<span class="survival-reference-meta">導航、急救、水分、緊急庇護與天候暴露等野外基本風險。</span></span><span class="survival-reference-arrow">↗</span></a><a class="survival-reference" href="https://www.wms.org/WMS/Research/WEM/Clinical-Practice-Guidelines.aspx" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R4</span><span class="survival-reference-title">Wilderness Medical Society · Clinical Practice Guidelines<span class="survival-reference-meta">野外創傷與環境疾病的循證臨床指引索引。</span></span><span class="survival-reference-arrow">↗</span></a><a class="survival-reference" href="https://wms.org/magazine/magazine/1260/2020hypothermia-CPG/default.aspx" target="_blank" rel="noopener noreferrer"><span class="survival-reference-id">R5</span><span class="survival-reference-title">Wilderness Medical Society · Accidental Hypothermia Guideline<span class="survival-reference-meta">失溫、淨熱量流失與野外依臨床表現進行評估的相關原則。</span></span><span class="survival-reference-arrow">↗</span></a></div><p class="survival-disclaimer">本區為學習紀錄，不取代合格急救、野外醫學訓練或當地緊急服務；涉及醫療與救援的內容會隨較新的高品質證據更新。</p></section></main><footer>© 2026 KeeCharlotte</footer></div></div>

  <div id="survivalDetailPage" class="view subpage"><div class="shell"><nav class="topbar" aria-label="Survival topic navigation"><button class="brand" type="button" onclick="showPortal()">KeeCharlotte</button><button class="back-link" type="button" onclick="backToSurvivalCategory()">← Situation Assessment</button></nav><main class="survival-detail-main"><header class="survival-detail-head"><p id="survivalDetailKicker" class="survival-detail-kicker">Survival Skills · 01.1</p><h1 id="survivalTopicTitle" class="survival-detail-title"></h1><p id="survivalTopicZh" class="survival-detail-zh"></p><p id="survivalTopicIntro" class="survival-detail-intro"></p></header><div id="survivalTopicBody" class="survival-article"></div></main><footer>© 2026 KeeCharlotte</footer></div></div>
'''

SURVIVAL_JS = r'''
    const survivalAssessmentNodes={
      threats:{num:"01.1",titleEn:"Immediate Threats",titleZh:"立即危險",introEn:"Identify hazards that can cause serious harm before slower survival problems matter.",sections:[
        {title:"先確認目前位置是否安全",items:["觀察是否存在正在發生或快速接近的危險，例如火與濃煙、急流或快速上漲的水、雷擊暴露、落石、倒木、懸崖、不穩定地面等。","注意足以在短時間內造成嚴重傷害的動物或其他移動威脅。","如果寒冷、炎熱或其他暴露已經快速影響意識、行動或身體功能，也必須視為迫切問題。"]},
        {title:"判斷是否必須立刻移動",items:["如果目前位置本身正在造成直接生命威脅，先移到較安全的位置，再繼續其他評估。","移動前仍要快速確認路徑本身是否會帶來新的危險；逃離一個威脅不代表任何方向都安全。","若沒有立即威脅，不要因為緊張而把不確定性變成新的風險，例如毫無方向地快速移動。"]},
        {title:"重新評估",text:"離開危險位置後要重新觀察環境與身體狀況。一次判斷安全，不代表之後仍然安全；火勢、水位、天候、動物位置與自身能力都可能改變。"}
      ],principle:"先處理能在最短時間內造成死亡或嚴重失能的威脅；但『立即危險』指的是迫近的實際風險，不是把所有可能發生的事情都當成最高優先。"},
      body:{num:"01.2",titleEn:"Physical Condition",titleZh:"身體狀況",introEn:"Check what your body can safely do before choosing a plan.",sections:[
        {title:"先找可能危及生命的問題",items:["確認自己的意識是否清楚，能不能理解環境並做出連貫判斷。","注意呼吸是否明顯困難，以及是否存在大量、持續且難以控制的出血。","若有嚴重外傷、劇烈疼痛或明顯失去肢體功能，後續移動、取水與搭建庇護的計畫都必須重新估算。"]},
        {title:"確認實際行動能力",items:["測試自己能否安全站立、行走、抓握與協調動作，而不是只以『感覺還可以』判斷。","觀察是否有持續發抖、動作變笨拙、異常疲倦、頭暈、意識改變或其他冷熱壓力跡象。","口渴、疲勞與疼痛都會影響判斷與行動；應持續比較症狀是否正在惡化。"]},
        {title:"讓計畫符合身體能力",text:"同一條路、同一個水源或同一個庇護位置，對健康的人與受傷、失溫或極度疲勞的人並不是同一個距離。計畫必須以當下真正能安全完成的行動為基準。"}
      ],principle:"先處理危及生命的身體問題，再用剩餘能力規劃後續行動；不要假設自己仍具有受傷前的速度、力量與判斷品質。"},
      environment:{num:"01.3",titleEn:"Environment",titleZh:"環境條件",introEn:"Read the combination of weather, exposure, terrain, and change over time.",sections:[
        {title:"不要只看單一氣溫",items:["氣溫只是其中一個變數；風、身體是否潮濕、降雨或降雪、日照與陰影會共同影響人體的熱量得失。","相同氣溫下，乾燥無風與全身濕透又有強風，對人體造成的壓力可以完全不同。","炎熱環境也要同時觀察日照、遮陰、濕度與活動強度，而不是只看溫度數字。"]},
        {title:"讀地形與天候變化",items:["觀察坡度、鬆動地面、水道、植被、天然遮蔽與可能的落石或積水區。","注意雲層、風勢、降水、雷聲、氣溫趨勢與其他能表示天候正在改變的跡象。","現在可以忍受的環境，不代表幾小時後仍可忍受；天黑、下雨、起風或身體變濕都可能改變優先順序。"]},
        {title:"尋找環境同時提供的保護",text:"環境不只有威脅，也可能提供陰影、擋風處、天然庇護、乾燥地面或其他保護。評估時要同時看到風險與可利用條件。"}
      ],principle:"判斷的是『環境對人體造成的綜合壓力以及它正在如何變化』，而不是把某一個天氣數值直接等同於安全或危險。"},
      location:{num:"01.4",titleEn:"Location & Time",titleZh:"位置與時間",introEn:"Know where you are, how certain you are, and how much usable time remains.",sections:[
        {title:"確認已知位置與證據",items:["先確認自己是否知道目前位置；如果不知道，回想最後一個可以確定的位置。","尋找能固定位置資訊的地標與人類痕跡，例如步道、道路、海岸、稜線、河流、建築或其他基礎設施。","把『我確定知道』與『我猜應該是』分開；方向感本身不等於可靠的位置資訊。"]},
        {title:"判斷移動是否會增加資訊",items:["只有在確定能安全沿已知路線折返時，折返才是真正有資訊支持的選項。","若已迷失又無法安全確認方向，持續亂走可能讓自己離最後已知位置更遠，也增加搜救範圍。","存在立即生命威脅時，離開危險位置仍然優先。"]},
        {title:"把時間放進決策",items:["估計剩餘日照，並觀察天候與氣溫是否會在短時間內明顯改變。","需要移動、找材料或搭建庇護的工作，都會消耗日照與體力；不能把時間視為無限資源。"]}
      ],principle:"優先保留可靠的位置資訊。當方向不確定時，沒有根據的移動不是探索，而可能是在降低之後找到路或被找到的機率。"},
      resources:{num:"01.5",titleEn:"Available Resources",titleZh:"可用資源",introEn:"Look for useful water, terrain, materials, shelter, and human-made signs around you.",sections:[
        {title:"資源不只等於可以撿進背包的物品",items:["天然遮蔽、陰影、岩壁、倒木、乾燥地面與擋風地形本身就可能具有生存價值。","木材、石頭、植物纖維與其他材料的價值取決於當下需要解決的問題，以及取得與加工的成本。","道路、建築、垃圾、反光材料、足跡或其他人工痕跡，也可能提供庇護、工具材料或求救線索。"]},
        {title:"先觀察，再決定是否取得",items:["看到水源不代表可以直接飲用；外觀清澈也不能證明沒有微生物或其他污染。","距離很遠的資源可能需要付出大量體力、時間與熱量，途中也可能暴露在新的地形或天候風險中。","取得一項資源前要問：它能解決哪個目前問題？取得成本是多少？使用它會不會創造新的風險？"]},
        {title:"盤點可以轉換成能力的東西",text:"在沒有裝備時，關鍵不是尋找特定現代用品，而是辨認周遭物質與地形能提供的功能，例如遮蔽、隔熱、盛裝、切削、固定、燃料或訊號。"}
      ],principle:"資源的價值不是固定的。它取決於當前威脅、距離、品質、取得成本與使用後的副作用。"},
      rescue:{num:"01.6",titleEn:"Rescue Situation",titleZh:"獲救可能",introEn:"Estimate whether help is likely and whether moving will make you easier or harder to find.",sections:[
        {title:"先判斷有沒有人可能開始找你",items:["有人是否知道你失蹤、出發地點、預定路線與原本應該返回的時間？","如果這些資訊已被他人知道，搜救通常會從有限的已知範圍開始，而不是隨機搜尋整片區域。","如果沒有人知道你在哪裡或何時失蹤，自救與主動尋找人類活動跡象的重要性可能提高。"]},
        {title:"觀察附近人類活動與求救機會",items:["道路、步道、建築、燈光、聲音、船隻、車輛與飛行器都可能改變獲救機率。","評估目前位置是否容易被看見或聽見，以及是否存在安全且有效的訊號方式。","不要只問『能不能走出去』，也要問移動後會不會讓原本可能找到你的人失去線索。"]},
        {title:"留在原地與自救都不是絕對規則",text:"如果目前位置安全、有人知道你的路線且搜救可能開始，維持可被找到的位置通常具有價值；若目前位置存在危險，或有高度可信且安全的自救路線，移動可能更合理。"}
      ],principle:"把『被找到的可能性』視為生存條件之一。移動的收益必須大於失去可搜尋位置與增加暴露風險的成本。"},
      priority:{num:"01.7",titleEn:"Priority Assessment",titleZh:"判斷目前最大威脅",introEn:"Combine the six assessments and decide what deserves attention first.",sections:[
        {title:"比較問題的時間尺度",items:["哪一個威脅最可能在最短時間內造成死亡或嚴重失能？","哪一個問題已經開始降低你處理其他問題的能力，例如失血、失溫、熱疾病、嚴重受傷或意識惡化？","哪些問題雖然重要，但目前仍有較長的安全處理時間？"]},
        {title:"比較行動的代價與可逆性",items:["某個行動會消耗多少體力、日照、材料與水分？","如果判斷錯誤，能否容易回到原本狀態，還是會永久離開已知位置、失去資源或讓身體狀況惡化？","解決一個問題是否會惡化另一個問題，例如為了找水長距離移動，卻同時增加失溫或迷失風險？"]},
        {title:"行動後重新評估",text:"優先順序不是一次決定後永遠不變。環境、身體、位置、資源與獲救可能都會改變，因此完成重要行動或情況明顯變化後，要重新跑一次評估。"}
      ],principle:"沒有固定的『永遠先火、再水、再食物』順序。合理的第一步取決於當下哪一個問題最可能造成近期生命或能力損失，以及你能採取什麼代價最低且有效的行動。"}
    };

    function renderSurvivalDetail(slug){const node=survivalAssessmentNodes[slug];if(!node)return false;document.getElementById("survivalDetailKicker").textContent="Survival Skills · "+node.num;document.getElementById("survivalTopicTitle").textContent=node.titleEn;document.getElementById("survivalTopicZh").textContent=node.titleZh;document.getElementById("survivalTopicIntro").textContent=node.introEn;const body=document.getElementById("survivalTopicBody");body.replaceChildren();node.sections.forEach(section=>{const article=document.createElement("section");article.className="survival-content-section";article.appendChild(makeText("h2","",section.title));if(section.text)article.appendChild(makeText("p","",section.text));if(section.items){const list=document.createElement("ul");section.items.forEach(item=>list.appendChild(makeText("li","",item)));article.appendChild(list)}body.appendChild(article)});const principle=document.createElement("section");principle.className="survival-content-section survival-key-principle";principle.append(makeText("h2","","核心判斷原則"),makeText("p","",node.principle));body.appendChild(principle);return true}
    function showSurvival(push=true){currentCategory="Survival Skills";activateView("survivalPage");if(push)setHash("#ability/Survival%20Skills");document.title="Survival Skills — KeeCharlotte"}
    function openSurvivalCategory(slug="situation-assessment",push=true){if(slug!=="situation-assessment"){showSurvival(push);return}currentCategory="Survival Skills";activateView("survivalCategoryPage");if(push)setHash("#ability/Survival%20Skills/situation-assessment");document.title="Situation Assessment — Survival Skills — KeeCharlotte"}
    function openSurvivalDetail(slug,push=true){if(!renderSurvivalDetail(slug)){openSurvivalCategory("situation-assessment",push);return}currentCategory="Survival Skills";activateView("survivalDetailPage");if(push)setHash("#ability/Survival%20Skills/situation-assessment/"+slug);document.title=survivalAssessmentNodes[slug].titleEn+" — Survival Skills — KeeCharlotte"}
    function backToSurvival(){backOrFallback("#ability/Survival%20Skills",()=>showSurvival())}
    function backToSurvivalCategory(){backOrFallback("#ability/Survival%20Skills/situation-assessment",()=>openSurvivalCategory("situation-assessment"))}


    const fictionWorks='''

text = replace_regex(
    text,
    r'\n    /\* Survival Skills · Situation Assessment \*/.*?(?=\n    footer\{)',
    SURVIVAL_CSS,
    "Survival CSS",
)

text = replace_regex(
    text,
    r'\n  <div id="survivalPage".*?(?=\n  <div id="categoryPage")',
    SURVIVAL_HTML,
    "Survival HTML",
)

text = replace_regex(
    text,
    r'\n    const survivalAssessmentNodes=\{.*?\n\n\n    const fictionWorks=',
    SURVIVAL_JS,
    "Survival JavaScript block",
)

old_views = 'const views=["portalPage","abilityPage","aboutPage","fictionPage","fictionDetailPage","disciplinePage","disciplinePeriodPage","cognitionPage","cognitionDetailPage","survivalPage","categoryPage","projectPage"]'
new_views = 'const views=["portalPage","abilityPage","aboutPage","fictionPage","fictionDetailPage","disciplinePage","disciplinePeriodPage","cognitionPage","cognitionDetailPage","survivalPage","survivalCategoryPage","survivalDetailPage","categoryPage","projectPage"]'
if old_views not in text:
    raise RuntimeError("views registry anchor not found")
text = text.replace(old_views, new_views, 1)

old_route = 'if(category==="Survival Skills"){const survivalNode=parts[2]&&survivalAssessmentNodes[parts[2]]?parts[2]:"root";showSurvival(false,survivalNode);return}'
new_route = 'if(category==="Survival Skills"){if(!parts[2]){showSurvival(false);return}if(parts[2]==="situation-assessment"){if(parts[3]&&survivalAssessmentNodes[parts[3]])openSurvivalDetail(parts[3],false);else openSurvivalCategory("situation-assessment",false);return}showSurvival(false);return}'
if old_route not in text:
    raise RuntimeError("Survival route anchor not found")
text = text.replace(old_route, new_route, 1)

for forbidden in [
    "A decision-based survival knowledge system built from real-world evidence",
    "Baseline scenario · alone · naked · outdoors · no equipment",
    "REALITY TRANSFER",
    "SIMULATION TRANSFER",
    "Survival Truth Rule",
    "SIMULATION VARIABLES",
]:
    if forbidden in text:
        raise RuntimeError(f"forbidden public text still present: {forbidden}")

required = [
    'id="survivalPage"',
    'id="survivalCategoryPage"',
    'id="survivalDetailPage"',
    "openSurvivalCategory('situation-assessment')",
    "openSurvivalDetail('threats')",
    'const survivalAssessmentNodes=',
    '核心判斷原則',
    'References',
]
for token in required:
    if token not in text:
        raise RuntimeError(f"required token missing: {token}")

path.write_text(text, encoding="utf-8")
print("Restructured Survival Skills into home -> major category -> detail pages.")
