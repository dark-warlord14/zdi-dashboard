# ZDI-11-254: Apple QuickTime 'trun' atom sampleCount Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-254
- **ZDI-CAN:** ZDI-CAN-1262
- **Date:** 2011-08-16
- **CVE:** CVE-2011-0256
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-254/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles the 'trun' atom. Quicktime uses user supplied data in the 'sampleCount' field to calculate a buffer size. An integer wrap can occur that results in the allocation of a memory buffer that is smaller than intended. When Quicktime writes to this buffer it causes a memory corruption that can lead to remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-06-03 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
