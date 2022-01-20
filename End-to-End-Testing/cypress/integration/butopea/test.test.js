/// <reference types="cypress" />

describe('SystemIntegrationBackendPreliminaryTestCase',()=>{
    const baseUrl = 'https://butopea.com'
    // Visiting the root url in each test
    beforeEach(() => {
        cy.visit('https://butopea.com')
    });

    it('Should confirm if the second square contains an image, if it does, then it should extract the img url',()=>{
        // Checking if the second square contains an image
        cy.get('div.banner-square-image').eq(1).find("img").should('exist')
          .invoke('attr', 'src').then((ImgSrc)=> {
              cy.log(baseUrl+ImgSrc)
        })
        // Check if the square exist
        cy.get('div.banner-square-overlay-container').eq(0).should('exist')
        // find and check if the paragraph of the square exists, if it does then shows its text
        cy.get('div.banner-square-overlay-container').eq(0).find("p").should('exist').invoke('text').then((text)=> {
            cy.log(text)
        })
        cy.get('div.banner-square-overlay-container').eq(0).find("div.banner-square-overlay-cta").should('exist').invoke('text').then((text)=> {
            cy.log(text)
        })
        

    });

    it('Should click on the new products tab, let the tab load, and check if contains a list of products, if it does, extract each product infos',()=>{

        // 1. Click on the new products tab and check if it's active
        cy.get('nav > div div').last().click()
        cy.get('nav > div div').last().should('have.class', 'active')

        // 2. Check if contains a list of products
        cy.get('.product-listing').should('exist')

        // 3. Extracting each product infos
        // getting the product infos
        cy.get('.product-listing div > .product').each(($el,index) => {
            index+=1
            cy.log(index + " Product's Link: " + baseUrl + $el.find('a[data-testid=productLink]').attr('href'))
            cy.log(index + " Product's Title: " + $el.find('p.product-name').text())
            cy.log(index + " Product's Image Url: " + baseUrl + $el.find('img:eq(1)').attr('data-src'))
            cy.log(index + " Product's Price: "+baseUrl + $el.find('div.lh30').text())
        })
        //within(()=>{ cy.get('a')})
    })
})