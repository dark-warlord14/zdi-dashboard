# ZDI-24-664: (Pwn2Own) Mozilla Firefox SpiderMonkey JIT Compiler Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-664
- **ZDI-CAN:** ZDI-CAN-23794
- **Date:** 2024-06-12
- **CVE:** CVE-2024-29943
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Manfred Paul (@_manfp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-664/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SpiderMonkey JIT compiler. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2024-15/#CVE-2024-29943

## Disclosure Timeline

- 2024-03-26 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
