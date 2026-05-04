# ZDI-11-342: Novell ZENworks Asset Management Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-342
- **ZDI-CAN:** ZDI-CAN-1282
- **Date:** 2011-12-07
- **CVE:** CVE-2011-2653
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-342/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Zenworks Asset Management. Authentication is not required to exploit this vulnerability. The flaw exists within the rtrlet component. This process listens on TCP port 8080. When handling an unauthenticated file upload the process does not properly sanitize the path. Directory traversal can be used to drop a file in an arbitrary location and a null byte inserted into the filename to provide arbitrary extension. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=hPvHtXeNmCU~

## Disclosure Timeline

- 2011-07-25 - Vulnerability reported to vendor
- 2011-12-07 - Coordinated public release of advisory
