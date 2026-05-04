# ZDI-16-439: Apple OS X ACMP4AACBaseDecoder Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-439
- **ZDI-CAN:** ZDI-CAN-3718
- **Date:** 2016-07-20
- **CVE:** CVE-2016-4646
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-439/
## Vulnerability Details

This vulnerability allows remote attackers to leak sensitive information on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of MOV files. The issue lies in the failure to validate a user-supplied value prior to using it as the size parameter in a call to memcpy. An attacker can leverage this vulnerability to leak sensitive information in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206903

## Disclosure Timeline

- 2016-05-05 - Vulnerability reported to vendor
- 2016-07-20 - Coordinated public release of advisory
