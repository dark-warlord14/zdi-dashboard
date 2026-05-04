# ZDI-10-094: Apple Webkit SelectionController via Marquee Event Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-094
- **ZDI-CAN:** ZDI-CAN-687
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1399
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit. User interaction is required in that a user must be coerced into viewing a website. The specific flaw exists within the way the library handles selections. If a particular element is selected by the application, an event can be triggered in order to interrupt execution handling a component of the selection. By modification of the elements contained in the selection by the interruption, an attacker can substitute contents of their own choosing in their place. This type switch can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-02-23 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
