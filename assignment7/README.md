Note about files: 

- Wait exercises: full experiment was not run - only small section of pseudocode from question 

- File: Assignment 7 - Wait Exercises Final.py 

- Clock exercises: 
       - 1,2,3. Only 2 simplified trials were conducted for ease of running code repeatedly - this was designed to test core.wait, clock + while loops, and countdown timer
      -  4. Contains full experiment using clock + while loops - question asked for a 'clock timer' since this was ambiguous as to which method, I used the method I preferred. 

- Files: Assignment 7 Clock Exercises Q1 Final.py, '' Q2.py, ''Q3.py, '' Q4.py 

- Frame-based timing exercises: I uploaded a cleaned up version of my code without clock-based timing comments for simplicity 

- Files: Assignment 7 frame based exercises - cleaned up.py 
       

Clock Exercises 

1. core.wait averaged 2.0017 s in 2 trials with 6 measurements - it is quite accurate but not exact
- Since experimental design requires extremely precise measures, core.wait is likely unacceptable 

2. clock + while loops averaged 2.0042 s through 2 trials with 6 measurements - similar results to core.wait were found 
 - depending on the precision required, it is possible this would be unnacceptable as well  

3. countdown timer + while loops averaged 2.0160 in 2 trials with 6 measurements - however, it should be noted that individual timer values were generally more consistent to each other (though this did show varience over multiple experiment runs) 
- the other methods resulted in an average value closer to 2s, their individual values showed a larger degree of varience, whereas the countdown timer showed greater consistency 


Frame-based Timing Exercises 

2. Depending on the run, 15-25 frames are typically dropped in the whole experiment (2 blocks, 3 trials each, 6 total trials). We can conclude that countdown timer was more effective for precise measurements. 
