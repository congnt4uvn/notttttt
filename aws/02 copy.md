# DAY 2 — Cloud Deployment Models

**Level:** Beginner  
**Focus:** Public Cloud, Private Cloud, Hybrid Cloud, Multi-Cloud, deployment choices, and real-world architecture

---

## 1. Learning objectives

By the end of this lesson, you should be able to:

- Explain what a cloud deployment model is.
- Describe Public Cloud, Private Cloud, Hybrid Cloud, and Multi-Cloud.
- Compare the advantages and disadvantages of each model.
- Choose a suitable deployment model for a business scenario.
- Understand how AWS can be used in different deployment models.
- Explain a basic hybrid architecture involving an on-premises system and AWS.
- Practice explaining deployment models in English.

## 2. What is a Cloud Deployment Model?

A cloud deployment model describes how cloud infrastructure is organized, who owns or operates it, and how users access it.

The main deployment models are:

1. Public Cloud.
2. Private Cloud.
3. Hybrid Cloud.
4. Multi-Cloud.

These models describe the environment in which services are deployed. They are different from cloud service models such as IaaS, PaaS, and SaaS, which describe the type of service being consumed.

## 3. Public Cloud

### 3.1 What is Public Cloud?

A Public Cloud is a cloud environment in which a cloud provider makes computing services available to customers over a network, typically the internet.

The provider owns and operates the underlying physical infrastructure. Customers provision and manage their cloud resources using logically isolated accounts, networks, and permissions.

Examples of public cloud providers include:

- Amazon Web Services (AWS).
- Microsoft Azure.
- Google Cloud Platform (GCP).

### 3.2 Public Cloud architecture

```text
                    Internet
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Customer A   Customer B   Customer C
          |            |            |
          v            v            v
      AWS Account  AWS Account  AWS Account
          |            |            |
          +------------+------------+
                       |
                       v
             Provider Infrastructure
           Physical Servers / Storage /
                    Networking
```

The underlying infrastructure may be shared by multiple customers, but cloud providers use logical isolation and security controls to separate customer environments.

### 3.3 Example: Deploying a Spring Boot application on AWS

```text
                 Users
                   |
                Internet
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
              Amazon RDS
                   |
                Amazon S3
```

This is a public cloud deployment because the application uses AWS public cloud infrastructure.

### 3.4 Advantages of Public Cloud

| Advantage | Explanation |
|---|---|
| Low upfront investment | No need to purchase physical servers before starting |
| Scalability | Provision additional resources when needed |
| Global infrastructure | Deploy in multiple Regions |
| Managed services | Use services such as RDS and S3 |
| Agility | Create resources quickly |
| Flexible pricing | Choose from different pricing options |

### 3.5 Disadvantages of Public Cloud

| Disadvantage | Explanation |
|---|---|
| Cost management | Unused or misconfigured resources can create unexpected charges |
| Provider dependency | Architecture may depend on provider-specific services |
| Compliance considerations | Workloads must meet legal and regulatory requirements |
| Internet and connectivity | Users and systems need appropriate network connectivity |
| Less physical control | Customers do not control the provider's underlying hardware |

Public Cloud does not mean that customer data is public. A public cloud account can contain private networks, private databases, and private storage.

## 4. Private Cloud

### 4.1 What is Private Cloud?

A Private Cloud is a cloud environment dedicated to a single organization.

The infrastructure may be operated:

- In the organization's own data centre.
- By a third-party service provider.
- In a dedicated hosted environment.

A private cloud can provide more control over infrastructure configuration and governance, but the organization or its provider still needs to operate and maintain the environment.

### 4.2 Private Cloud architecture

```text
              Organization Network
                       |
                       v
                Private Firewall
                       |
                       v
                Private Cloud
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Compute       Storage      Network
          |
          v
     Applications
          |
          v
      Databases
```

### 4.3 Technologies used for Private Cloud

Examples of technologies used to build private cloud environments include:

