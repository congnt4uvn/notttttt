# DAY 1 — Introduction to Cloud Computing (AWS Learning Roadmap)

**Level:** Beginner  
**Focus:** Cloud Computing, AWS, business benefits, On-Premises vs Cloud, and CapEx vs OpEx

---

## 1. Learning objectives

By the end of this lesson, you should be able to:

- Explain what cloud computing is.
- Describe what Amazon Web Services (AWS) provides.
- Explain why companies move workloads to the cloud.
- Compare on-premises infrastructure with cloud infrastructure.
- Distinguish Capital Expenditure (CapEx) from Operational Expenditure (OpEx).
- Describe a simple cloud architecture for a Java Spring Boot application.

## 2. What is Cloud Computing?

Cloud computing is the on-demand delivery of computing resources—such as servers, storage, databases, networking, and software—over the internet, usually with pay-as-you-go pricing.

Instead of buying and maintaining all physical infrastructure yourself, you rent or consume resources from a cloud provider when you need them.

### Traditional approach

A company buys physical servers, installs them in a data centre, configures networking, maintains hardware, and plans capacity in advance.

```text
                 Company Office / Data Centre
                              |
                    +---------+---------+
                    |                   |
                 Network             Servers
                                        |
                           +------------+------------+
                           |            |            |
                         App          Database      Storage
```

### Cloud approach

The company provisions resources from a cloud provider through a web console, API, or infrastructure-as-code tool.

```text
                  Users / Customers
                         |
                      Internet
                         |
                         v
                  Cloud Provider
                         |
              +----------+----------+
              |          |          |
            Compute    Database   Storage
              |
        Application Server
              |
        Spring Boot API
```

### Key characteristics

| Characteristic | Explanation |
|---|---|
| On-demand self-service | Provision resources when needed |
| Broad network access | Access services over networks using standard clients |
| Resource pooling | Provider resources serve multiple customers with logical isolation |
| Rapid elasticity | Scale resources up or down as demand changes |
| Measured service | Usage can be monitored and billed |

**Example:** If an online shop experiences a large increase in traffic during a promotion, it can add computing capacity and reduce it again when demand falls.

## 3. What is AWS?

Amazon Web Services (AWS) is a cloud platform that provides a broad range of services for building, deploying, and operating applications.

AWS services include:

| Category | Example service | Purpose |
|---|---|---|
| Compute | Amazon EC2 | Virtual servers |
| Object storage | Amazon S3 | Store files and objects |
| Relational database | Amazon RDS | Managed relational databases |
| Networking | Amazon VPC | Isolated virtual networks |
| Identity and access | AWS IAM | Manage identities and permissions |
| Serverless compute | AWS Lambda | Run code without managing servers |
| Containers | Amazon ECS | Run containerized applications |
| Monitoring | Amazon CloudWatch | Metrics, logs, and alarms |
| Content delivery | Amazon CloudFront | Deliver content through a CDN |

AWS offers services that can be combined to create architectures ranging from small websites to large distributed systems.

## 4. Why do companies use AWS?

### 4.1 Reduce upfront infrastructure investment

A company does not necessarily need to purchase servers, storage arrays, and networking equipment before launching a service.

It can provision cloud resources and pay for usage according to the applicable pricing model.

### 4.2 Scale with demand

Cloud resources can be scaled to handle changes in workload.

```text
Low traffic                 High traffic
    |                           |
    v                           v
+---------+               +-------------+
| 1 App   |     Scale     | Multiple    |
| Server  | ------------> | App Servers |
+---------+               +-------------+
```

For example, an application may use a small number of EC2 instances during normal periods and an Auto Scaling Group to add instances during peak traffic.

### 4.3 Improve availability and resilience

AWS provides infrastructure across multiple Regions and Availability Zones.

An application can be designed to continue operating when an individual resource or Availability Zone becomes unavailable.

High availability is not automatic: the application architecture must use appropriate redundancy, health checks, failover, and data protection.

### 4.4 Deploy globally

