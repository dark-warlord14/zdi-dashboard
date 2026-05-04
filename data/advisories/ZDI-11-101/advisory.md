# ZDI-11-101: Apple iPhone Webkit Library Javascript Array sort Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-101
- **ZDI-CAN:** ZDI-CAN-918
- **Date:** 2011-03-02
- **CVE:** CVE-2011-0154
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-101/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's iPhone Webkit library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the library implements the .sort function for an array. The library will trust the implementation of a particular method which when executed can be used to manipulate elements out from underneath it. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4554

## Disclosure Timeline

- 2010-09-29 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory
