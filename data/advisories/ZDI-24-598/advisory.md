# ZDI-24-598: (0Day) Microsoft Windows Incorrect Permission Assignment Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-598
- **ZDI-CAN:** ZDI-CAN-16220
- **Date:** 2024-06-11
- **CVE:** N/A
- **CVSS:** 7.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Uncodable
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-598/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information or to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Furthermore, the vulnerable behavior occurs only in certain hardware configurations. The specific flaw exists within the Volume Manager. The issue results from incorrect permissions set on an object. An attacker can leverage this vulnerability to disclose information in the context of the kernel. An attacker can also leverage this to create a denial-of-service condition on the system.

## Additional Details

02/08/22 – ZDI reported the vulnerability to the vendor. 02/08/22 – The vendor acknowledged the report. 02/16/22 – The vendor asks for an extension till Patch Tuesday of June 2022. 02/23/22 – The vendor asked for additional details. 02/23/22 – ZDI provided additional details. 03/04/22 – The vendor states this is not a Microsoft issue, but an issue in third-party software and that we should report it to them. 08/31/22 – The ZDI reported the vulnerability to the third-party vendor. 09/07/22 – The vendor states the issue is a Microsoft problem. 05/24/24 – From October 2022 to May 2024, ongoing discussions were had between Microsoft and the third-party vendor with ZDI monitoring progress along the way. 05/24/24 – After a lengthy debate between the engineering teams for Microsoft and the third-party vendor over the course of several months, it was determined that Microsoft is responsible for this vulnerability. 05/24/24 – The ZDI informed the vendor that we intend to publish this case as a zero-day advisory on 06/11/24 if there isn’t a fix available before then. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2024-06-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
