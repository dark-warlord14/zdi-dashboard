# ZDI-10-096: Apple Webkit Recursive Use Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-096
- **ZDI-CAN:** ZDI-CAN-711
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1404
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the WebKit library handles recursively defined Use elements. Upon expanding the target of the use element within the tree, the application will create a dual-reference of a Use element. Upon page deconstruction the application will destroy the single reference and then attempt to destroy the second one that is currently occupying the recently freed memory. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-02-23 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