Companies can deploy workloads in Regions closer to customers or use content delivery services to improve user experience.

### 4.5 Access managed services

AWS offers managed services such as RDS, S3, and DynamoDB. These reduce the amount of underlying infrastructure that a team must operate.

Managed services still require configuration, security, monitoring, and cost management.

### 4.6 Improve speed and experimentation

Development teams can create test environments quickly, try new ideas, and remove resources when they are no longer needed.

## 5. Benefits of Cloud Computing

| Benefit | Explanation | Example |
|---|---|---|
| Cost flexibility | Pay for resources according to the pricing model | Start with a small EC2 instance |
| Scalability | Increase or decrease capacity | Auto Scaling |
| Agility | Provision resources quickly | Create a test environment |
| Global reach | Deploy in multiple Regions | Serve customers in different countries |
| Availability options | Design across multiple Availability Zones | Multi-AZ application |
| Managed services | Reduce infrastructure administration | Amazon RDS |
| Automation | Provision infrastructure using code | AWS CloudFormation or Terraform |
| Security capabilities | Use identity, encryption, logging, and network controls | IAM and KMS |

Cloud adoption does not automatically guarantee lower costs or better security. Results depend on architecture, governance, workload characteristics, and operational practices.

## 6. On-Premises vs Cloud

**On-premises** means an organization operates infrastructure in its own facilities or data centre, or in a facility it directly manages.

**Cloud** means the organization consumes computing services from a cloud provider.

| Area | On-Premises | Cloud |
|---|---|---|
| Hardware | Organization purchases or leases it | Provider operates underlying hardware |
| Initial investment | Often high | Can start with low upfront investment |
| Capacity | Must be planned and installed | Can often be provisioned on demand |
| Maintenance | Organization manages physical infrastructure | Provider manages physical cloud infrastructure |
| Scaling | May require purchasing hardware | Can often scale through configuration |
| Deployment speed | Can be slower | Often faster |
| Control | More direct control over hardware | Control through provider services and configurations |
| Billing | Hardware, facilities, maintenance, staffing | Usage-based and other pricing models |
| Responsibility | Organization manages most layers | Shared between provider and customer |

### Example: Deploying a Spring Boot application

**On-premises architecture**

```text
             Internet
                |
          Company Firewall
                |
          Load Balancer
                |
        Physical Application Server
                |
          Spring Boot API
                |
        Physical Database Server
```

**AWS architecture**

```text
                Internet
                   |
             Application Load
                Balancer
                   |
             Amazon EC2
                   |
             Spring Boot API
                   |
               Amazon RDS
                   |
             Amazon S3
```

The AWS architecture is illustrative. A production design may include private subnets, security groups, multiple Availability Zones, backups, monitoring, and additional security controls.

## 7. CapEx vs OpEx

These are two important financial concepts when comparing traditional infrastructure with cloud services.

### 7.1 CapEx — Capital Expenditure

CapEx is money spent to acquire or improve long-term assets.

Examples:

- Buying physical servers.
- Purchasing network switches.
- Buying storage systems.
- Building or expanding a data centre.
- Purchasing hardware that will be used for several years.

Example:

A company buys 10 physical servers for $50,000. This is generally a capital investment, subject to the organization's accounting policies.

### 7.2 OpEx — Operational Expenditure

OpEx is spending on ongoing operations and services.

Examples:

- Cloud service usage charges.
- Electricity.
- Internet connectivity.
- Software subscriptions.
- Maintenance services.
- Managed service fees.

Example:

A company rents cloud compute capacity and pays monthly based on its usage and selected pricing model.

### 7.3 CapEx vs OpEx comparison

| Feature | CapEx | OpEx |
|---|---|---|
| Meaning | Capital expenditure | Operational expenditure |
| Spending pattern | Often larger upfront investment | Often recurring or usage-based |
| Typical example | Buy physical servers | Pay for cloud resources |
| Ownership | May acquire a long-term asset | Usually consumes a service |
| Capacity planning | Often requires advance planning | Can be more flexible |
| Accounting | Generally capitalized and depreciated according to policy | Generally expensed according to policy |

