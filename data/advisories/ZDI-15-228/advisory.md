# ZDI-15-228: Apple Safari file:// Redirection Sandbox Escape Vulnerabliity

## Metadata

- **ZDI ID:** ZDI-15-228
- **ZDI-CAN:** ZDI-CAN-2783
- **Date:** 2015-05-15
- **CVE:** CVE-2015-1155
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Joe Vennix of Rapid7 Inc.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-228/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of popups to invalid pages. The issue lies in the ability to control the history of a window with higher privileges. An attacker can leverage this vulnerability to execute code outside the context of the Safari sandbox.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT204826

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-05-15 - Coordinated public release of advisory
