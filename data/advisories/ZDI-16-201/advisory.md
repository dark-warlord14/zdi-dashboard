# ZDI-16-201: Apple OS X PDF Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-201
- **ZDI-CAN:** ZDI-CAN-3460
- **Date:** 2016-03-22
- **CVE:** CVE-2016-1740
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** HappilyCoded (ant4g0nist & r3dsm0k3)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-201/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDF files. The issue lies in the parsing of encoded fonts containing invalid characters. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206167

## Disclosure Timeline

- 2015-12-17 - Vulnerability reported to vendor
- 2016-03-22 - Coordinated public release of advisory
