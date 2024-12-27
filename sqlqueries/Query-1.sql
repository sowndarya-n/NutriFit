-- CREATE DATABASE NutriFit;
-- CREATE USER 'NutriFit'@'localhost' IDENTIFIED BY 'NutriFit@1234';
-- GRANT ALL PRIVILEGES ON NutriFit.* TO 'NutriFit'@'localhost';
-- FLUSH PRIVILEGES;
INSERT INTO main_fitnessblogpost (id, title, content, excerpt, image, date)
VALUES 
(1, 'Understanding the Mind-Body Connection', 
    'The mind-body connection is a powerful concept that shows how our physical health impacts our mental well-being, and vice versa. Studies have shown that regular physical activity can lead to improved mood, reduced anxiety, and even better cognitive function. This connection works both ways; when we take steps to improve our mental health through practices like mindfulness or meditation, we often see positive changes in our physical health as well. In this post, we will explore the science behind the mind-body connection and provide practical tips for nurturing both aspects of wellness.', 
    'Explore how physical and mental health are deeply intertwined, and learn ways to nurture both.', 
    'img/mind_body.png', '2024-01-31 11:11:11');

INSERT INTO main_fitnessblogpost (id, title, content, excerpt, image, date)
VALUES 
(2, 'Breathing Techniques for Stress Relief', 
    'In our busy lives, stress can accumulate quickly and have a detrimental impact on our overall health. One of the simplest and most effective ways to manage stress is through controlled breathing techniques. Exercises like diaphragmatic breathing, box breathing, and the 4-7-8 technique help activate the body’s relaxation response, reduce heart rate, and lower blood pressure. In this post, we will break down these breathing techniques step-by-step, explaining when and how to use each method to manage stress effectively.', 
    'Discover simple but effective breathing exercises that can help reduce stress and promote relaxation.', 
    'img/deep_breathe.png', '2024-02-10 14:45:00');

INSERT INTO main_fitnessblogpost (id, title, content, excerpt, image, date)
VALUES 
(3, 'Mental Health Benefits of Regular Exercise', 
    'Physical exercise is one of the most effective, natural ways to improve mental health. Regular activity has been shown to reduce symptoms of anxiety and depression, increase self-esteem, and improve cognitive function. Exercise stimulates the release of endorphins, dopamine, and serotonin—brain chemicals that play a crucial role in mood regulation. Whether it\'s aerobic exercises like running and cycling or strength training, each type of exercise has unique benefits for mental wellness. This post will explore the various mental health benefits of regular exercise and offer tips on how to start an exercise routine.', 
    'Learn how physical activity can alleviate symptoms of anxiety, depression, and other mental health challenges.', 
    'img/mental_exe.png', '2024-03-05 09:20:00');

INSERT INTO main_fitnessblogpost (id, title, content, excerpt, image, date)
VALUES 
(4, 'Incorporating Mindfulness into Your Daily Routine', 
    'Mindfulness involves paying attention to the present moment without judgment. While meditation is a popular way to practice mindfulness, you can also bring mindfulness into daily activities like eating, walking, and even brushing your teeth. Practicing mindfulness helps reduce stress, improve focus, and increase emotional resilience. This post will provide simple ways to incorporate mindfulness into your day-to-day life, showing you how to use mindfulness techniques to remain grounded and reduce stress, no matter how busy your schedule is.', 
    'Mindfulness is more than meditation; here’s how to bring mindfulness into everyday activities for better mental wellness.', 
    'img/mindfulness.png', '2024-04-18 17:55:00');

UPDATE main_fitnessblogpost
SET image = 'img/mind-body.jpg'
WHERE id = 1;

