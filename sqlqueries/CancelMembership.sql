select * from main_cancellationrequest;

UPDATE main_cancellationrequest
SET cancelled_status = 1
WHERE user_id =  'saisumanth151515@gmail.com'
AND cancelled_status = 0;

UPDATE main_membershiprequest
SET approved_status = 0
WHERE email = 'saisumanth151515@gmail.com' and id= 2;

select * from main_usersubscription;

DELETE FROM main_usersubscription
WHERE user_id = 'saisumanth151515@gmail.com';


UPDATE main_user
SET membership_id = NULL
WHERE email = 'saisumanth151515@gmail.com';