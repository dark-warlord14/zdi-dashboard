# ZDI-09-025: Apple Quicktime Picture Viewer FLC Delta-Encoded Frame Decompression Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-025
- **ZDI-CAN:** ZDI-CAN-402
- **Date:** 2009-06-02
- **CVE:** CVE-2009-0951
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-025/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of QuickTime Player. User interaction is required to exploit this vulnerability in that the target must either open a malicious file, or visit a malicious web page. The specific flaw exists during decompression of a delta-encoded chunk. The algorithm to decompress the frame trusts a line specifier when calculating where to write decompressed data. This results in a relative write using attacker supplied values which can lead to remove code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3591

## Disclosure Timeline

- 2008-10-28 - Vulnerability reported to vendor
- 2009-06-02 - Coordinated public release of advisory