| Technology | Purpose |
|---|---|
| VMware vSphere | Virtualization and infrastructure management |
| OpenStack | Open-source cloud infrastructure platform |
| Microsoft Azure Stack | Azure-related services in customer-managed environments |
| Kubernetes | Container orchestration; can be part of a private cloud platform |

Kubernetes by itself is not automatically a complete private cloud. A private cloud usually includes compute, storage, networking, identity, automation, and service management capabilities.

### 4.4 Advantages of Private Cloud

- Dedicated environment for one organization.
- Greater control over infrastructure configuration.
- Can support specialized security and compliance requirements.
- Can be integrated with existing data-centre systems.
- May provide predictable infrastructure placement and governance.

### 4.5 Disadvantages of Private Cloud

- Higher infrastructure and operational costs in many cases.
- Requires skilled infrastructure and operations teams.
- Hardware capacity must be planned and maintained.
- Scaling may require purchasing or installing additional equipment.
- The organization remains responsible for significant infrastructure operations.

### 4.6 Example: Banking system

A bank may operate selected sensitive workloads in a private cloud because of its infrastructure, governance, integration, or regulatory requirements.

This does not mean every bank must use a private cloud. Deployment choices depend on applicable regulation, risk, architecture, and the bank's operating model.

## 5. Hybrid Cloud

### 5.1 What is Hybrid Cloud?

Hybrid Cloud combines a private environment, such as an on-premises data centre or private cloud, with public cloud services.

The environments are connected so that applications and data can work across them.

A hybrid architecture may allow an organization to retain certain systems on-premises while using AWS for additional capacity, backups, analytics, or newer applications.

### 5.2 Hybrid Cloud architecture

```text
             Users / Customers
                    |
                 Internet
                    |
             +------+------+
             |             |
             v             v
       Public Cloud    On-Premises
           AWS          Data Centre
             |             |
             v             v
        AWS Services   Private Systems
             |             |
             +------+------+
                    |
              Secure Network
             Connectivity
```

### 5.3 Real-world example

Imagine a company has an existing database in its data centre.

The company wants to deploy a new Spring Boot application on AWS but still needs to access the existing database.

One possible architecture:

```text
                 Customers
                     |
                  Internet
                     |
                     v
               AWS Application
                  Load Balancer
                     |
                     v
                Spring Boot
                 on EC2
                     |
                     v
               AWS VPC Private
                   Subnet
                     |
             Site-to-Site VPN
                or Direct Connect
                     |
                     v
             On-Premises Network
                     |
                     v
             Existing Database
```

The application runs in AWS, while the existing database remains on-premises.

The connection can use AWS Site-to-Site VPN or AWS Direct Connect, depending on security, performance, availability, and connectivity requirements.

### 5.4 AWS services for Hybrid Cloud

| AWS service | Purpose |
|---|---|
| AWS Site-to-Site VPN | Encrypted network connection between a VPC and an external network |
| AWS Direct Connect | Dedicated network connection from an organization to AWS |
| AWS Storage Gateway | Connects on-premises environments to AWS storage services |
| AWS Outposts | AWS infrastructure and services deployed at a customer site |
| AWS Systems Manager | Helps manage supported hybrid and cloud resources |
| AWS IAM Identity Center | Centralized workforce access management |

### 5.5 Advantages of Hybrid Cloud

- Keep selected systems on-premises.
- Gradually migrate workloads to AWS.
- Connect existing systems to new cloud applications.
- Use cloud resources for additional capacity.
- Support data placement and operational requirements.

### 5.6 Disadvantages of Hybrid Cloud

- Network architecture is more complex.
- Requires secure and reliable connectivity.
- Monitoring and troubleshooting span multiple environments.
- Identity and access management can be more complicated.
- Data movement and integration need careful design.

## 6. Multi-Cloud

### 6.1 What is Multi-Cloud?

Multi-Cloud means using services from more than one cloud provider.

For example, an organization may use:

- AWS for application hosting.
- Microsoft Azure for selected enterprise services.
- Google Cloud for data analytics or machine learning.

