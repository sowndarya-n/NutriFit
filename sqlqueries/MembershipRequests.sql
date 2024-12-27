select * from main_membershiprequest;

UPDATE main_membershiprequest
SET approved_status = 1
WHERE id = 3;


UPDATE main_user
SET membership_id = (
    SELECT id FROM main_membershiprequest
    WHERE main_membershiprequest.email = main_user.email
    AND approved_status = 1
)
WHERE EXISTS (
    SELECT 1 FROM main_membershiprequest
    WHERE main_membershiprequest.email = main_user.email
    AND approved_status = 1
);


INSERT INTO main_usersubscription (id, plan, subscription_type, start_date, expiry_date, email, user_id)
SELECT 
    u.membership_id AS id,
    mr.plan,
    mr.subscription_type,
    CURRENT_DATE AS start_date,
    DATE_ADD(CURRENT_DATE, INTERVAL 1 MONTH) AS expiry_date,
    u.email,
    u.email AS user_id  -- Use `email` to satisfy the foreign key constraint
FROM 
    main_user u
JOIN 
    main_membershiprequest mr 
ON 
    u.membership_id = mr.id
WHERE 
    mr.approved_status = 1;
