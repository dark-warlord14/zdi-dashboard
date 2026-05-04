# ZDI-21-501: Microsoft Windows win32kfull MulDrawStream Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-501
- **ZDI-CAN:** ZDI-CAN-12577
- **Date:** 2021-04-29
- **CVE:** CVE-2021-27077
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-501/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull.sys driver. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-27077

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-04-29 - Coordinated public release of advisory
