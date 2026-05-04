# ZDI-20-1130: Microsoft Windows State Repository Service Race Condition Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1130
- **ZDI-CAN:** ZDI-CAN-11126
- **Date:** 2020-09-10
- **CVE:** CVE-2020-0914
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1130/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the State Repository Service. The issue results from the lack of proper locking when performing operations on an object, which can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0914

## Disclosure Timeline

- 2020-06-17 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory
