using OpenQA.Selenium; 
using OpenQA.Selenium.Chrome; 

namespace parent_form
{
    class miaform
    {
        static void Main(string[] args)
        {
            //open browser
            IWebDriver driver = new ChromeDriver();

            //#navigate to https://miacademy.co/#/
            driver.Navigate().GoToUrl("https://miacademy.co/#/");  




        }




    }



}

