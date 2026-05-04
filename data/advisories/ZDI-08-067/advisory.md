# ZDI-08-067: Apple CUPS HP-GL/2 Filter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-067
- **ZDI-CAN:** ZDI-CAN-367
- **Date:** 2008-10-09
- **CVE:** CVE-2008-3641
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-067/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple CUPS. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Hewlett-Packard Graphics Language filter. Inadequate bounds checking on the pen width and pen color opcodes result in an arbitrary memory overwrite allowing for the execution of arbitrary code as the "hgltops" process uid.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3216

## Disclosure Timeline

- 2008-08-19 - Vulnerability reported to vendor
- 2008-10-09 - Coordinated public release of advisory