Multi-Cloud is about using multiple cloud providers. It does not necessarily mean that an on-premises data centre is involved.

### 6.2 Multi-Cloud architecture

```text
                  Organization
                       |
              +--------+--------+
              |        |        |
              v        v        v
             AWS     Azure     GCP
              |        |        |
              v        v        v
          Applications Services Analytics
```

### 6.3 Example

A company may:

- Run its Spring Boot application on AWS.
- Use Microsoft Azure for an existing enterprise identity or productivity ecosystem.
- Use Google Cloud for a specific analytics workload.

The services need appropriate identity, networking, data integration, security, and monitoring arrangements.

### 6.4 Advantages of Multi-Cloud

- Access to services from different providers.
- Can reduce dependence on one provider for selected workloads.
- Can support business, technical, or geographic requirements.
- Allows teams to select services based on workload needs.

### 6.5 Disadvantages of Multi-Cloud

- More complex architecture.
- Teams need knowledge of multiple platforms.
- Different identity and security systems must be integrated.
- Monitoring and cost management can be fragmented.
- Moving data between providers can introduce cost and latency.

Multi-Cloud does not automatically prevent vendor lock-in. Applications can still depend heavily on provider-specific services.

## 7. Compare the four deployment models

| Feature | Public Cloud | Private Cloud | Hybrid Cloud | Multi-Cloud |
|---|---|---|---|---|
| Environment | Provider cloud | Dedicated to one organization | Private plus public | Multiple cloud providers |
| Physical infrastructure | Provider-operated | Organization or dedicated provider | Combination | Multiple providers |
| Upfront investment | Often lower | Often higher | Varies | Varies |
| Scalability | Usually high | Depends on capacity | Combines environments | Depends on providers |
| Operational complexity | Varies | Often significant | High | High |
| Typical use | Web and business applications | Dedicated organizational workloads | Existing systems plus cloud | Workloads across providers |

### Quick way to remember

- **Public Cloud:** Use a cloud provider's public cloud services.
- **Private Cloud:** Dedicated cloud environment for one organization.
- **Hybrid Cloud:** Connect private infrastructure with public cloud.
- **Multi-Cloud:** Use more than one cloud provider.

## 8. Hybrid Cloud vs Multi-Cloud

These concepts are often confused.

| Feature | Hybrid Cloud | Multi-Cloud |
|---|---|---|
| Main idea | Combine private and public environments | Use multiple cloud providers |
| Requires on-premises/private environment? | Yes, in the usual definition | No |
| Requires multiple public cloud providers? | No | Yes |
| Example | On-premises database + AWS application | AWS application + Azure service |
| Main challenge | Integration and connectivity across environments | Consistency across cloud providers |

An organization can use both Hybrid Cloud and Multi-Cloud at the same time.

For example, it may connect an on-premises data centre to AWS and also use Azure for another workload.

## 9. How to choose a deployment model

There is no universally best deployment model. Choose based on business requirements.

| Requirement | Possible choice | Reason |
|---|---|---|
| Launch a new web application quickly | Public Cloud | Fast provisioning and managed services |
| Dedicated infrastructure control | Private Cloud | Dedicated environment and governance |
| Keep an existing database on-premises while moving applications to AWS | Hybrid Cloud | Connects existing and cloud systems |
| Use services from AWS and Azure | Multi-Cloud | Multiple providers |
| Gradually migrate an existing data centre | Hybrid Cloud | Supports staged migration |
| Avoid unnecessary operational complexity | Often a single cloud environment | Fewer platforms to integrate |

Before choosing, consider:

1. Security and compliance requirements.
2. Application architecture.
3. Existing infrastructure.
4. Network connectivity.
5. Skills and operational capacity.
6. Availability and disaster recovery requirements.
7. Total cost of ownership.
8. Data location and data transfer requirements.

## 10. AWS hands-on: Identify your AWS account and Region

