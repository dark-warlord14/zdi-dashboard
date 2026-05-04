# ZDI-20-253: (Pwn2Own) Samsung Galaxy S10 Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-253
- **ZDI-CAN:** ZDI-CAN-9654
- **Date:** 2020-02-20
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S10
- **Credit:** @fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy S10. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays in JSCallReducer::ReduceArrayMap. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 11.0.00.76

## Disclosure Timeline

- 2019-11-07 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
- 2020-02-21 - Advisory Updated
