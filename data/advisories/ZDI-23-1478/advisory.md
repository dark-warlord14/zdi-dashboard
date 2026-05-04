# ZDI-23-1478: (0Day) Control Web Panel Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1478
- **ZDI-CAN:** ZDI-CAN-20582
- **Date:** 2023-09-27
- **CVE:** CVE-2023-42121
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Control Web Panel
- **Affected Products:** Control Web Panel
- **Credit:** Muhammad Ikhsanudin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1478/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Control Web Panel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of authentication within the web interface. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of a valid CWP user.

## Additional Details

05/09/23 – ZDI requested a PSIRT contact. 05/10/23 – The vendor provided a contact, and ZDI reported the vulnerability to the vendor. 09/22/23 – ZDI asked for an update and informed the vendor that we intend to publish the case as a zero-day advisory on 09/27/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-05-10 - Vulnerability reported to vendor
- 2023-09-27 - Coordinated public release of advisory
