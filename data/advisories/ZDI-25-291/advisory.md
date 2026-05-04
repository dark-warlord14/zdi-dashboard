# ZDI-25-291: (Pwn2Own) Mozilla Firefox IonMonkey JIT Compiler Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-291
- **ZDI-CAN:** ZDI-CAN-27172
- **Date:** 2025-05-21
- **CVE:** CVE-2025-4919
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Manfred Paul (@manf@infosec.exchange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IonMonkey JIT compiler. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2025-36/

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
