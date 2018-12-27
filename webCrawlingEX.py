# coding=utf-8

from selenium import webdriver

pageNum = 1
boardNum = 10
maxPageNum = 2
maxBoardNum = 3
initNum = 0
initPageNum = 1
dataNum = 1

browser = webdriver.Chrome(executable_path=r"chromedriver.exe 경로 기입")
browser.implicitly_wait(3)


with open('result.txt', 'w+') as f:
    for mpn in range(initPageNum, maxPageNum):
        browser.get('http://ㅅㄷㄴㅅㄴㄷㄱㄴㄷㅅㅈㄷㄱㄹㅈㄷㄱㄹㅈㄷㄹ?category=ㄹㄷㄹ&url=/fss/vstop/1436425918273&bbsid=1436425918273&page=%s' % mpn)
        # 크롤링 시작 페이지 겟
        categoryName = browser.title
        f.write('============================================================================================\n')
        f.write('카테고리 : ' + categoryName.encode('utf-8') + '\n')
        f.write('============================================================================================\n')

        for page in range(initNum, boardNum):
            al_list = browser.find_elements_by_class_name('t_al') #t_al 클라스 가져오기
            a_tag = al_list[page].find_element_by_tag_name('a') # a 태그 가저오기
            a_tag.click()
            title_tag = browser.find_element_by_class_name('tit').text
            audio_tag = browser.find_element_by_tag_name('audio')
            source_src = audio_tag.find_element_by_tag_name('source').get_attribute('src') # 오디오 소스 태그의 src 속성 가져오기
            tlanslation_text = None

            # f.write(str(dataNum) + '. ')
            # f.write(title_tag.encode('utf-8') + '\n')
            # f.write('--------------------------------------------------------------------------------------------\n')
            # f.write('|mp3 Download addr :  ' + source_src + '\n')
            # f.write('--------------------------------------------------------------------------------------------\n')
            # f.write('내용: \n' + '타이핑 결과물 없음\n')
            # f.write('============================================================================================\n')


            try:
                tlanslation_text = browser.find_element_by_class_name('b_scroll').text
                f.write(str(dataNum) + '. ')
                f.write(title_tag.encode('utf-8') + '\n')
                f.write('--------------------------------------------------------------------------------------------\n')
                f.write('|mp3 Download addr :  ' + source_src + '\n')
                f.write('--------------------------------------------------------------------------------------------\n')
                f.write('내용: \n' + tlanslation_text.encode('utf-8') + '\n' if tlanslation_text else '타이핑 결과물 없음\n')
                f.write('============================================================================================\n')

                f.write(tlanslation_text.encode('utf-8'))

            except Exception as ex:
                f.write(str(dataNum) + '. ')
                f.write(title_tag.encode('utf-8') + '\n')
                f.write('--------------------------------------------------------------------------------------------\n')
                f.write('|mp3 Download addr :  ' + source_src + '\n')
                f.write('--------------------------------------------------------------------------------------------\n')
                f.write('내용: \n' + '타이핑 결과물 없음\n'  )
                f.write('============================================================================================\n')
                # pass

            print(dataNum)
            # print(title_tag)
            # print(categoryName)
            # print(source_src)
            # print(tlanslation_text)
            dataNum += 1
            if dataNum > maxBoardNum:
                exit()
            browser.back()






