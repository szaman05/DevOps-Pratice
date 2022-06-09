# Jenkins Introduction (Part 1) – 06/09/2022

## What is Jenkins?

1.  Jenkins is the "leading open-source automation server."

2.  built in Java.

3.  It's basically a platform to follow best SDLC practices.

4.  Commonly used to implement continuous integration and continuous
    delivery concepts.

## Some History:

5.  Created from Hudson in 2004 by Oracle.

6.  2011 Jenkins community Started.

## Jenkins Specialty, why do we use it?

7.  useful to anyone who works on a software project, including:

    1.  Application Developers

    2.  Web Developers

    3.  IT Operations

    4.  Systems Engineers

    5.  DevOps Engineers

8.  Jenkins is known for being easy to use and highly adaptable. There
    are thousands of customizations and plugins that make Jenkins
    suitable for most use cases. It also works in the most common OS
    environments and is relatively lightweight.

## What is CI?

9.  Continuous Integration is a software development practice where
    contributors are integrating their work very frequently. This
    results in multiple daily integrations to a mainline (Branch).
    Automated build and testing (post-commit promotion) is commonly
    used.

## Explain CI Workflow:

10. Checkout from an SCM (like git).

11. Branch and make local changes.

12. Add or change tests as necessary.

13. Trigger automated build locally.

14. If successful, consider committing.

15. Update with latest from mainline.

16. Push changes, build and test on integration machine.

## Explain the CI/ SDLC/ GIT Best Practices/ Benefits:

17. Maintain a single source repository.

18. Have a common mainline Branch (usually master).

19. Automate the Build.

20. Minimize potential for user error, automate everything possible.

21. Make the Build Self-testing.

22. Self-testing code.

23. Use Unit Tests for granular functionality.

24. Everyone commits frequently (at least daily, preferably).

25. Communication is key! Seems basic, but it's where many orgs fail.

26. Frequent merges will help avoid conflict errors.

27. The working branch should be updated as frequently as possible to
    help avoid very large diffs while merging.

28. Build every commit.

29. Prioritize fixing broken builds.

30. Keep your builds fast!

31. Testing environment should be as close to production as possible

32. Make it easy for anyone to get the latest.

33. Keep it open; everyone should see what's happening.

34. Automate the deployment if possible.

## What is Continuous Delivery?

35. A software development discipline where software is built so that it
    CAN be released to production at any time.

## Explain CD best Practices/ Benefits:

36. Software is always deployable throughout software development life
    cycle (SDLC).

37. Not breaking the build is prioritized over adding features.

38. Feedback is fast; production readiness is known.

39. Push-button deployments of any version of the software.

40. Close/collaborative working relationship.

41. Extensive automation.

## What are the Differences between CI and CD?

42. Continuous Delivery is the ability to release at any time.

43. Continuous Integration is just the practice of integrating code
    continuously. It doesn't necessarily mean that it can or will be
    released at any time.

## Explain the Stages of CI and CD: 

44. Build Deploy Test Release

## What are the differences between Continuous Delivery and Deployment?

45. Continuous Delivery means the code CAN be released at any time. When
    the term "Delivery" is used exclusively, the business generally
    isn't deploying as frequently.

46. Continuous Deployment means that code IS released continuously as
    part of an automated pipeline. Usually associated with many
    deployments to production every day.

## What tools would you advise to build a CI/CD System and why?

47. It depends for the projects I am assuming it a java project. I will
    advise GitHub, maven, SonarQube, nexus, Jenkins.

48. These are opensource, free of cost, widely used and very good and
    active community.

## Who are the Stakeholders?

49. Stakeholders are those with an interest in your project's outcome.
    They are typically the members of a project team: dev, QA, project
    managers, executives, project sponsors, customers, and users.

## What is Cloudbees Jenkins?

50. Cloudbees is a company providing Jenkins PaaS.

51. It’s the enterprise edition of Jenkins with support.
