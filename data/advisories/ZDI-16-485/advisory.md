# ZDI-16-485: Apple Safari Array.slice Out-Of-Bounds Access Remote Code Execuction Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-485
- **ZDI-CAN:** ZDI-CAN-3673
- **Date:** 2016-08-18
- **CVE:** CVE-2016-4622
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Samuel Groß
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-485/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Array.slice. The issue lies in the failure to ensure that an array's length has not changed during processing of user-supplied arguments. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206900

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-08-18 - Coordinated public release of advisory
