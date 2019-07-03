/// <reference types="cypress" />
describe('Oracle APEX Test', function() {
  it('Login demo', function() {
    cy.visit('/ords/f?p=100:LOGIN_DESKTOP')
    cy.get('#P9999_USERNAME').type('Hayden')
    cy.get('#P9999_USERNAME').type('hayden')
    cy.get('#P9999_PASSWORD').type('Oradoc_db1')
    cy.get('.t-Button').click()
    cy.get('#P1_COMMENT').type('hello')
    cy.get('#B1601598626035803').click()
    cy.get('.t-Region-headerItems--title')
  })
})