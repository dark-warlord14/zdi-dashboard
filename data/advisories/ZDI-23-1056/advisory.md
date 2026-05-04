# ZDI-23-1056: (0Day) Microsoft Azure Machine Learning Compute Instance certificate Exposure of Resource to Wrong Sphere Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1056
- **ZDI-CAN:** ZDI-CAN-20771
- **Date:** 2023-08-09
- **CVE:** N/A
- **CVSS:** 4.4
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Nitesh Surana (@_niteshsurana) & David Fiser (@anu4is) of Project Nebula, Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1056/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on Microsoft Azure. An attacker must first obtain the ability to execute high-privileged code on the target environment in order to exploit this vulnerability. The specific flaw exists within the handling of certificates. The issue results from the exposure of a resource to the wrong control sphere. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

04/07/23 – ZDI reported the vulnerability to the vendor. 04/11/23 – The vendor acknowledged the report. 07/13/23 – ZDI asked for an update. 07/19/23 – The vendor asked us to join a call to discuss the report. 07/19/23 – ZDI joined the call and provided the vendor with additional details. 07/20/23 – The vendor states that they are considering this bug low severity and that they would release a fix in 30-45 days. 07/20/23 – The ZDI informed the vendor that the case is due on 08/05/23 and that we are publishing this case as a zero-day advisory on 08/09/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-04-07 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
- 2023-08-09 - Advisory Updated
