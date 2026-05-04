# ZDI-20-1221: Trend Micro Apex One scanServer64 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1221
- **ZDI-CAN:** ZDI-CAN-10848
- **Date:** 2020-09-25
- **CVE:** CVE-2020-25770
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn and Jay Lo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1221/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the scanServer64 module. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000271974

## Disclosure Timeline

- 2020-05-12 - Vulnerability reported to vendor
- 2020-09-25 - Coordinated public release of advisory
