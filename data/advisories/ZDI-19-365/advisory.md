# ZDI-19-365: (Pwn2Own) Mozilla Firefox IonMonkey Optimizer Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-365
- **ZDI-CAN:** ZDI-CAN-8373
- **Date:** 2019-04-15
- **CVE:** CVE-2019-9813
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Niklas Baumstark (@_niklasb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-365/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within IonMonkey. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2019-09/#CVE-2019-9813

## Disclosure Timeline

- 2019-03-21 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
