# ZDI-20-341: Apple Safari Object Transition Cache Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-341
- **ZDI-CAN:** ZDI-CAN-9855
- **Date:** 2020-03-26
- **CVE:** CVE-2020-3897
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Brendan Draper (@6r3nd4n)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-341/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the object transition cache. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-eg/HT211104

## Disclosure Timeline

- 2019-12-19 - Vulnerability reported to vendor
- 2020-03-26 - Coordinated public release of advisory
