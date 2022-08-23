# email-automation
Python code to automate the tedious task of sending emails to people.
Made with smtplib for sending email automation and ssl for encryption and authentication 

How it works:
First, go to your Google account, nd on the left panel select the option “Security.”
![image](https://user-images.githubusercontent.com/94329833/186037207-39994e3a-bc76-4093-9e6c-1881f662d316.png)

From there select the 2-step verification option:
![image](https://user-images.githubusercontent.com/94329833/186037281-0c1a1898-684a-4d3b-a832-8b8c0766c1e4.png)

After this, we’ll see a new page. We have to click on “Get Started”

Google will ask to log in again. Then we have to input our phone number, and click on “Next.” We’ll get a code to verify our phone number. After we introduce the code, You should see the following page:
![image](https://user-images.githubusercontent.com/94329833/186037631-92f34e9b-f222-426c-bb3d-4bae4f8ccad0.png)

If everything was set up correctly, you'llsee a new page with the message "2-Step Verification is On"

Once you are logged in again, you should see the App Passwords under the same page and it looks like this:
![image](https://user-images.githubusercontent.com/94329833/186048820-d11fa9b7-3e9b-4d8d-88ff-3dda4cc5ffe9.png)
In the “Select app” dropdown, select “Other (Custom name)” and type any name you want. I’ll name mine “encrypt" and then click on "generate"

After this, you should see a new page with the 16-charachter password inside a yellow box as show below:
![image](https://user-images.githubusercontent.com/94329833/186048997-40255020-7916-407e-b91f-ea84a445262e.png)

It’s all set!  this 16 character password will be used to log into your email via the python code.


