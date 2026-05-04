# ZDI-16-200: Apple Safari Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-200
- **ZDI-CAN:** ZDI-CAN-3449
- **Date:** 2016-03-22
- **CVE:** CVE-2016-1778
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** 0x1byte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-200/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of events. The issue lies in the processing of the dispatchEvent function. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206171

## Disclosure Timeline

- 2015-12-17 - Vulnerability reported to vendor
- 2016-03-22 - Coordinated public release of advisory