This lesson focuses on deployment models rather than creating infrastructure. We can still use the AWS CLI to identify the account and default Region.

Check your identity:

```bash
aws sts get-caller-identity
```

Example response:

```json
{
  "UserId": "AIDAEXAMPLE",
  "Account": "123456789012",
  "Arn": "arn:aws:iam::123456789012:user/example-user"
}
```

The exact identity will depend on your configured credentials. In production, prefer IAM Identity Center or short-lived role credentials rather than long-lived IAM user access keys.

Check your configured Region:

```bash
aws configure get region
```

Set a default Region:

```bash
aws configure set region ap-southeast-1
```

This sets a CLI default. It does not move existing resources or change the Region of resources already created.

## 11. Practical exercises with answers

### Exercise 1 — Public Cloud

**Question:** A startup deploys its Spring Boot application using Amazon EC2 and Amazon RDS. Which deployment model is this?

A. Private Cloud  
B. Public Cloud  
C. On-Premises only  
D. No cloud

**Answer: B. Public Cloud.**

The startup consumes AWS public cloud services.

### Exercise 2 — Private Cloud

**Question:** An organization operates a cloud environment dedicated to itself in its own data centre. Which model is this?

**Answer: Private Cloud.**

The environment is dedicated to one organization.

### Exercise 3 — Hybrid Cloud

**Scenario:** A company runs its application on AWS but keeps its database in its own data centre. The two environments are connected through a secure network.

**Question:** Which deployment model is this?

**Answer: Hybrid Cloud.**

It combines public cloud infrastructure with an on-premises environment.

### Exercise 4 — Multi-Cloud

**Scenario:** A company uses AWS for application hosting and Azure for another business workload.

**Question:** Which deployment model is this?

**Answer: Multi-Cloud.**

The company uses services from multiple cloud providers.

### Exercise 5 — Choose a deployment model

Match the scenario to a suitable model.

| Scenario | Suggested answer |
|---|---|
| Startup launches a new application on AWS | Public Cloud |
| Organization operates a dedicated cloud environment | Private Cloud |
| AWS application connects to an on-premises database | Hybrid Cloud |
| Application uses AWS and Azure | Multi-Cloud |
| Company gradually migrates from its data centre to AWS | Hybrid Cloud during migration |

### Exercise 6 — Hybrid connectivity

**Question:** Name two AWS services or solutions that can connect an on-premises network to AWS.

**Answer:**

- AWS Site-to-Site VPN.
- AWS Direct Connect.

Site-to-Site VPN provides an encrypted connection over the internet. Direct Connect provides dedicated network connectivity.

### Exercise 7 — Architecture design

**Scenario:** A company has a legacy database in its data centre. It wants to deploy a new Spring Boot API on AWS without immediately moving the database.

**Suggested answer:**

```text
             Customer
                 |
              Internet
                 |
                 v
           AWS Application
                 |
              Spring Boot
                 |
               AWS VPC
                 |
          Site-to-Site VPN
                 |
                 v
          On-Premises Network
                 |
                 v
          Legacy Database
```

This is a Hybrid Cloud architecture.

## 12. Vietnamese vocabulary with pronunciation

Pronunciation is approximate and intended as a speaking aid.

