# ZDI-16-685: Apple OS X IOCommandQueue Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-685
- **ZDI-CAN:** ZDI-CAN-3854
- **Date:** 2017-06-21
- **CVE:** CVE-2016-7624
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Qidan He(@flanker_hqd) from KeenLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-685/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within IOCommandQueue. The process does not properly validate user-supplied data which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207423

## Disclosure Timeline

- 2016-09-06 - Vulnerability reported to vendor
- 2017-06-21 - Coordinated public release of advisory
