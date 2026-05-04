# ZDI-26-252: Mozilla Firefox IonMonkey Switch Statement Optimization Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-252
- **ZDI-CAN:** ZDI-CAN-29301
- **Date:** 2026-04-02
- **CVE:** CVE-2026-4698
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** maxpl0it
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-252/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within IonMonkey when optimizing JavaScript switch statements. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://hg-edge.mozilla.org/releases/mozilla-esr115/rev/ae75e9f5366f , https://www.mozilla.org/en-US/security/advisories/mfsa2026-22/#CVE-2026-4698

## Disclosure Timeline

- 2026-03-02 - Vulnerability reported to vendor
- 2026-04-02 - Coordinated public release of advisory
- 2026-04-02 - Advisory Updated
