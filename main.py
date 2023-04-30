from playwright.sync_api import sync_playwright
import pandas as pd
def main():
    with sync_playwright() as p:
        

        # IMPORTANT: Change dates to future dates, otherwise it won't work
       # checkin_date = '2023-03-23'
        #checkout_date = '2023-03-24'
        #card5 > div > div.vendor-card.extra-radius

        page_url = f'https://www.booking.com/searchresults.html?ss=New+Delhi%2C+India&efdco=1&label=bdot-Os1*aFx2GVFdW3rxGd0MYQS461499016018%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp9050497%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYriJK-Ikd_dLBPOo0BdMww&aid=378266&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2106102&dest_type=city&checkin=2023-04-30&checkout=2023-05-01&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(page_url, timeout=60000)

        hotels = page.locator('//div[@data-testid="property-card"]').all()
        print(f'There are: {len(hotels)} hotels.')

        hotels_list = []
        for hotel in hotels:
            hotel_dict = {}
            hotel_dict['Hotel Name'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            hotel_dict['Address'] = hotel.locator('//span[@data-testid="address"]').inner_text()
            hotel_dict['Price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            
            #hotel_dict['reviews']=hotel.locator('//div[@data-testid="review-score"]').all_inner_texts()[0]
            hotel_dict['Ratings out of 10']= hotel.locator('.b5cd09854e.d10a6220b4').all_inner_texts()
            hotel_dict['Review']=hotel.locator('.b5cd09854e.f0d4d6a2f5.e46e88563a').all_inner_texts()
            hotel_dict['No. of reviews']=hotel.locator('.d8eab2cf7f.c90c0a70d3.db63693c62').all_inner_texts()
            hotel_dict['Type of Room']=hotel.locator('.df597226dd').all_inner_texts()
            hotel_dict['Type of Bed']=hotel.locator('.cb5b4b68a4').all_inner_texts()
            '''if hotel.locator('.e05969d63d').all_inner_texts() =="[]":
                hotel_dict['Breakfast Included ']='Yes'
            else:
                hotel_dict['Breakfast Included ']="No"'''
            hotel_dict['Breakfast Included ']=hotel.locator('.e05969d63d').all_inner_texts()

            

            
            #<div class=""><div class="d8eab2cf7f">1 king bed</div></div>
    
          
           #span class="df597226dd">Deluxe Room</span>
           #<div class="">1 full bed</div>

            

                

            
            #hotel_dict['score'] = page.query_selector(".b5cd09854e d10a6220b4").inner_text()
            #hotel_dict['score']=hotel.locator('.b5cd09854e d10a6220b4').inner_text()
            #= ua.inner_text()
            
            #hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]').inner_text()
           #s hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]
           #<div aria-label="Scored 7.8 " class="b5cd09854e d10a6220b4">7.8</div>
           #<div class="d8eab2cf7f c90c0a70d3 db63693c62">1 review</div>

            hotels_list.append(hotel_dict)

        df = pd.DataFrame(hotels_list)
        df.to_excel('hotels_list.xlsx', index=False) 
        df.to_csv('hotels_list.csv', index=False) 
        browser.close()
if __name__ == '__main__':

    main()
