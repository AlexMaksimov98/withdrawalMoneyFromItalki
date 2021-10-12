# withdrawalMoneyFromItalki
This is the script, which helps teachers who work at Italki.com to withdraw money from Italki to Paypal and then to bank account.
Firstly, it logs in to Italki and checks the current balance. If current balance is more than 30 dollars and if this is more than a constant
MINIMUN_MONEY_TO_WITHDRAW. Then script asks to write a type of withdrawal and after receieving the response, it does all of job.
Right after, money is sent, it opens Mail.ru and parses the unread messages folder every 30 minutes for express withdrawal and every 2 hours for
regular withdrawal. When money is sent, it goes to Paypal and withdraws money to bank account.
