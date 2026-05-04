# ZDI-23-1050: (0Day) (Pwn2Own) Inductive Automation Ignition ConditionRefresh Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1050
- **ZDI-CAN:** ZDI-CAN-20499
- **Date:** 2023-08-08
- **CVE:** CVE-2023-39477
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Vens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1050/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Inductive Automation Ignition. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of OPC UA ConditionRefresh requests. By sending a large number of requests, an attacker can consume all available resources on the server. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://inductiveautomation.com/downloads/releasenotes/8.1.33

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-08 - Coordinated public release of advisory
- 2023-12-19 - Advisory Updated
