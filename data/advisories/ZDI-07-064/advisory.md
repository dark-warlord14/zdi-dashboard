# ZDI-07-064: Novell Client Trust Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-064
- **ZDI-CAN:** ZDI-CAN-199
- **Date:** 2007-10-31
- **CVE:** CVE-2007-5767
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Border Manager
- **Credit:** uvinc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-064/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell software which utilize the Novell Client Trust. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Novell Client Trust application, clntrust.exe, which listens by default on UDP port 3024 on Novell client machines. During a validation request, the Client Trust process copies a user-supplied Novell tree name until a wide-character backslash or a NULL is encountered. If neither is found within the data, the process will copy excess data which later overflows a static buffer during a call to wsprintfA.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=AuOWp2Xsvmc~

## Disclosure Timeline

- 2007-07-17 - Vulnerability reported to vendor
- 2007-10-31 - Coordinated public release of advisory
