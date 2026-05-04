# ZDI-16-527: Apple Safari HTMLVideoElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-527
- **ZDI-CAN:** ZDI-CAN-3852
- **Date:** 2016-09-27
- **CVE:** CVE-2016-4768
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-527/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HTMLVideoElement objects. By manipulating a document's elements an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207157

## Disclosure Timeline

- 2016-07-12 - Vulnerability reported to vendor
- 2016-09-27 - Coordinated public release of advisory
