# ZDI-20-1432: (0Day) Microsoft Windows splwow64 Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1432
- **ZDI-CAN:** ZDI-CAN-11351
- **Date:** 2020-12-15
- **CVE:** CVE-2021-1648
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1432/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the user-mode printer driver host process splwow64.exe. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges from low integrity and execute code in the context of the current user at medium integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/01/20 - ZDI reported the vulnerability to Microsoft 07/01/20 - Microsoft confirmed receipt of the report 08/18/20 - Microsoft requested an extension until 11/10/20 08/19/20 - ZDI agreed to the extension 10/29/20 - Microsoft requested an extension until 12/10/20 10/29/20 - ZDI agreed to the extension 12/03/20 - Microsoft requested an extension until 01/10/21 12/07/20 - ZDI notified Microsoft of the intention to publish these reports as 0-day advisories on 12/15/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
