# ZDI-22-1467: (0Day) IronCAD STP File Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1467
- **ZDI-CAN:** ZDI-CAN-17672
- **Date:** 2022-10-25
- **CVE:** CVE-2022-43609
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** IronCAD
- **Affected Products:** IronCAD
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1467/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IronCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of STP files. When parsing the VECTOR element, the process does not properly initialize a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/19/22 – ZDI reported the vulnerability to the vendor. 07/26/22 – ZDI asked for an update. 08/25/22 – ZDI called their technical support line, and they confirmed that we were using the right email to contact them. 08/25/22 – ZDI emailed the vendor and referenced the telephone conversation. 08/30/22 – ZDI asked for an update. 10/20/22 – ZDI informed the vendor that the case will be published as a zero-day advisory on 10/25/22. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-10-20 - Vulnerability reported to vendor
- 2022-10-25 - Coordinated public release of advisory
