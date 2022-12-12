const chai = require('chai');
const chaiHttp = require('chai-http');


const server = "http://localhost:8000";


//assertions
chai.should();
chai.use(chaiHttp);


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwODc3NjEzLCJqdGkiOiI4ZTg2MDk2YTBkNDE0NTkyYTRkNDU0OWM4OTZlYjY2YSIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoicGF1bG5kYW1ibyJ9.T5G9eZvzEcVPF3lIboOTb4HWlI9H2skTEPIqceqSN_I"

describe("Get User Bills", () => {
  //get all Bank Accounts
  describe("GET /finance/bills/", () => {
    it("Should Get All User Bills", (done) => {
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

    //Should not get bills without authentications
    it("Should not get any bills", (done) => {
        chai.request(server)
            .get("/finance/bills")
            .end((err, response) => {
                response.should.status(401);
        done();
        });
    });

    //Get A Single Bill
    it("Should Get Single Bill When Given Bill ID", (done) => {
        billId = 4
        chai.request(server)
            .get(`/finance/bills/${billId}`)
            .set("Authorization", "Bearer " + token)
            .end((err, response) => {
                response.should.have.status(200);
                response.body.should.have.property("name");
                response.body.should.be.a("object");
            done();
        });
    });
  });


  describe("Create User Bills", () => {
    describe("POST /finance/bills/", () => {
        //When Authenticated, should be able to create a bill
        it("should create a bill", (done) => {
            bill = {
                "name": "Safaricom Internet",
                "bill_type": "basic",
                "allocated": 5000,
                "expenditure": 0,
                "budget": 2
            }
            chai
                .request(server)
                .post("/finance/bills/")
                .set("Content-Type", "application/json")
                .set("Connection", "keep alive")
                .send(bill)
                .set("Authorization", "Bearer " + token)
                .end((err, response) => {
                    response.should.have.status(201);
                done();
            });
        });
        //When not unauthorized should be unable to create a bill
        it("should not create a bill", (done) => {
          bill = {
            name: "Safaricom Internet",
            bill_type: "basic",
            allocated: 5000,
            expenditure: 0,
            budget: 2,
          };
          chai
            .request(server)
            .post("/finance/bills/")
            .set("Content-Type", "application/json")
            .set("Connection", "keep alive")
            .send(bill)
            //.set("Authorization", "Bearer " + token)
            .end((err, response) => {
              response.should.have.status(401);
              done();
            });
        });
    });
  });

});