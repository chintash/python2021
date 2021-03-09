name = "shiva"

lname = "prasad"

list_of_numbers = []
for i in range(1, 10000):
    list_of_numbers.append(i)
print(name,  lname)


// import { assert, time } from "console";
import { Given, Then, When } from "cucumber";
import cli from "cucumber/lib/cli";
import { client } from "nightwatch-api";
// import { PAUSE } from "redux-persist";

const myProfilePage = client.page.my_profile_page();
let workFlowCount
// ------------  Update User Name Correctly Scenario  ----------------------------------
When("I visit MyProfile page", async () => {
  await myProfilePage.getText("@workFlowCount", function(result){
    workFlowCount = result.value
  })
  console.log(" ---- workFlowCount : ", workFlowCount)
  await myProfilePage.navigate();
});

Then("I can see my prfile page", async () => {
  await myProfilePage.waitForElementVisible("@pageTitle");
  await myProfilePage.assert.visible("@pageTitle");
});


Then("I verify Update Information button is disabled", async () => {
  try{

    await myProfilePage.waitForElementVisible("@userName");
    await myProfilePage.waitForElementVisible("@spinner")
    await myProfilePage.assert.visible("@spinner");
    // await myProfilePage.waitForElementNotVisible("@spinner")
  }
  catch(e){
    console.log("Warning !!!")
  }
  });

  Then("I update User name as {string}", async updateText => {
  try{

    await myProfilePage.waitForElementVisible("@userName");
    await myProfilePage.waitForElementVisible("@spinner")
    await myProfilePage.assert.visible("@spinner");
    await myProfilePage.waitForElementNotPresent("@spinner")
  }
  catch(e){
    console.log("Warning !!!")
  }

  await myProfilePage.setValue("@userName", ["", [client.Keys.CONTROL, "a"]]);
  await client.keys(client.Keys.DELETE);
  await client.pause(200);
  await myProfilePage.setValue("@userName", updateText);

});


Then("I click on Update Information button", async () => {
  await myProfilePage.click("@updateInfoButton")
  await myProfilePage.waitForElementVisible("@successMessage")
  await myProfilePage.assert.visible("@successMessage")
});

Then("A success message is displayed", async () => {
  let val
  await myProfilePage.pause(2000)
  await myProfilePage.getText("@successMessage", function(result){
    val = result.value
  })
  console.log("............  Value 2: ", val)

  await myProfilePage.assert.equal("Password Changed Successfully!", val)

});

Then("I update Company name as {string}", async updateText => {
  try{

    await myProfilePage.waitForElementVisible("@userName");
    await myProfilePage.waitForElementVisible("@spinner")
    await myProfilePage.assert.visible("@spinner");
    await myProfilePage.waitForElementNotPresent("@spinner")
  }
  catch(e){
    console.log("Warning !!!")
  }

  await myProfilePage.setValue("@userName", ["", [client.Keys.CONTROL, "a"]]);
  await client.keys(client.Keys.DELETE);
  await client.pause(200);
  await myProfilePage.setValue("@userName", updateText);

});


// ------------ Update User Name Incorrectly  ------------
When("I am on User Information tab", async () => {
    await client.pause(300)
    await myProfilePage.assert.visible("@panelHeader")
});

Then("I add User Name as {string}", async updateText  => {
    await myProfilePage.sendKeys("@userName", updateText);
});

Then("Error message should be displayed", async () => {
    await myProfilePage.waitForElementVisible("@inputErrorMessage")
    await myProfilePage.assert.visible("@inputErrorMessage")
    await myProfilePage.pause(10000)

});

// ------------ Email Address textbox should be disabled for editing scenario  ------------

Then("Email Address textbox should be disabled for editing", async () => {
  await myProfilePage.assert.attributeEquals("@emailID", "disabled", 'true')

});


// ------------  Update Password Scenario  ----------------------------------

Then("I wait for details to be fetched", async () => {

  try
  {
    await myProfilePage.waitForElementVisible("@spinner")
    await myProfilePage.assert.visible("@spinner");
    // await myProfilePage.waitForElementNotVisible("@spinner")
  }
  catch(e){
    console.log("Warning !!!")
  }
  });

When("I click on Password tab", async () => {
  await myProfilePage.pause(7000)

  await myProfilePage.assert.visible("@passwordTab")
  await myProfilePage.click("@passwordTab")
  let panelHeader
  await myProfilePage.getText("@panelHeader", function(result){
    panelHeader = result.value
  })
});

Then("I wait for the panel to load", async () => {

  try
  {
    await myProfilePage.waitForElementVisible("@oldPassword");
    await myProfilePage.waitForElementVisible("@spinner")
    await myProfilePage.assert.visible("@spinner");
    // await myProfilePage.waitForElementNotVisible("@spinner")
  }
  catch(e){
    console.log("Warning !!!")
  }
  });


Then("I enter {string} as new password", async password => {
  await myProfilePage.sendKeys("@newPassword", password)
});

// -------------  Acoount Plan Tab -------------

When("I click on Account Plan tab", async () => {
  await myProfilePage.pause(5000)

  await myProfilePage.assert.visible("@accountPlanTab")
  await myProfilePage.click("@accountPlanTab")
  let val
  await myProfilePage.getText("@panelHeader", function(result){
    val = result.value
  })
    await myProfilePage.assert.equal("Plan Details", val)
    await myProfilePage.pause(3000)

});

When("I verify the workflow count", async () => {
  let val
  await myProfilePage.getText("@planTabWorkflowCount", function(result){
    val = result.value
  })
  await myProfilePage.assert.equal(val[0], workFlowCount[1])

});