| English | Pronunciation | Vietnamese |
|---|---|---|
| Deployment Model | di-PLOY-mənt MOD-əl | Mô hình triển khai |
| Public Cloud | PUB-lik KLAUD | Đám mây công cộng |
| Private Cloud | PRAI-vət KLAUD | Đám mây riêng |
| Hybrid Cloud | HAI-brid KLAUD | Đám mây lai |
| Multi-Cloud | MUL-tee KLAUD | Đa đám mây |
| Data Centre | DAY-tə SEN-tər | Trung tâm dữ liệu |
| Dedicated | DED-i-kay-tid | Dành riêng |
| Infrastructure | IN-frə-struhk-chər | Cơ sở hạ tầng |
| Connectivity | kon-ek-TIV-ə-tee | Khả năng kết nối |
| Integration | in-ti-GRAY-shən | Tích hợp |
| Migration | mai-GRAY-shən | Di chuyển hệ thống |
| Workload | WERK-lohd | Khối lượng công việc |
| Compliance | kəm-PLAI-əns | Tuân thủ |
| Governance | GUV-er-nəns | Quản trị |
| Network | NET-wərk | Mạng |
| Secure Connection | si-KYOOR kə-NEK-shən | Kết nối an toàn |
| Cloud Provider | KLAUD prə-VAI-dər | Nhà cung cấp đám mây |
| Vendor Lock-in | VEN-dər lok-in | Phụ thuộc nhà cung cấp |
| Scalability | skay-lə-BIL-ə-tee | Khả năng mở rộng |
| Operational Complexity | op-ə-RAY-shən-əl kəm-PLEK-si-tee | Độ phức tạp vận hành |

## 13. Useful English sentences

| English | Vietnamese |
|---|---|
| Public Cloud provides computing services over the internet. | Public Cloud cung cấp dịch vụ điện toán qua internet. |
| A Private Cloud is dedicated to one organization. | Private Cloud dành riêng cho một tổ chức. |
| Hybrid Cloud combines private infrastructure and public cloud services. | Hybrid Cloud kết hợp hạ tầng riêng và dịch vụ đám mây công cộng. |
| Multi-Cloud uses services from multiple cloud providers. | Multi-Cloud sử dụng dịch vụ từ nhiều nhà cung cấp đám mây. |
| Our database is running on-premises. | Cơ sở dữ liệu của chúng tôi đang chạy tại chỗ. |
| Our application runs on AWS. | Ứng dụng của chúng tôi chạy trên AWS. |
| We connect our data centre to AWS using a VPN. | Chúng tôi kết nối trung tâm dữ liệu với AWS bằng VPN. |
| The company is migrating its applications to the cloud. | Công ty đang di chuyển các ứng dụng lên đám mây. |
| We need to consider security and compliance requirements. | Chúng ta cần xem xét các yêu cầu bảo mật và tuân thủ. |
| Multi-Cloud can increase operational complexity. | Multi-Cloud có thể làm tăng độ phức tạp vận hành. |

## 14. English speaking practice

### Topic: Explain Cloud Deployment Models

Read aloud:

> There are several cloud deployment models.
>
> The first model is Public Cloud. In this model, a cloud provider offers computing services over the internet. Amazon Web Services is an example of a public cloud provider.
>
> The second model is Private Cloud. A private cloud is dedicated to one organization. It can provide more control over infrastructure and configuration.
>
> The third model is Hybrid Cloud. Hybrid Cloud combines private infrastructure with public cloud services. For example, a company can run its Spring Boot application on AWS while keeping its database in an on-premises data centre.
>
> The fourth model is Multi-Cloud. Multi-Cloud means using services from multiple cloud providers, such as AWS and Microsoft Azure.
>
> Each deployment model has advantages and disadvantages. Companies should choose a model based on security, cost, compliance, connectivity, and business requirements.

### Speaking questions and model answers

**Question 1: What is Public Cloud?**

> Public Cloud is a cloud environment where a provider offers computing services to customers. AWS is an example of a public cloud provider.

**Question 2: What is Private Cloud?**

> Private Cloud is a cloud environment dedicated to one organization.

**Question 3: What is Hybrid Cloud?**

> Hybrid Cloud combines private infrastructure with public cloud services.

**Question 4: What is Multi-Cloud?**

> Multi-Cloud means using cloud services from more than one provider, such as AWS and Azure.

**Question 5: What is the difference between Hybrid Cloud and Multi-Cloud?**

> Hybrid Cloud combines private and public environments. Multi-Cloud uses multiple cloud providers.

**Question 6: Which deployment model can connect an on-premises database to an AWS application?**

> Hybrid Cloud is suitable because it connects the company's existing infrastructure with public cloud services.

## 15. Interview questions

