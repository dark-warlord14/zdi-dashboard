# ZDI-17-735: Microsoft Windows PlgBlt Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-735
- **ZDI-CAN:** ZDI-CAN-5082
- **Date:** 2017-09-15
- **CVE:** CVE-2017-8720
- **CVSS:** 1.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-735/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within vPlgWrite1 in the win32kfull driver. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8720

## Disclosure Timeline

- 2017-08-04 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
