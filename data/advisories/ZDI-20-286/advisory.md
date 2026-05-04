# ZDI-20-286: (Pwn2Own) Xiaomi Mi9 Browser ParseFormalParameterList Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-286
- **ZDI-CAN:** ZDI-CAN-9646
- **Date:** 2020-03-12
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** @fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-286/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Xiaomi Mi9 Browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the ParseFormalParameterList function. The issue results from the lack of proper validation of user-supplied data before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in v11.4.4-g

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
