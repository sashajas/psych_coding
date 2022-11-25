PsychoPy Keypress Exercises

1. Use a conditional to collect only the first response recorded from event.getKeys() 

  'if keys:
      firstResponse = keys[0]'
      
2. 
a) If you put event.clearEvents() within the trial loop it will run during each iteration (ie. 
getKeys will be cleared during each trial, allowing you to seperate out responses from each trial 
seperatel). 

However, if you put it outside the trial loop it will only run before the trials begin (either within each block 
or before each experiment). This means all of your responses will be recorded together since nothing is being 
cleared between trials. 

b) If you unindent the 'if keys:' line, it will only record the first response of the very last trial run. 
For you to access first responses for all trials, 'if keys:' needs to be within the trial loop. 

Psychtoolbox Keypress Exercises 
1. 