INSERT INTO main_fitnessblogpost (id, title, content, excerpt, image, date)
VALUES 
(5, 'Stress Management Techniques for Busy Schedules', 
    'Stress is an inevitable part of life, but with the right strategies, we can manage it effectively. For those with busy schedules, finding time to unwind can be challenging. Fortunately, there are many quick techniques that can help. This post covers progressive muscle relaxation, mini-meditations, and the power of physical movement to alleviate stress. Each method is designed to fit seamlessly into your day, whether you’re at work, home, or on the go. Learn how to use these techniques to keep stress in check, boost resilience, and maintain mental clarity.', 
    'Discover quick and effective ways to manage stress, even on the busiest days.', 
    'img/mental_stress.png', '2024-10-26 11:11:11');
    
    


-- Insert Workout Categories
INSERT INTO main_workoutcategories (id, title, overview)
VALUES 
(1, 'Strength-Building Workouts', 'Strength training not only builds muscle but also supports bone health and metabolism. This section provides routines focused on building overall strength.'),
(2, 'Weight Loss Workouts', 'For effective weight loss, a combination of cardio and strength training can help burn calories and build lean muscle. This section includes fat-burning workouts to aid in weight loss.'),
(3, 'Flexibility & Mobility Workouts', 'Flexibility and mobility are crucial for joint health, reducing injury risk, and improving movement quality. This section offers stretching and mobility exercises to enhance flexibility.'),
(4, 'General Fitness Workouts', 'A balanced approach to fitness combining strength, cardio, and flexibility for overall health and wellness.');

-- Insert Exercises with Routines

-- Exercises for Strength-Building Workouts (category_id = 1)
INSERT INTO main_fitnessexercise (id, category_id, name, description, routine, image)
VALUES 
(1, 1, 'Compound Lifts', 'Discover the benefits of compound exercises like squats, deadlifts, and overhead presses, which engage multiple muscle groups.', 'Perform 3 sets of 8-10 reps each with 1-minute rest between sets.', 'img/compound_lift.jpg'),
(2, 1, 'Isolation Exercises', 'Target specific muscles with exercises like bicep curls, tricep extensions, and leg extensions.', '3 sets of 12-15 reps for each exercise with 30 seconds rest.', 'img/isolation.png'),
(3, 1, 'Strength Circuit', 'A full-body circuit designed for strength with exercises like pull-ups, push-ups, and lunges.', '4 sets of 6-8 reps with 90 seconds rest between each exercise.', 'img/circuit_training.jpg');

-- Exercises for Weight Loss Workouts (category_id = 2)
INSERT INTO main_fitnessexercise (id, category_id, name, description, routine, image)
VALUES 
(4, 2, 'High-Intensity Interval Training (HIIT)', 'HIIT involves short bursts of intense exercise followed by brief rest periods, helping you burn more calories in less time.', '20 seconds of maximum effort followed by 10 seconds of rest, for 8 rounds.', 'img/hiit.png'),
(5, 2, 'Tabata Training', 'A popular form of HIIT that includes short, intense exercise intervals followed by rest.', '4 minutes of 20-second sprints followed by 10 seconds of rest for each exercise.', 'img/tabata.png'),
(6, 2, 'Fat-Burning Circuit', 'Combines cardio and bodyweight strength exercises like mountain climbers, burpees, and jump squats.', 'Perform 3 rounds of 10 reps for each exercise with minimal rest.', 'img/fat_burn.png');

-- Exercises for Flexibility & Mobility Workouts (category_id = 3)
INSERT INTO main_fitnessexercise (id, category_id, name, description, routine, image)
VALUES 
(7, 3, 'Static Stretching', 'Static stretches help lengthen muscles and are ideal post-workout for recovery.', 'Hold each stretch for 30 seconds, repeat 3 times per side.', 'img/static_stretch.png'),
(8, 3, 'Dynamic Warm-Up', 'Increase mobility with movements like leg swings, arm circles, and walking lunges.', '10-15 minutes of dynamic exercises to prepare muscles for more intense activity.', 'img/dynamic_warmup.jpg'),
(9, 3, 'Yoga Flow', 'Perform a sequence of poses to enhance flexibility and reduce stress.', 'Complete a 20-minute yoga flow, holding each pose for 30-60 seconds.', 'img/yoga_flow.jpg');

