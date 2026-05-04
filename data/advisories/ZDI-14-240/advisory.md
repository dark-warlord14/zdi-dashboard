# ZDI-14-240: Apple OS X Dock Service Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-240
- **ZDI-CAN:** ZDI-CAN-2285
- **Date:** 2014-07-18
- **CVE:** CVE-2014-1371
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-240/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the OS X Dock. The issue lies in the failure to proper sanitize a user-supplied value prior to indexing into an array of function pointers. An attacker could leverage this vulnerability to execute code within the context of the Dock process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6296

## Disclosure Timeline

- 2014-04-23 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
