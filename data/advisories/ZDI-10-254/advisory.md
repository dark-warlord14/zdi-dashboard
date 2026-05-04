# ZDI-10-254: Apple QuickTime ELST MediaRate Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-254
- **ZDI-CAN:** ZDI-CAN-838
- **Date:** 2010-11-10
- **CVE:** CVE-2010-3791
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-254/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the QuickTimeMPEG.qtx module. When handling an ELST atom's edit list table data large values are not handled properly. Specifically, the media rate field is explicitly trusted and can be abused to control memory copy operations. By specifying a large enough value, an attacker can utilize this to write to an arbitrary address in process memory. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Fixed in Mac OS X 10.6.5: http://support.apple.com/kb/HT4435 QuickTime 7.6.9: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-11-10 - Coordinated public release of advisory