-- Exercises for General Fitness Workouts (category_id = 4)
INSERT INTO main_fitnessexercise (id, category_id, name, description, routine, image)
VALUES 
(10, 4, 'Full-Body Circuit', 'Get a mix of strength and cardio with a full-body circuit, alternating between exercises like squats, push-ups, and jumping jacks.', '3 sets of 15 reps each exercise with minimal rest.', 'img/full_body.png'),
(11, 4, 'Endurance Run', 'Improve cardiovascular health with a steady-state endurance run.', 'Run at a moderate pace for 30-45 minutes.', 'img/endurance_running.jpg'),
(12, 4, 'Functional Mobility', 'Improve overall mobility and stability with exercises like hip openers, thoracic rotations, and ankle stretches.', 'Perform each exercise for 30-45 seconds, focusing on controlled movements and breathing.', 'img/functional_mobility.jpg');

-- Insert Fitness Equipment Data
INSERT INTO main_fitnessequipment (name, description, image, amazon_link) VALUES
('Dumbbells', 
 'Versatile weights used for various exercises, from strength training to functional movements. Dumbbells help improve muscle tone and strength.', 
 'img/dumbbell.png', 
 'https://www.amazon.com/s?k=dumbbells'),

('Barbell', 
 'Ideal for heavy lifting, barbells allow compound movements like squats, deadlifts, and bench presses to develop overall body strength.', 
 'img/barbell.jpg', 
 'https://www.amazon.com/s?k=barbell'),

('Kettlebell', 
 'Great for functional strength and cardio, kettlebells are used for dynamic movements like swings, presses, and squats.', 
 'img/kettlebell.jpg', 
 'https://www.amazon.com/s?k=kettlebell'),

('Resistance Bands', 
 'Portable and versatile, resistance bands are excellent for strength training, stretching, and rehabilitation exercises.', 
 'img/resistance_bands.jpg', 
 'https://www.amazon.com/s?k=resistance+bands'),

('Jump Rope', 
 'An effective cardio tool that boosts endurance, coordination, and agility, jump ropes are compact and easy to use anywhere.', 
 'img/speed_rope.jpg', 
 'https://www.amazon.com/s?k=jump+rope'),

('Medicine Ball', 
 'Used in strength, cardio, and rehabilitation exercises, medicine balls enhance explosive power and coordination.', 
 'img/medball.png', 
 'https://www.amazon.com/s?k=medicine+ball'),

('Foam Roller', 
 'Perfect for recovery, foam rollers help relieve muscle tension and improve flexibility through self-massage techniques.', 
 'img/foam_roller.png', 
 'https://www.amazon.com/s?k=foam+roller'),

('Pull-Up Bar', 
 'Ideal for bodyweight exercises, pull-up bars develop upper body strength through exercises like pull-ups and chin-ups.', 
 'img/pullupbars.jpg', 
 'https://www.amazon.com/s?k=pull+up+bar'),

('Workout Bench', 
 'A versatile base for strength exercises, workout benches are used for presses, flys, and step-ups, making it essential for weightlifting.', 
 'img/workout_bench.jpg', 
 'https://www.amazon.com/s?k=workout+bench'),

('Treadmill', 
 'Great for indoor cardio, treadmills provide a controlled running environment, useful for beginners and advanced runners alike.', 
 'img/treadmill.png', 
 'https://www.amazon.com/s?k=treadmill');
 
 INSERT INTO main_recipe (title, description, image, link)
VALUES 
('Avocado Toast with Eggs', 'A nutritious and easy-to-make breakfast option with healthy fats and protein.', 'nutrition_images/recipes/avocado_toast.jpg', 'https://www.example.com/avocado-toast-recipe'),
('Quinoa Salad with Chickpeas', 'A protein-packed salad with quinoa, chickpeas, fresh veggies, and a tangy dressing.', 'nutrition_images/recipes/quinoa_salad.jpg', 'https://www.example.com/quinoa-salad-recipe');

