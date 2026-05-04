# ZDI-17-639: Microsoft Windows Error Reporting Manager Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-639
- **ZDI-CAN:** ZDI-CAN-4770
- **Date:** 2017-08-08
- **CVE:** CVE-2017-8633
- **CVSS:** 2.6
- **CVSS Vector:** AV:L/AC:H/Au:N/C:N/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Thomas Vanhoutte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-639/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute medium-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Error Reporting Manager (wermgr). The issue results from the lack of proper validation of a path prior to using it in file operations. An attacker can leverage this vulnerability to delete any files accessible to SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8633

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