**Important:** Cloud does not mean every cost is OpEx in every accounting or contractual situation. The actual accounting treatment depends on the contract, asset, and applicable accounting standards.

### 7.4 Simple business example

A startup wants to launch an online shopping application.

**Option A — On-premises**

- Purchase servers.
- Purchase networking equipment.
- Prepare a server room.
- Pay for electricity and cooling.
- Maintain hardware.
- Plan capacity before traffic grows.

**Option B — AWS**

- Create an AWS account.
- Provision EC2 or a managed compute service.
- Use RDS for a relational database.
- Use S3 for images and documents.
- Pay for the resources consumed.

The cloud option can reduce upfront hardware investment and increase flexibility, but the company must still monitor cloud spending and design its architecture carefully.

## 8. Real-world case study: Online shopping application

Imagine a company is building an e-commerce platform with Java Spring Boot.

### Business requirements

- Customers browse products.
- Customers upload profile images.
- Customers place orders.
- The application stores product and order information.
- The application must support increasing traffic.

### Example AWS architecture

```text
                  Customers
                      |
                      v
                   Internet
                      |
                      v
                 Route 53
                      |
                      v
               Application Load
                  Balancer
                      |
              +-------+-------+
              |               |
              v               v
           EC2 AZ-A         EC2 AZ-B
              |               |
              +-------+-------+
                      |
               Spring Boot API
                      |
          +-----------+-----------+
          |                       |
          v                       v
       Amazon RDS              Amazon S3
       Orders and               Product images
       products                 and documents
```

Possible AWS services:

| Requirement | AWS service |
|---|---|
| Run Spring Boot application | Amazon EC2 |
| Distribute HTTP traffic | Application Load Balancer |
| Store relational data | Amazon RDS |
| Store product images | Amazon S3 |
| Manage permissions | AWS IAM |
| Monitor application infrastructure | Amazon CloudWatch |
| Manage DNS | Amazon Route 53 |

### Example application flow

1. A customer opens the shopping website.
2. The request reaches the Application Load Balancer.
3. The load balancer forwards the request to a healthy Spring Boot instance.
4. Spring Boot retrieves product information from RDS.
5. Product images are retrieved from S3.
6. The application returns the response to the customer.

## 9. Key cloud terminology

| Term | Meaning |
|---|---|
| Cloud Provider | Company providing cloud services |
| Region | Separate geographic AWS area |
| Availability Zone | Isolated location within an AWS Region |
| Scalability | Ability to increase or decrease capacity |
| Elasticity | Ability to adapt capacity to changing demand |
| High Availability | Design that minimizes service interruption |
| Fault Tolerance | Ability to continue operating despite certain failures |
| Pay-as-you-go | Pay according to usage or selected pricing |
| Infrastructure | Computing, storage, networking, and related resources |
| Workload | Application or set of tasks running on infrastructure |

We will study Regions and Availability Zones in more detail in a later lesson.

## 10. Practical exercises with answers

### Exercise 1 — Cloud Computing

**Question:** What is cloud computing?

A. Buying physical servers only.  
B. Delivering computing resources over a network on demand.  
C. A programming language.  
D. A database engine.

**Answer: B.** Cloud computing provides computing resources such as compute, storage, and databases on demand.

### Exercise 2 — AWS

**Question:** Which AWS service provides virtual servers?

A. Amazon S3  
B. Amazon EC2  
C. Amazon RDS  
D. AWS IAM

**Answer: B. Amazon EC2.** EC2 provides virtual compute instances.

### Exercise 3 — Storage

**Question:** Which service is commonly used to store product images and documents?

A. Amazon S3  
B. Amazon EC2  
C. AWS IAM  
D. Amazon VPC

**Answer: A. Amazon S3.** S3 is an object storage service.

### Exercise 4 — On-Premises vs Cloud

