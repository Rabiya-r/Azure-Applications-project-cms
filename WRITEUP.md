# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

1. Virtual Machine:
    1.Full control over OS and environment
    2.Flexible networking and storage options.
    3.But can cost expensive, if vm's required more.
    4.Requires manual configuration of app deployment on each scaled instance.

2. App Service
    1.It's easier for web applications that requires fast deployement.
    2.No need to manage OS and some network configurations.
    3.High availability by default.
    4.Can scale up (increase resources of one instance) or out (add more instances) quickly.

Justification:
I chose App service because the FlaskApp I'm developing requires no management of the OS, costs will be lesser compared to Virtual Machine. AppService provides more efficient, scalable solution for a standard CMS.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

The decision may change to Virtual Machine from AppService can be:
1. If the CMS requires full control over OS,network.
2. If incase needed for advanced security operations an AppService would not be a suitable option.
3. If it requires High performance or specialized hardware needs.
