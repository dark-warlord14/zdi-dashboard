# ZDI-18-280: Spotify Music Player URI parsing Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-280
- **ZDI-CAN:** ZDI-CAN-5501
- **Date:** 2018-04-10
- **CVE:** CVE-2018-1167
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Spotify
- **Affected Products:** Music Player
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-280/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Spotify Music Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of URI handlers. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Fixed in version 1.0.73.345

## Disclosure Timeline

- 2018-01-26 - Vulnerability reported to vendor
- 2018-04-10 - Coordinated public release of advisory
- 2018-04-12 - Advisory Updated
