# ZDI-20-1214: Apple Safari replace Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1214
- **ZDI-CAN:** ZDI-CAN-11116
- **Date:** 2020-09-21
- **CVE:** CVE-2020-9948
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Brendan Draper (@6r3nd4n)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1214/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the optimization of calls to String.prototype.replace. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-gb/HT211845

## Disclosure Timeline

- 2020-07-15 - Vulnerability reported to vendor
- 2020-09-21 - Coordinated public release of advisory
