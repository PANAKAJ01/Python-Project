import qrcode

#Taking UPI ID as input

Upi_id=input("Enter the UPI_ID= ")

##creating URL

Phonepe_url=f'upi://pay?pa={Upi_id}&pn=Recipient%20Name&mc=1234' #These all are the parameter for recieveing the payment
Paytm_url=f'upi://pay?pa={Upi_id}&pn=Recipient%20Name&mc=1234'
Google_pay_url=f'upi://pay?pa={Upi_id}&pn=Recipient%20Name&mc=1234'

Phonepe_qr=qrcode.make(Phonepe_url)
Paytm_qr=qrcode.make(Paytm_url)
Google_pay_qr=qrcode.make(Google_pay_url)

#save the qrcode to image file(optional)

Phonepe_qr.save('phonepe_qr.png')
Paytm_qr.save('paytm_qr.png')
Google_pay_qr.save("google_pay_qr.png")

#Display the qr code using pillow module

Phonepe_qr.show()
Paytm_qr.show()
Google_pay_qr.show()






