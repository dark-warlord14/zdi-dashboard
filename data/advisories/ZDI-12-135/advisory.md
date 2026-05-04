# ZDI-12-135: Apple QuickTime JPEG2k Sample Size Atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-135
- **ZDI-CAN:** ZDI-CAN-1459
- **Date:** 2012-08-03
- **CVE:** CVE-2012-0661
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-135/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Apple QuickTime handles movies with the jpeg2k codec. When the size for a sample defined in the stsz atom is too big the QuickTime player fails to allocate the required memory for that sample. A pointer to the previous sample data still exists after the previous sample got freed. This pointer normally gets updated to point to the current sample data, but this does not happen when the allocation fails. The QuickTime player then re-uses the stale pointer and a use-after-free situation occurs. This can lead to remote code execution under that context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