**Question:** What is one major difference between on-premises infrastructure and cloud infrastructure?

**Answer:** With on-premises infrastructure, the organization manages and operates its physical infrastructure. With cloud infrastructure, the cloud provider manages the underlying physical infrastructure while the customer configures and manages the services and workloads it consumes.

### Exercise 5 — CapEx vs OpEx

Classify the following:

| Item | Suggested classification |
|---|---|
| Buying physical servers | CapEx |
| Paying a monthly cloud usage bill | OpEx |
| Purchasing network equipment | CapEx |
| Paying for an ongoing software subscription | Usually OpEx |
| Paying for electricity | OpEx |

### Exercise 6 — Architecture

**Question:** Your Spring Boot application needs to store product images. Which AWS service would you choose?

**Answer:** Amazon S3, because it provides managed object storage for images and other files.

### Exercise 7 — Business scenario

**Scenario:** An online shopping application experiences high traffic during a promotional event. What cloud benefit can help?

**Answer:** Scalability and elasticity. The application can increase its compute capacity to handle higher traffic and reduce capacity when demand decreases.

## 11. Vietnamese vocabulary with pronunciation

Pronunciation is approximate and intended as a speaking aid.

| English | Pronunciation | Vietnamese |
|---|---|---|
| Cloud Computing | KLAUD kəm-PYOO-ting | Điện toán đám mây |
| Cloud Provider | KLAUD prə-VAI-dər | Nhà cung cấp dịch vụ đám mây |
| Infrastructure | IN-frə-struhk-chər | Cơ sở hạ tầng |
| Server | SER-vər | Máy chủ |
| Storage | STOR-ij | Lưu trữ |
| Database | DAY-tə-bейс | Cơ sở dữ liệu |
| Network | NET-wərk | Mạng |
| Scalability | skay-lə-BIL-ə-tee | Khả năng mở rộng |
| Elasticity | ee-las-TIS-ə-tee | Khả năng co giãn |
| Availability | ə-vay-lə-BIL-ə-tee | Tính sẵn sàng |
| Reliability | ri-lai-ə-BIL-ə-tee | Độ tin cậy |
| Security | si-KYOOR-ə-tee | Bảo mật |
| On-Premises | on-PREM-iss-iz | Tại chỗ |
| Capital Expenditure | KAP-ə-təl ik-SPEN-di-chər | Chi phí đầu tư |
| Operational Expenditure | op-ə-RAY-shən-əl ik-SPEN-di-chər | Chi phí vận hành |
| Pay-as-you-go | PAY-əz-yoo-GOH | Trả theo mức sử dụng |
| Workload | WERK-lohd | Khối lượng công việc |
| Data Centre | DAY-tə SEN-tər | Trung tâm dữ liệu |
| Deployment | di-PLOY-mənt | Triển khai |
| Maintenance | MAYN-tə-nəns | Bảo trì |

## 12. English speaking practice

### Topic: Explain Cloud Computing

Read aloud:

> Cloud computing is the delivery of computing resources over the internet.
>
> Instead of buying and maintaining physical servers, companies can use cloud services from providers such as Amazon Web Services.
>
> AWS provides many services, including EC2, S3, RDS, and IAM.
>
> EC2 provides virtual servers. S3 stores files and objects. RDS provides managed relational databases. IAM manages identities and permissions.
>
> Companies use cloud computing because it provides flexibility, scalability, and access to managed services.
>
> Cloud computing can also reduce the need for large upfront infrastructure investments.
>
> However, companies still need to manage security, performance, availability, and costs.
>
> I want to learn AWS so that I can build and deploy scalable applications using Java Spring Boot.

### Speaking questions and model answers

**Question 1: What is cloud computing?**

> Cloud computing is the delivery of computing resources over the internet. Companies can use servers, storage, and databases without managing all the physical hardware themselves.

**Question 2: What is AWS?**

> AWS is Amazon's cloud platform. It provides services such as EC2, S3, RDS, and IAM.

**Question 3: Why do companies use AWS?**

