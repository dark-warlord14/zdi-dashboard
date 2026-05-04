# ZDI-21-090: (0Day) Microsoft Windows win32kfull bRotate NULL Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-090
- **ZDI-CAN:** ZDI-CAN-12671
- **Date:** 2021-01-27
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-090/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull.sys driver. The issue results from dereferencing a NULL pointer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/23/20 – ZDI reported the vulnerability to the vendor 12/23/20 – The vendor acknowledged the report 12/28/20 – The vendor indicated the case does not meet the bar for servicing 01/19/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 01/27/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-01-27 - Coordinated public release of advisory
