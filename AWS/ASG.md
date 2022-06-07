# Auto Scaling Group:

Q: How can you launch 3 ec2 instances in 3 separate AZs at once?

A: Create a Launch Template with Spread/ Partition placement group
Create ASG select subnets in different AZs, enter 3 as desired capacity
and 3 as max capacity and Create it without any target tracking scaling
policy. It will launch 3 instances with 3 AZs. Point to note we just
need to delete the ASG to terminate the instances.

<img src="./images/ASG/media/image1.png"
style="width:6.5in;height:7.42986in" />

Q: How can we launch a number of instances based on a time range?

A: After creating an auto scaling group we can create scheduled scaling
policy; this option is not available during the time of creation. It’s
kind of overwrite the actual policy based on time condition. Also, for
every task we have to create single policy. Such as to launch in
specific time 1 policy to stop in specific time another policy.

<img src="./images/ASG/media/image2.png"
style="width:6.5in;height:2.99375in" />

Most of the Advanced Configurations in ASG we have to do after the
creation of ASG. Such as: Termination policy, Suspension process etc.

<img src="./images/ASG/media/image3.png"
style="width:6.5in;height:6.17569in" />

**Lifecycle Hooks:**

Lifecycle hooks help you perform custom actions on instances as they
launch and before they terminate.

<img src="./images/ASG/media/image4.png"
style="width:6.5in;height:2.08403in" />

**Active instance refresh:**

Instance refresh performs rolling updates on the Auto Scaling group's
instances. Only one instance refresh can be active at a time.

**Scaling Cooldowns:**

-   After a scaling activity happens, you are in the cooldown period
    (default 300 seconds).

-   During the cooldown period, the ASG will not launch or terminate
    additional instances (to allow for metrics to stabilize).

-   Use a ready-to-use AMI to reduce configuration time in order to be
    serving request fasters and reduce the cooldown period.
