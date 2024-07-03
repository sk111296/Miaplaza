using OpenQA.Selenium; 
using OpenQA.Selenium.Chrome; 
using OpenQA.Selenium.Support.UI;
using OpenQA.Selenium.Interactions;

namespace ParentsForm
{
    class Miaform
    {
        static void Main(string[] args)
        {
            ChromeOptions options = new();
            options.AddArguments("--start-maximized");
            //open browser
            IWebDriver driver = new ChromeDriver(options);

            //#navigate to https://miacademy.co/#/
            driver.Navigate().GoToUrl("https://miacademy.co/#/");

            //navigate to MiaPrep Online High School through the link on banner
            IWebElement link = driver.FindElement(By.LinkText("Online High School"));
            link.Click();


            //apply to MOHS/click on Apply to our school button on the banner

            IWebElement apply_button_locator = driver.FindElement(By.XPath("/html//main[@id='main']/div[@class='content-wrap']/article/div[@class='entry-content-wrap']/div/div[2]/div//a[@href='https://forms.zohopublic.com/miaplazahelp/form/MOHSInitialApplication/formperma/okCyt4yyq39rZvSBXB9FSjDeek1ilbRVK1iNCK--3K8']"));
            apply_button_locator.Click();           
             

            Thread.Sleep(2000);

            //fill in the Parent Information 
            IWebElement first_name = driver.FindElement(By.XPath("//li[@id='Name-li']/div[@class='tempContDiv twoType']/div/span[1]/input[@name='Name']"));
            first_name.SendKeys("Max");

            
            IWebElement last_element = driver.FindElement(By.XPath("//li[@id='Name-li']/div[@class='tempContDiv twoType']/div/span[2]/input[@name='Name']"));
            last_element.SendKeys("Mustermann");

            
            IWebElement email_id = driver.FindElement(By.Id("Email-arialabel"));
            email_id.SendKeys("max.mustermann@email.com");

            Thread.Sleep(2000);

            IWebElement number = driver.FindElement(By.Id("PhoneNumber"));
            number.SendKeys("1766767432");


            //#select value from drop down for additional parent informaiton
            IWebElement drop_down = driver.FindElement(By.Id("Dropdown-arialabel"));
            var values = new SelectElement(drop_down);
            values.SelectByText("Yes");

            Thread.Sleep(2000);

            //enter second parent information
            IWebElement secparent_fname = driver.FindElement(By.XPath("//div[@id='formBodyDiv']/ul[1]/li[7]//div[@class='nameWrapper']/span[1]/input[@name='Name1']"));
            secparent_fname.SendKeys("Michelle");

            Thread.Sleep(1000);

            IWebElement secparent_lname = driver.FindElement(By.XPath("//div[@id='formBodyDiv']/ul[1]/li[7]//div[@class='nameWrapper']/span[2]/input[@name='Name1']"));
            secparent_lname.SendKeys("Mustermann");

            Thread.Sleep(1000);

            IWebElement secparent_emailID = driver.FindElement(By.Id("Email1-arialabel"));
            secparent_emailID.SendKeys("Michelle.Mustermann@email.com");

            Thread.Sleep(1000);

            IWebElement secparent_phonenum = driver.FindElement(By.Name("PhoneNumber1"));
            secparent_phonenum.SendKeys("1766767454");

            // scroll page down
            var name_element = driver.FindElement(By.XPath("//li[@id='Checkbox-li']//div[@role='group']/span[12]/label[@class='checkChoice cusChoiceLabel']/em[@class='cusChoiceEm']"));
            Actions actions = new(driver);
            actions.ScrollToElement(name_element);
            actions.Perform();

            //How did you hear about us? (Select all checkbox that apply)
            IWebElement checkbox1 = driver.FindElement(By.XPath("//li[@id='Checkbox-li']//div[@role='group']/span[1]/label[@class='checkChoice cusChoiceLabel']"));
            checkbox1.Click();

            Thread.Sleep(1000);

            IWebElement checkbox2 = driver.FindElement(By.XPath("//li[@id='Checkbox-li']//div[@role='group']/span[2]/label[@class='checkChoice cusChoiceLabel']"));
            checkbox2.Click();

            Thread.Sleep(1000);

            IWebElement checkbox3 = driver.FindElement(By.XPath("//li[@id='Checkbox-li']//div[@role='group']/span[3]/label[@class='checkChoice cusChoiceLabel']"));
            checkbox3.Click();

            Thread.Sleep(1000);

            // scroll to bottom of page
            actions.SendKeys(Keys.PageDown).Build().Perform();
            Thread.Sleep(1000);

            //What is your preferred start date?
            IWebElement calendar = driver.FindElement(By.Id("Date-date"));
            calendar.Click();
            Thread.Sleep(4000);
            IWebElement start_date = driver.FindElement(By.XPath("//div[@id='ui-datepicker-div']/table[@class='ui-datepicker-calendar']/tbody/tr[4]/td[1]/a[@href='#']"));
            actions.MoveToElement(start_date);
            Thread.Sleep(1000);
            start_date.Click();

            Thread.Sleep(3000);

            //click on next button to navigate to student information page
            IWebElement next_button = driver.FindElement(By.XPath("/html//li[@id='formAccess']//div[@class='inlineBlock nextAlign']/button[@type='button']"));
            actions.MoveToElement(next_button);
            next_button.Click();

            Thread.Sleep(3000);

            //close the browser
            driver.Quit();
        }

    }
}

