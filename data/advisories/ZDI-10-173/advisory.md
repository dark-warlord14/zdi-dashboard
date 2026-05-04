# ZDI-10-173: Mozilla Firefox nsTreeSelection Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-173
- **ZDI-CAN:** ZDI-CAN-903
- **Date:** 2010-09-13
- **CVE:** CVE-2010-2760
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-173/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the fix implemented for CVE-2010-2753 in the nsTreeSelection interface. In a certain condition, the application still can be made to free a reference and then made to use said freed reference. This can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-54.html

## Disclosure Timeline

- 2010-08-09 - Vulnerability reported to vendor
- 2010-09-13 - Coordinated public release of advisory
