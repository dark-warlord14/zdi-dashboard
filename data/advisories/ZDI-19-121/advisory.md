# ZDI-19-121: (0Day) Microsoft Windows contact File Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-121
- **ZDI-CAN:** ZDI-CAN-7591
- **Date:** 2019-01-22
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** John Page (aka hyp3rlinx)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-121/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of CONTACT files. Crafted data in a CONTACT file can cause Windows to display a dangerous hyperlink. The user interface fails to provide sufficient indication of the hazard. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

12/04/18 - ZDI reported the vulnerability to the vendor 12/04/18 - The vendor acknowledged the report 12/05/18 - The vendor provided a tracking # 12/13/18 - The vendor requested additional information 12/13/18 - ZDI provided the requested additional information 01/04/19 - The vendor notified ZDI that “we've determined that we will not address this issue via a monthly security update, so we will be closing this case. Instead, the team will address this in a future release of Windows” 01/07/19 - ZDI notified the vendor of the intent to publish the report as 0-day on 01/22/19

## Disclosure Timeline

- 2018-12-04 - Vulnerability reported to vendor
- 2019-01-22 - Coordinated public release of advisory
- 2019-05-30 - Advisory Updated
