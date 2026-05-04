# ZDI-12-105: Apple QuickTime Text Track Descriptor Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-105
- **ZDI-CAN:** ZDI-CAN-1408
- **Date:** 2012-06-27
- **CVE:** CVE-2012-0664
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-105/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way QuickTime handles text track descriptors. Values for almost all of the text descriptors recognized by QuickTime will be read into a fixed-length buffer. This can lead to a heap-based buffer overflow which can result in remote code execution under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-12-27 - Vulnerability reported to vendor
- 2012-06-27 - Coordinated public release of advisory
- 2019-07-19 - Advisory Updated
