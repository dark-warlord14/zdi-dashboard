# ZDI-12-004: Apple Quicktime JPEG2000 COD Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-004
- **ZDI-CAN:** ZDI-CAN-1184
- **Date:** 2012-01-05
- **CVE:** CVE-2011-3250
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime 7.3
- **Credit:** Luigi Auriemma Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the JP2Deco component which is used when handling an mjp2 sample. This sample format (JPEG2000) has a required COD marker segment (0xff52) followed by a COD length value. When extracting the contents of this section the application subtracts from this length before passing it into a call to memcpy. A remote attacker can exploit this error to execute arbitrary code under the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5016

## Disclosure Timeline

- 2011-07-25 - Vulnerability reported to vendor
- 2012-01-05 - Coordinated public release of advisory