INSERT INTO main_guide (title, description, image, link)
VALUES 
('Meal Planning Basics', 'Learn the fundamentals of meal planning to support a balanced diet.', 'nutrition_images/guides/meal_planning.jpg', 'https://www.example.com/meal-planning-guide'),
('Hydration Essentials', 'Discover the importance of staying hydrated for optimal health and performance.', 'nutrition_images/guides/hydration.jpg', 'https://www.example.com/hydration-essentials');

INSERT INTO main_article (title, description, image, link)
VALUES 
('Understanding Macronutrients', 'A guide to proteins, fats, and carbohydrates and their role in your diet.', 'nutrition_images/articles/macronutrients.jpg', 'https://www.example.com/understanding-macronutrients'),
('The Benefits of Fiber', 'Explore how fiber contributes to digestive health and satiety.', 'nutrition_images/articles/fiber_benefits.jpg', 'https://www.example.com/benefits-of-fiber');

UPDATE main_article 
SET detailed_info = 'Proteins:\n - Essential for muscle repair and growth.\n - Serve as building blocks for enzymes and hormones.\nFats:\n - Provide long-term energy storage.\n - Essential for absorbing fat-soluble vitamins (A, D, E, K).\nCarbohydrates:\n - Primary source of energy for the body.\n - Includes simple sugars and complex carbs, which affect blood sugar differently.',  
    link = 'https://youtu.be/RdiFBx6dQpQ?feature=shared'
WHERE id = 1;

UPDATE main_article 
SET detailed_info = 'Types of Fiber:\n - Soluble fiber helps lower cholesterol and stabilize blood sugar levels.\n - Insoluble fiber aids digestion by adding bulk to stool.\nHealth Benefits:\n - Supports gut health and beneficial gut bacteria.\n - Promotes satiety, aiding in weight management.', 
    link = 'https://youtu.be/zsnEhLqQVbU?feature=shared'
WHERE id = 2;

select * from main_article;

INSERT INTO main_guide (id, title, description, content, image, yt_link)
VALUES 
(1, 'Meal Planning Basics', 
 'Learn the fundamentals of meal planning to support a balanced diet.', 
 'What is Meal Planning? Meal planning involves creating a weekly or monthly schedule of meals to help achieve nutritional goals and save time.\n\nBenefits of Meal Planning:\n- Healthier Eating: Ensures balanced meals with all essential nutrients.\n- Time-Saving: Reduces the time spent deciding on and preparing meals daily.\n- Budget-Friendly: Helps with budgeting by reducing food waste and frequent dining out.\n\nSteps for Effective Meal Planning:\n- Identify Your Goals: Decide if you want to focus on weight loss, muscle gain, or general health.\n- Create a Weekly Menu: Plan meals based on your nutritional needs and available ingredients.\n- Prep in Advance: Batch cook meals or prep ingredients to make cooking easier throughout the week.', 
 'nutrition_images/guides/meal_planning.jpg', 
 'https://www.youtube.com/watch?v=example6');
 
INSERT INTO main_guide (id, title, description, content, image, yt_link)
VALUES 
(2, 'Hydration Essentials', 
 'Discover the importance of staying hydrated for optimal health and performance.', 
 'Why Hydration is Important: Proper hydration is essential for maintaining body temperature, joint lubrication, and nutrient transport.\n\nDaily Water Intake Recommendations: Adults should drink about 8-10 glasses of water daily, but this can vary based on activity level, climate, and body size.\n\nTips to Stay Hydrated:\n- Start Your Day with Water: Drink a glass of water first thing in the morning.\n- Set Regular Reminders: Use apps or alarms to remind you to drink water throughout the day.\n- Flavor Your Water: Add slices of fruit or herbs like mint to make drinking water more enjoyable.\n\nSigns of Dehydration: Recognize signs like dark urine, dry mouth, fatigue, and headaches as indicators to increase water intake.', 
 'img/hydration.jpg', 
 'https://www.youtube.com/watch?v=_JGcNlHF7I4');
