# ZDI-20-126: (Pwn2Own) Sony X800G Smart TV Vewd Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-126
- **ZDI-CAN:** ZDI-CAN-9641
- **Date:** 2020-01-15
- **CVE:** CVE-2017-5030
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Sony
- **Affected Products:** X800G Smart TV
- **Credit:** @fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-126/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sony X800G Smart TV. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of arrays in Vewd. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this to execute code in the context of the current process.

## Additional Details

Fixed in Vewd 4.11

## Disclosure Timeline

- 2019-11-07 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
- 2020-02-21 - Advisory Updated
