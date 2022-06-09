# Jenkins Introduction (Part 1) – 06/09/2022

## What is Jenkins?

-   Jenkins is the "leading open-source automation server."

-   built in Java.

-   It's basically a platform to follow best SDLC practices.

-   Commonly used to implement continuous integration and continuous
    delivery concepts.

## Some History:

-   Created from Hudson in 2004 by Oracle.

-   2011 Jenkins community Started.

## Jenkins Specialty, why do we use it?

-   useful to anyone who works on a software project, including:

    -   Application Developers

    -   Web Developers

    -   IT Operations

    -   Systems Engineers

    -   DevOps Engineers

-   Jenkins is known for being easy to use and highly adaptable. There
    are thousands of customizations and plugins that make Jenkins
    suitable for most use cases. It also works in the most common OS
    environments and is relatively lightweight.

## What is CI?

-   Continuous Integration is a software development practice where
    contributors are integrating their work very frequently. This
    results in multiple daily integrations to a mainline (Branch).
    Automated build and testing (post-commit promotion) is commonly
    used.

## Explain CI Workflow:

-   Checkout from an SCM (like git).

-   Branch and make local changes.

-   Add or change tests as necessary.

-   Trigger automated build locally.

-   If successful, consider committing.

-   Update with latest from mainline.

-   Push changes, build and test on integration machine.

## Explain the CI/ SDLC/ GIT Best Practices/ Benefits:

-   Maintain a single source repository.

-   Have a common mainline Branch (usually master).

-   Automate the Build.

-   Minimize potential for user error, automate everything possible.

-   Make the Build Self-testing.

-   Self-testing code.

-   Use Unit Tests for granular functionality.

-   Everyone commits frequently (at least daily, preferably).

-   Communication is key! Seems basic, but it's where many orgs fail.

-   Frequent merges will help avoid conflict errors.

-   The working branch should be updated as frequently as possible to
    help avoid very large diffs while merging.

-   Build every commit.

-   Prioritize fixing broken builds.

-   Keep your builds fast!

-   Testing environment should be as close to production as possible

-   Make it easy for anyone to get the latest.

-   Keep it open; everyone should see what's happening.

-   Automate the deployment if possible.

## What is Continuous Delivery?

-   A software development discipline where software is built so that it
    CAN be released to production at any time.

## Explain CD best Practices/ Benefits:

-   Software is always deployable throughout software development life
    cycle (SDLC).

-   Not breaking the build is prioritized over adding features.

-   Feedback is fast; production readiness is known.

-   Push-button deployments of any version of the software.

-   Close/collaborative working relationship.

-   Extensive automation.

## What are the Differences between CI and CD?

-   Continuous Delivery is the ability to release at any time.

-   Continuous Integration is just the practice of integrating code
    continuously. It doesn't necessarily mean that it can or will be
    released at any time.

## Explain the Stages of CI and CD: 

-   Build Deploy Test Release

## What are the differences between Continuous Delivery and Deployment?

-   Continuous Delivery means the code CAN be released at any time. When
    the term "Delivery" is used exclusively, the business generally
    isn't deploying as frequently.

-   Continuous Deployment means that code IS released continuously as
    part of an automated pipeline. Usually associated with many
    deployments to production every day.

## What tools would you advise to build a CI/CD System and why?

-   It depends for the projects I am assuming it a java project. I will
    advise GitHub, maven, SonarQube, nexus, Jenkins.

-   These are opensource, free of cost, widely used and very good and
    active community.

## Who are the Stakeholders?

-   Stakeholders are those with an interest in your project's outcome.
    They are typically the members of a project team: dev, QA, project
    managers, executives, project sponsors, customers, and users.

## What is Cloudbees Jenkins?

-   Cloudbees is a company providing Jenkins PaaS.

-   It’s the enterprise edition of Jenkins with support.
