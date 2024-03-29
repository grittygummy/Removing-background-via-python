from removebg import RemoveBg
api_key='qWH6fjkAZxLfoDMejtYuM5w1'
removebg=RemoveBg(api_key,'error.log')
input_image='jess1.png'
removebg.remove_background_from_img_file(input_image,size='regular')