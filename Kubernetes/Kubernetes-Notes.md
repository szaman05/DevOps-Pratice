## Session 1: 

Kubernetes Introduction: 05/23/2022 1:30 PM:

Class Notes by instructor:

Containerization --\> Docker, Rocket (Rkt)

Container Orchestration Tools --\> Docker Swarm, Kubernetes, OpenShift

Installation

============

Self Managed K8's Cluster

minikube --\> Single Node K8's Cluster.

kubeadm --\> We can setup multi node k8's cluster using kubeadm.

Cloud Managed(Managed Services)

EKS --\> Elastic Kubernetes Service(AWS)

AKS --\> Azure Kubernetes Service(Azure)

GKE --\> Google Kubernetes Engine(GCP)

KOPS --\> Kubernetes Operations is a software using which we can create
production ready

highly available Kubernetes services in Cloud like AWS.KOPS will
leverage Cloud Services like

AWS Autoscaling & Launch Configurations to setup K8's Master & Workers.
It will Create 2 ASG & Launch Configs

one for master and one for workers. These Auto Scaling Groups will
manage EC2 Instances.

In this session K8s Architecture has been discussed. All the slides are
here: [Kubernaties.pdf](file:///D:\Mithun%20Videos\K8s\Kubernaties.pdf)

Q: Can you please explain K8s Architecture?

Q: Why do you prefer to use K8s? or, Explain core K8s features.

Q: What do you understand by a Cluster?

Q: What are the common ports for common K8s services?

Q: Which Flavor of K8s have you used?

## Session 2:

CNI: Container Network Interface. There are some plugins: Calico,
Weavenet, funnel etc.

Q: If we delete a namespace what will happen to the objects of that
namespace?

A: They will be deleted.

Q: Describe namespace:

A: it’s a logical isolation of groups in cluster. By default, there are
about 4 ns. Default, kube-public, kube-system, kube-node-lease.

Resources names must be unique within the ns.

\#kubectl get ns

\#kubectl get all -n kube-system

\#kubectl get all –all-namespaces

\#kubectl create ns kubekart

\#kubectl run nginx –image=nginx -n kubekart

Session 3:

Q: How does 2 containers communicate inside the Pod?

A: They share same network so they communicate localhost and port number
of that service.

So, its important they should not have any conflicting ports with each
other. Important thing to mention if we attach any storage to the pod,
they can also share the same storage.

Q: What is the range of Node port in K8s?

A: 30000 – 32767

Q: What is Static Pods?

A: Static pods are directly managed by node kubelet(nodes agent). Its
visible from api server but not manageable. You have to keep your
manifest file to /etc/Kubernetes/manifests
