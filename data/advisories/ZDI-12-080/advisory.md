# ZDI-12-080: Adobe Flash Player MP4 Stream Decoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-080
- **ZDI-CAN:** ZDI-CAN-1470
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0754
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-080/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MP4 files. A size value is read from MP4 files and used for size calculation without proper validation. The arithmetic performed on the size value can cause integer overflows, resulting in undersized allocations. This undersized memory allocation can be subsequently overpopulated with data supplied by the input file which can be used to gain remote code execution under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb12-03.html

## Disclosure Timeline

- 2012-01-12 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
