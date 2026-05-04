# ZDI-20-682: Apple Safari HasIndexedProperty Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-682
- **ZDI-CAN:** ZDI-CAN-10504
- **Date:** 2020-05-28
- **CVE:** CVE-2020-9800
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Brendan Draper (@6r3nd4n)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-682/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the HasIndexedProperty DFG node. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://support.apple.com/en-gb/HT211177

## Disclosure Timeline

- 2020-02-26 - Vulnerability reported to vendor
- 2020-05-28 - Coordinated public release of advisory
