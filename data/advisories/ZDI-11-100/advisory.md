# ZDI-11-100: Apple Webkit Root HTMLBRElement Style Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-100
- **ZDI-CAN:** ZDI-CAN-969
- **Date:** 2011-03-02
- **CVE:** CVE-2011-0149
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-100/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a specially formatted HTML file. When parsing a particular element that also defines the namespace of the document, the library will call a dangling pointer which is consistent but unmapped. Due to this being unmapped, if an attacker can get code loaded at that address this can can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4554

## Disclosure Timeline

- 2010-10-18 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory
