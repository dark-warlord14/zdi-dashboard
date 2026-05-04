# ZDI-18-607: Apple macOS IOGraphics IDState Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-607
- **ZDI-CAN:** ZDI-CAN-6204
- **Date:** 2018-07-10
- **CVE:** CVE-2018-4283
- **CVSS:** 6.3
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** juwei lin (@panicaII) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-607/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the IOGraphics kext. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208937

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-07-10 - Coordinated public release of advisory
- 2018-07-10 - Advisory Updated