drop table main_essentials;
drop table main_membershiprequest;
drop table main_userprofile;
drop table main_membershipapproval;
drop table main_usersubscription;



use NutriFit;
Show tables;




delete from main_user where email='vn34182@uga.edu'; 
select * from auth_user;
select * from main_user;
select * from main_fitnessblogpost;
select * from main_workoutcategories;
select * from main_fitnessexercise;
select * from main_fitnessequipment;
select * from main_membershiprequest;
select * from main_usersubscription;

select * from main_recipe;
select * from main_essentials;
select * from main_guide;



select * from main_recipe;







select * from main_cancellationrequest;



UPDATE main_user u
JOIN main_userprofile p ON u.email = p.user_id
SET u.phone_number = p.phone,
    u.address = p.address
WHERE u.email = p.user_id;

select * from main_userprofile;

select * from main_essentials;
select * from main_user;
select * from main_membershiprequest;
select * from main_usersubscription;
select * from main_cancellationrequest;

-- drop table main_usersubscription;

delete from main_membershiprequest where email = 'saisumanth151515@gmail.com' and id=2;

ALTER TABLE main_article
DROP COLUMN detailed_info;

ALTER TABLE main_usersubscription
CHANGE COLUMN id membership_id  INT ;


select * from main_membershiprequest where approved_status=0;





UPDATE main_membershiprequest
SET approved_status = 1
WHERE id = 2;

select * from main_membershiprequest;
select * from main_user;
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
select * from main_membershiprequest;
select * from main_user;
select * from main_usersubscription;

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




ALTER TABLE main_article
ADD column detailed_info TEXT;


ALTER TABLE main_usersubscription
DROP FOREIGN KEY main_usersubscription_user_id_97272827_fk_main_user_email;



ALTER TABLE main_membershiprequest
CHANGE COLUMN id request_id INT;

ALTER TABLE main_membershiprequest
CHANGE COLUMN request_id request_id INT AUTO_INCREMENT;


ALTER TABLE main_membershiprequest
ADD CONSTRAINT fk_user_membership FOREIGN KEY (user_id) REFERENCES main_user(user_id);



ALTER TABLE main_membershiprequest
ADD COLUMN user_id INT;

UPDATE main_user
SET user_id= 2
WHERE email= 'sowndaryanookala3104@gmail.com';

UPDATE main_guide
SET content = 'Proper hydration is essential for maintaining body temperature, joint lubrication, and nutrient transport.\n\nDaily Water Intake Recommendations: Adults should drink about 8-10 glasses of water daily, but this can vary based on activity level, climate, and body size.\n\nTips to Stay Hydrated:\n- Start Your Day with Water: Drink a glass of water first thing in the morning.\n- Set Regular Reminders: Use apps or alarms to remind you to drink water throughout the day.\n- Flavor Your Water: Add slices of fruit or herbs like mint to make drinking water more enjoyable.\n\nSigns of Dehydration: Recognize signs like dark urine, dry mouth, fatigue, and headaches as indicators to increase water intake.'
WHERE id= 2;

UPDATE main_recipe
SET ingredients = '1 cup cooked quinoa, 1/2 cup canned chickpeas (rinsed and drained), 1/2 cup diced cucumber, 1/2 cup diced tomatoes, 1/4 cup chopped parsley, 1 tbsp olive oil, Juice of 1 lemon, Salt and pepper to taste' 
WHERE id= 2;

UPDATE main_user
SET membership_id = null
WHERE email= 'saisumanth151515@gmail.com';

delete from main_membershiprequest where id= 1;

select * from main_userprofile;
delete from main_userprofile where id=1;


ALTER TABLE main_userprofile 
DROP FOREIGN KEY main_userprofile_user_id_15c416f4_fk_main_user_email;
