# ZDI-25-092: (Pwn2Own) Apple Safari B3 JIT Compiler Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-092
- **ZDI-CAN:** ZDI-CAN-23795
- **Date:** 2025-02-24
- **CVE:** CVE-2024-27833
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Manfred Paul (@_manfp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-092/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the B3 JIT compiler. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow that causes an incorrect optimization. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-la/120896

## Disclosure Timeline

- 2024-03-26 - Vulnerability reported to vendor
- 2025-02-24 - Coordinated public release of advisory
- 2025-02-24 - Advisory Updated
