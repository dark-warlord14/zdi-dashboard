# ZDI-10-042: Apple QuickTime MediaVideo Compressor Name Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-042
- **ZDI-CAN:** ZDI-CAN-570
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0528
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists during the parsing of malformed MediaVideo data from a sample description atom (STSD). The application will read a length from the file, subtract 1 and then use it as a counter for a loop. Certain values may cause memory corruption and can result in code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4104

## Disclosure Timeline

- 2009-08-20 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
