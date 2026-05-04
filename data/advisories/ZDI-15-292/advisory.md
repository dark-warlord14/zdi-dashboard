# ZDI-15-292: Apple QuickTime SGI Image File Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-292
- **ZDI-CAN:** ZDI-CAN-2948
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3669
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-292/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SGI Image Files. By providing a malformed file, an attacker can overflow a fixed sized region of the heap. This could allow an attacker to execute arbitrary code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2015-06-02 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
