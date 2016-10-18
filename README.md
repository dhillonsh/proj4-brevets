# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

## ACP controle times
t
That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.   

The algorithm for calculating controle times is described at
http://www.rusa.org/octime_alg.html . The description is ambiguous,
but the examples help.  Part of finishing this project is clarifying
anything that is not clear about the requirements, and documenting it
clearly.  

We are essentially replacing the calculator at
http://www.rusa.org/octime_acp.html .  We can also use that calculator
to clarify requirements.   

## AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes
an HTML form and emits a text page. The reimplementation will fill in
times as the input fields are filled.  Each time a distance is filled
in, the corresponding open and close times should be filled in.   If
no begin time has been provided, use 0:00 as the begin time.  

I will leave much of the design to you.   

## Testing

A suite of nose test cases is a requirement of this project.  Design
the test cases based on an interpretation of rules at
http://www.rusa.org/octime_alg.html .  Be sure to test your test
cases:  You can use the current brevet time calculator (
http://www.rusa.org/octime_acp.html ) to check that your expected test
outputs are correct. While checking these values once is a manual
operation, re-running your test cases should be automated in the usual
manner. 
