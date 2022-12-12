const chai = require("chai");
const server = "http://127.0.0.1:8000";
const chaiHttp = require("chai-http");

//assertions
chai.should();
chai.use(chaiHttp);

token =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwODc3NjEzLCJqdGkiOiI4ZTg2MDk2YTBkNDE0NTkyYTRkNDU0OWM4OTZlYjY2YSIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoicGF1bG5kYW1ibyJ9.T5G9eZvzEcVPF3lIboOTb4HWlI9H2skTEPIqceqSN_I";

describe("BANK ACCOUNTS API", () => {
  //get all Bank Accounts
  describe("GET /banking/bank-accounts/", () => {
    it("It should Get all Bank Accounts", (done) => {
      chai
        .request(server)
        .get("/finance/bills/")
        .set("Authorization", "Bearer " + token)
        .end((err, response) => {
          response.should.have.status(200);
          response.body.should.be.a("array");
          //response.body.length.should.be.eq(6)
          done();
        });
    });

    //Not Authenticated and Not Admin Should Not Get User Accounts
    it("It should not GET Bank Accounts", (done) => {
      chai
        .request(server)
        .get("/finance/bills/")
        .end((err, response) => {
          response.should.have.status(401);
          done();
        });
    });
  });

  /*
  //GET Authenticated User Bank Accounts
  describe("GET /banking/user-bank-accounts/", () => {
    it("It should Get Bank Accounts For Authenticated User", (done) => {
      chai
        .request(server)
        .get("/banking/user-bank-accounts/")
        .set("Authorization", "Bearer " + token)
        .end((err, response) => {
          response.should.have.status(200);
          done();
        });
    });

    it("It should Not Get User Bank Accounts If Not Authenticated", (done) => {
      chai
        .request(server)
        .get("/banking/user-bank-accounts/")
        .end((err, response) => {
          response.should.have.status(401);
          done();
        });
    });
  });

  //GET All Bank Transactions
  describe("GET /banking/all-bank-transactions/", () => {
    it("It should Get All Bank Transactions", (done) => {
      chai
        .request(server)
        .get("/banking/all-bank-transactions/")
        .set("Authorization", "Bearer " + token)
        .end((err, response) => {
          response.should.have.status(200);
          done();
        });
    });

    it("It should Not Get All Bank Transaction If Not Admin", (done) => {
      chai
        .request(server)
        .get("/banking/all-bank-transactions/")
        .end((err, response) => {
          response.should.have.status(401);
          done();
        });
    });
  });

  //GET Authenticated User Transactions
  describe("GET /banking/account-transactions/", () => {
    it("It should Get User Bank Transactions", (done) => {
      chai
        .request(server)
        .get("/banking/account-transactions/")
        .set("Authorization", "Bearer " + token)
        .end((err, response) => {
          response.should.have.status(200);
          done();
        });
    });

    it("It should Not Get User Bank Transaction If Not Authenticated", (done) => {
      chai
        .request(server)
        .get("/banking/account-transactions/")
        .end((err, response) => {
          response.should.have.status(401);
          done();
        });
    });
  });

  //GET User Transactions By Specific ID
  describe("GET /banking/user-transactions/", () => {
    it("It should Get User Bank Transactions By Specific ID", (done) => {
      userId = 1;
      chai
        .request(server)
        .get("/banking/user-transactions/" + userId)
        .set("Authorization", "Bearer " + token)
        .end((err, response) => {
          response.should.have.status(200);
          done();
        });
    });

    it("It should Get 0 Bank Transaction If User ID Does Not Exist", (done) => {
      userId = 70000;
      chai
        .request(server)
        .get("/banking/user-transactions/" + userId)
        .end((err, response) => {
          response.should.have.status(200);
          response.body.should.be.a("array");
          response.body.length.should.be.eq(0);
          done();
        });
    });
  });
*/
});
