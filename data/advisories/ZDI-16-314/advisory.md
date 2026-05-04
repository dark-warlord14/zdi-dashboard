# ZDI-16-314: Apple iOS MDM Profile Signing Bypass

## Metadata

- **ZDI ID:** ZDI-16-314
- **ZDI-CAN:** ZDI-CAN-3429
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1766
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** iOS
- **Credit:** Taylor Boyko
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-314/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple iOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of signed MDM profiles. The issue lies in the failure to properly check the certificate chain. An attacker can leverage this vulnerability to make a MDM profile appear to be trusted.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206166

## Disclosure Timeline

- 2015-12-03 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
