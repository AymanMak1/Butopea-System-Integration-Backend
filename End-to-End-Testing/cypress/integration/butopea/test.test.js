/// <reference types="cypress" />

describe('SystemIntegrationBackendPreliminaryTestCase',()=>{
    // Visiting the root url in each test
    beforeEach(() => {
        cy.visit('https://butopea.com')
    });

    it('Should confirm if the second square contains an image, if it does, then it should extract the img url',()=>{
        // Checking if the second square contains an image
        cy.get('div.banner-square-image').eq(1)
        .find("img").should('exist').then(img =>{
            cy.log(img)
        });

    });

    it('Should click on the new products tab, let the tab load, and check if contains a list of products, if it does, extract each product infos',()=>{
        // 1. Click on the new products tab
        cy.get('nav > div div').last().click()
        // 2. Check if contains a list of products
        cy.get('.product-listing').should('exist')
        // 3. Extracting each product infos
        // getting the link of the product and checking if it's valid or not
        
        cy.get('.product-listing div > .product').each(($el) => {
            //cy.log(``)
        })

        cy.get('.product-listing div > .product a').invoke('attr', 'href').then(href => {
            cy.request(href).its('status').should('eq', 200);
            cy.log("https://butopea.com" + href)
        });
    })
})