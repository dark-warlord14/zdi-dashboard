# ZDI-10-064: Mozilla Firefox WOFF Font Format dirEntry Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-064
- **ZDI-CAN:** ZDI-CAN-741
- **Date:** 2010-04-06
- **CVE:** CVE-2010-1028
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-064/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the browser loads a WOFF-based font. Upon calculating the length of some data read from the file, the application will miscalculate a size used for an allocation, and then copy an incorrect amount of data into that buffer. Due to the difference between the size of the allocation and the size of the copy, a buffer overflow will occur which can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-08.html

## Disclosure Timeline

- 2010-03-22 - Vulnerability reported to vendor
- 2010-04-06 - Coordinated public release of advisory
