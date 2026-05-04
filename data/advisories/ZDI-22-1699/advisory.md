# ZDI-22-1699: X.Org Server ProcXIChangeProperty Numeric Truncation Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1699
- **ZDI-CAN:** ZDI-CAN-19405
- **Date:** 2022-12-28
- **CVE:** CVE-2022-46344
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1699/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of ProcXIChangeProperty requests. The issue results from the lack of proper validation of user-supplied data, which can result in a numeric truncation before allocating a buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2022-December/003302.html

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2022-12-28 - Coordinated public release of advisory
