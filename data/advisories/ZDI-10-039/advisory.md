# ZDI-10-039: Apple OS X Internet Enabled Disk Image Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-039
- **ZDI-CAN:** ZDI-CAN-537
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0497
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Brian Mastenbrook
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the handling of internet enabled disk image files. When a specially crafted Menu Extras plugin is included in the disk image, it is executed without further interaction allowing for arbitrary code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4077

## Disclosure Timeline

- 2009-08-10 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