**Q1. What is a cloud deployment model?**

A cloud deployment model describes how cloud infrastructure is organized, operated, and made available to users.

**Q2. What is Public Cloud?**

Public Cloud provides cloud services through a provider-operated infrastructure that serves multiple customers with logical isolation.

**Q3. What is Private Cloud?**

Private Cloud is a cloud environment dedicated to one organization.

**Q4. What is Hybrid Cloud?**

Hybrid Cloud combines private infrastructure with public cloud services and connects them to support workloads and data across environments.

**Q5. What is Multi-Cloud?**

Multi-Cloud is the use of services from multiple cloud providers.

**Q6. What is the difference between Hybrid Cloud and Multi-Cloud?**

Hybrid Cloud combines private and public environments. Multi-Cloud uses more than one cloud provider. An organization can use both.

**Q7. What is AWS Site-to-Site VPN?**

It provides an encrypted network connection between an organization's network and an AWS VPC over the internet.

**Q8. What is AWS Direct Connect?**

It provides dedicated network connectivity from an organization's network to AWS.

**Q9. Why might a company choose Private Cloud?**

It may need a dedicated environment, specific infrastructure controls, integration with existing systems, or particular governance requirements.

**Q10. What are the disadvantages of Multi-Cloud?**

Multi-Cloud can increase operational complexity, skills requirements, monitoring effort, security integration work, and data transfer costs.

**Q11. Does Public Cloud mean that data is publicly accessible?**

No. Public Cloud describes the provider's cloud model. Customer resources can remain private through IAM, network controls, encryption, and resource policies.

**Q12. How would you design a Hybrid Cloud architecture for Spring Boot?**

I could deploy the Spring Boot application on EC2 inside an AWS VPC and connect it securely to an on-premises database using Site-to-Site VPN or Direct Connect.

## 16. DAY 2 summary

| Concept | Key point |
|---|---|
| Deployment Model | Describes how cloud infrastructure is organized and used |
| Public Cloud | Provider-operated cloud services available to customers |
| Private Cloud | Cloud environment dedicated to one organization |
| Hybrid Cloud | Combines private infrastructure and public cloud |
| Multi-Cloud | Uses multiple cloud providers |
| Site-to-Site VPN | Encrypted network connection to AWS |
| Direct Connect | Dedicated network connection to AWS |
| Vendor Lock-in | Dependence on a provider's services or technology |
| Compliance | Meeting legal, regulatory, and organizational requirements |

## 17. Progress checklist

- [ ] Understand what a cloud deployment model is.
- [ ] Understand Public Cloud.
- [ ] Understand Private Cloud.
- [ ] Understand Hybrid Cloud.
- [ ] Understand Multi-Cloud.
- [ ] Compare the four deployment models.
- [ ] Explain Hybrid Cloud vs Multi-Cloud.
- [ ] Understand AWS Site-to-Site VPN.
- [ ] Understand AWS Direct Connect.
- [ ] Design a simple Hybrid Cloud architecture.
- [ ] Complete the practical exercises.
- [ ] Review the interview questions.
- [ ] Practice the English speaking topic.

## 18. What you should understand before moving to Day 3

Make sure you can explain these questions in your own words:

1. What is a Public Cloud?
2. What is a Private Cloud?
3. What is a Hybrid Cloud?
4. What is a Multi-Cloud?
5. What is the difference between Hybrid Cloud and Multi-Cloud?
6. How can an on-premises database connect to an AWS application?
7. What is the difference between AWS Site-to-Site VPN and Direct Connect?

---

## Next lesson — DAY 3: Cloud Service Models (IaaS, PaaS, SaaS)

In Day 3, we will study:

- Infrastructure as a Service (IaaS).
- Platform as a Service (PaaS).
- Software as a Service (SaaS).
- Differences between IaaS, PaaS, and SaaS.
- Real-world AWS examples.
- Shared Responsibility Model introduction.
- Practical exercises with answers.
- Vietnamese vocabulary and English speaking practice.