> Companies use AWS because it provides scalability, flexibility, global infrastructure, and managed services.

**Question 4: What is the difference between CapEx and OpEx?**

> CapEx is money spent on long-term assets, such as physical servers. OpEx is money spent on ongoing operations, such as cloud usage fees.

**Question 5: What is the difference between on-premises and cloud infrastructure?**

> On-premises infrastructure is operated by the organization in its own or managed facilities. Cloud infrastructure is provided as services by a cloud provider.

## 13. Interview questions

**Q1. What is cloud computing?**

Cloud computing is the on-demand delivery of computing resources over a network, with pricing based on the service and usage model.

**Q2. What is AWS?**

AWS is a cloud platform offering compute, storage, databases, networking, security, analytics, and many other services.

**Q3. What are the main benefits of cloud computing?**

Scalability, elasticity, agility, global reach, access to managed services, and flexible pricing.

**Q4. What is the difference between scalability and elasticity?**

Scalability is the ability to increase or decrease system capacity. Elasticity is the ability to adjust capacity in response to changing demand.

**Q5. What is the difference between CapEx and OpEx?**

CapEx is spending on long-term assets. OpEx is spending on ongoing operations and services.

**Q6. Does moving to the cloud always reduce costs?**

No. Cloud can reduce upfront investment and improve flexibility, but poor resource management, unsuitable architecture, and unnecessary usage can increase costs.

**Q7. What is on-premises infrastructure?**

Infrastructure operated in an organization's own or directly managed facilities.

**Q8. Name four AWS services and explain their purposes.**

- EC2: Virtual compute instances.
- S3: Object storage.
- RDS: Managed relational databases.
- IAM: Identity and access management.

**Q9. What is a cloud Region?**

A Region is a separate geographic area where AWS operates infrastructure and services.

**Q10. How would you deploy a Spring Boot application on AWS?**

One possible approach is to deploy the application to EC2, place an Application Load Balancer in front of it, use RDS for relational data, and use S3 for files. IAM Roles provide secure access to AWS services.

## 14. DAY 1 summary

| Concept | Key point |
|---|---|
| Cloud Computing | Computing resources delivered on demand |
| AWS | Amazon's cloud platform |
| EC2 | Virtual servers |
| S3 | Object storage |
| RDS | Managed relational database |
| IAM | Identity and access management |
| Scalability | Increase or decrease capacity |
| Elasticity | Adjust capacity as demand changes |
| On-Premises | Infrastructure operated in managed facilities |
| CapEx | Investment in long-term assets |
| OpEx | Ongoing operational spending |

## 15. Progress checklist

- [ ] Understand the definition of Cloud Computing.
- [ ] Understand the five key cloud characteristics.
- [ ] Understand what AWS is.
- [ ] Know the purpose of EC2.
- [ ] Know the purpose of S3.
- [ ] Know the purpose of RDS.
- [ ] Know the purpose of IAM.
- [ ] Understand why companies use AWS.
- [ ] Understand scalability and elasticity.
- [ ] Compare On-Premises and Cloud.
- [ ] Understand CapEx and OpEx.
- [ ] Explain a simple Spring Boot AWS architecture.
- [ ] Complete the practical exercises.
- [ ] Review the interview questions.
- [ ] Practice the English speaking topic.

## 16. What you should understand before moving to Day 2

Before continuing, make sure you can explain these ideas in your own words:

1. What is cloud computing?
2. What is AWS?
3. Why do companies use cloud services?
4. What is the difference between on-premises and cloud infrastructure?
5. What is the difference between CapEx and OpEx?
6. What are EC2, S3, RDS, and IAM used for?

---

## Next lesson — DAY 2: Cloud Deployment Models

In Day 2, we will study:

- Public Cloud.
- Private Cloud.
- Hybrid Cloud.
- Multi-Cloud.
- Advantages and disadvantages of each model.
- Real-world architecture examples.
- Practical exercises and answers.
- Vietnamese vocabulary and English speaking practice.
