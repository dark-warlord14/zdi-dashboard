# ZDI-10-255: Apple QuickTime m1s Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-255
- **ZDI-CAN:** ZDI-CAN-839
- **Date:** 2010-11-10
- **CVE:** CVE-2010-3792
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-255/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the quicktime.qtx. When handling the m1s atom an integer value is used as an offset into a buffer. Minimal validation is done and an attacker can supply a negative value. This can be used to write to an arbitrary address in process memory. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Fixed in Mac OS X 10.6.5: http://support.apple.com/kb/HT4435 QuickTime 7.6.9: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-11-10 - Coordinated public release of advisory
