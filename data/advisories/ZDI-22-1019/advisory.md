# ZDI-22-1019: (Pwn2Own) Inductive Automation Ignition Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1019
- **ZDI-CAN:** ZDI-CAN-17115
- **Date:** 2022-07-15
- **CVE:** CVE-2022-35872
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ZIP files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://support.inductiveautomation.com/hc/en-us/articles/7625759776653-Regarding-Pwn2Own-2022-Vulnerabilities

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-07-15 - Coordinated public release of advisory
