from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

replacements = [
    (
        '''    <button class="survival-subnode" type="button" onclick="openSurvivalDetail('rescue')"><span class="survival-node-num">01.6</span><span class="survival-node-en">Rescue Situation</span><span class="survival-node-zh">獲救可能</span></button>\n''',
        ''
    ),
    (
        '''<button class="survival-priority-node" type="button" onclick="openSurvivalDetail('priority')"><span class="survival-node-num">01.7</span><span class="survival-node-en">Priority Assessment</span><span class="survival-node-zh">判斷目前最大威脅</span></button>''',
        '''<button class="survival-priority-node" type="button" onclick="openSurvivalDetail('priority')"><span class="survival-node-num">01.6</span><span class="survival-node-en">Priority Assessment</span><span class="survival-node-zh">判斷目前最大威脅</span></button>'''
    ),
    (
        '''停止盲目行動、確認位置、立即危險例外、資源盤點與求救原則。''',
        '''停止盲目行動、確認位置、立即危險例外與資源盤點。'''
    ),
    (
        '''本區為學習紀錄，不取代合格急救、野外醫學訓練或當地緊急服務；涉及醫療與救援的內容會隨較新的高品質證據更新。''',
        '''本區為學習紀錄，不取代合格急救或野外醫學訓練；涉及醫療與生存安全的內容會隨較新的高品質證據更新。'''
    ),
    (
        '''尋找能固定位置資訊的地標與人類痕跡，例如步道、道路、海岸、稜線、河流、建築或其他基礎設施。''',
        '''尋找能固定位置資訊的自然地標，例如海岸、稜線、河流交會處、山峰、谷地或辨識度高的岩層與地形。'''
    ),
    (
        '''若已迷失又無法安全確認方向，持續亂走可能讓自己離最後已知位置更遠，也增加搜救範圍。''',
        '''若已迷失又無法安全確認方向，持續亂走可能讓自己離最後已知位置更遠，也增加耗能、受傷與進一步迷失的風險。'''
    ),
    (
        '''優先保留可靠的位置資訊。當方向不確定時，沒有根據的移動不是探索，而可能是在降低之後找到路或被找到的機率。''',
        '''優先保留可靠的位置資訊。當方向不確定時，沒有根據的移動不是探索，而可能讓自己更難回到已知位置、增加耗能並擴大迷失程度。'''
    ),
    (
        '''introEn:"Look for useful water, terrain, materials, shelter, and human-made signs around you."''',
        '''introEn:"Look for useful water, terrain, shelter, and natural materials around you."'''
    ),
    (
        '''道路、建築、垃圾、反光材料、足跡或其他人工痕跡，也可能提供庇護、工具材料或求救線索。''',
        '''水流、動物足跡、裸露岩層、植被分布與地形變化，也能提供水源、材料、方向與環境條件的線索。'''
    ),
    (
        '''在沒有裝備時，關鍵不是尋找特定現代用品，而是辨認周遭物質與地形能提供的功能，例如遮蔽、隔熱、盛裝、切削、固定、燃料或訊號。''',
        '''在沒有裝備時，關鍵不是尋找特定現代用品，而是辨認周遭物質與地形能提供的功能，例如遮蔽、隔熱、盛裝、切削、固定、燃料或照明。'''
    ),
    (
        '''priority:{num:"01.7",titleEn:"Priority Assessment",titleZh:"判斷目前最大威脅",introEn:"Combine the six assessments and decide what deserves attention first."''',
        '''priority:{num:"01.6",titleEn:"Priority Assessment",titleZh:"判斷目前最大威脅",introEn:"Combine the five assessments and decide what deserves attention first."'''
    ),
    (
        '''環境、身體、位置、資源與獲救可能都會改變，因此完成重要行動或情況明顯變化後，要重新跑一次評估。''',
        '''環境、身體、位置與資源都會改變，因此完成重要行動或情況明顯變化後，要重新跑一次評估。'''
    ),
]

for old, new in replacements:
    if old not in html:
        raise SystemExit(f'Expected text not found:\n{old}')
    html = html.replace(old, new, 1)

# Remove the entire Rescue Situation knowledge object.
start_marker = '      rescue:{num:"01.6",titleEn:"Rescue Situation"'
end_marker = '      priority:{num:"01.6",titleEn:"Priority Assessment"'
start = html.find(start_marker)
if start == -1:
    raise SystemExit('Rescue object start not found')
end = html.find(end_marker, start)
if end == -1:
    raise SystemExit('Priority object marker not found after rescue object')
html = html[:start] + html[end:]

for forbidden in [
    "openSurvivalDetail('rescue')",
    'Rescue Situation',
    '獲救可能',
    '求救',
    '搜救',
    '被找到的可能性',
    '救援',
    'Combine the six assessments',
    'human-made signs',
    '人類痕跡',
    '人工痕跡',
]:
    if forbidden in html:
        raise SystemExit(f'Forbidden rescue/civilization-remnant wording remains: {forbidden}')

required = [
    '01.5</span><span class="survival-node-en">Available Resources',
    '01.6</span><span class="survival-node-en">Priority Assessment',
    'priority:{num:"01.6",titleEn:"Priority Assessment"',
    'Combine the five assessments and decide what deserves attention first.',
    '自然地標，例如海岸、稜線、河流交會處',
]
for token in required:
    if token not in html:
        raise SystemExit(f'Required post-change token missing: {token}')

path.write_text(html, encoding='utf-8')
print('Removed rescue assumptions from Survival Skills.')
