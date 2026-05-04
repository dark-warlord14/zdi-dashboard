# ZDI-23-1060: (0Day) (Pwn2Own) Softing Secure Integration Server Exposure of Resource to Wrong Sphere Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1060
- **ZDI-CAN:** ZDI-CAN-20547
- **Date:** 2023-08-09
- **CVE:** CVE-2023-39478
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1060/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Softing Secure Integration Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of OPC FileDirectory namespaces. The issue results from the lack of proper validation of user-supplied data before using it to create a server object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

02/16/23 – The ZDI reported this vulnerability to the vendor during the Pwn2Own Miami contest. 02/20/23 – The vendor states they would review and report back with the security advisories. 03/08/23 – The vendor requested CVE Numbers. 03/15/23 – ZDI provided the vendor with CVE numbers. 07/31/23 – ZDI asked for an update. 08/03/23 – ZDI asked for an update. 08/07/23 – The ZDI asked for an update and informed the vendor that we are publishing this case as a zero-day advisory on 08/09/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
